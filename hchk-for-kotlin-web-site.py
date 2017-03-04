#!/usr/bin/env python2
# vim: sw=4 ts=4 sts=4 et

import sys
from hchk import get_missed_hashes, print_result, is_abs_http_ref, trim_title


def tidy_title(title):
    return trim_title(title).replace('{: .keyword }', '').lower()


def is_outer_ref(r):
    # grammar.html is not supported currently
    return r.startswith('grammar.html#') or is_abs_http_ref(r)

if __name__ == '__main__':
    # `<a name="declarations"` is not supported currently
    white_list = {'type-safe-builders.html#declarations'}

    path = len(sys.argv) > 1 and sys.argv[1] or '.'
    refs_map, all_missed = get_missed_hashes(path, white_list, tidy_title)

    print_result(refs_map, all_missed, is_outer_ref)
