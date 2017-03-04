#!/usr/bin/env python2
# vim: sw=4 ts=4 sts=4 et

import os
import re
import sys
import glob
import string

from collections import defaultdict
from collections import Counter
from itertools import ifilterfalse


def is_abs_http_ref(r):
    return r.startswith('http://') or r.startswith('https://')


def trim_title(r):
    return r.strip()


re_title = re.compile('\n#+ (.*)\n')                  # markdown title, e.g.
                                                      #    `## Higher-Order Functions`

re_hash = re.compile(r'\{:#([a-z0-9-_]+)\}')          # explicit specified hash, e.g.
                                                      #    `{:#qualified}`

re_cross_refs = re.compile(r'\]\(([^)]+#[^)]+)\)')    # references to hash in other markdown file, e.g.
                                                      #    `](visibility-modifiers.html#constructors)`

re_inner_refs = re.compile(r'\]\((#[^)]+)\)')         # references to hash in same markdown file, e.g.
                                                      #    `](#null-safety-and-platform-types)`


def get_missed_hashes(path, white_list=set(), tidy_title=trim_title):
    def is_hash_char(c):
        return c == '-' or c not in string.punctuation

    def title_to_hash(title):
        # make the tidied title lower case, remove any punctuation, and then replace all blank space to bar
        return filter(is_hash_char, tidy_title(title).lower()).replace(' ', '-')

    all_hashes = set()
    all_refs = set()
    refs_map = defaultdict(dict)

    os.chdir(path)
    md_names = glob.glob('*.md') + glob.glob('*.markdown')

    for txt, page_name in ((open(md_name).read(), md_name.replace('md', 'html')) for md_name in md_names):
        # title and explicit specified hash
        page_hashes = [page_name + "#" + title_to_hash(title) for title in re_title.findall(txt)] + \
                      [page_name + hash_ for hash_ in re_hash.findall(txt)]

        all_hashes.update(page_hashes)

        # cross references and inner references
        refs = re_cross_refs.findall(txt) + \
               [page_name + ref for ref in re_inner_refs.findall(txt)]

        all_refs.update(refs)
        for ref, cnt in Counter(refs).iteritems():
            refs_map[ref].update({page_name: cnt})

    return refs_map, all_refs - all_hashes - white_list


def print_result(refs_map, all_missed, is_outer=is_abs_http_ref):
    print '\n-- missed hash references --'
    for ref in sorted(ifilterfalse(is_outer, all_missed)):
        print ref
        print '\t', dict(refs_map[ref])

    print '\n-- outer hash references (need manually verify) --'
    for ref in sorted(filter(is_outer, all_missed)):
        print ref
        print '\t', dict(refs_map[ref])


if __name__ == '__main__':
    print_result(*get_missed_hashes(len(sys.argv) > 1 and sys.argv[1] or '.'))
