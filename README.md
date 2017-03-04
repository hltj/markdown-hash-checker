# markdown-hash-checker
A invalid hash references checker for markdown-based sites or GitBooks etc.

## Usage

```bash
path/to/hchk.py [dir]
```
Check for if there are any invalid hash references in the markdown files under the specified directory.  
Note that recursive sub-directories are not supported currently.

### For normal markdown-based sites or GitBooks

```bash
cd path/to/markdown-dir
path/to/hchk.py
```
or
```bash
./hchk.py path/to/markdown-dir
```

### Specially for [kotlin-web-site](https://github.com/JetBrains/kotlin-web-site)

```bash
cd path/to/kotlin-web-site/pages/docs/reference
path/to/hchk-for-kotlin-web-site.py
```
or
```bash
./hchk-for-kotlin-web-site.py path/to/kotlin-web-site/pages/docs/reference
./hchk-for-kotlin-web-site.py path/to/kotlin-web-site/pages/docs/tutorials
```

### Simple output

```
-- missed hash references --

-- outer hash references (need manually verify) --
grammar.html#callSuffix
        {'lambdas.html': 1}
grammar.html#for
        {'control-flow.html': 1}
grammar.html#if
        {'control-flow.html': 1}
grammar.html#import
        {'packages.html': 1}
grammar.html#labelReference
        {'returns.html': 1}
grammar.html#precedence
        {'operator-overloading.html': 1, 'typecasts.html': 1}
grammar.html#when
        {'control-flow.html': 1}
grammar.html#while
        {'control-flow.html': 1}
http://en.wikipedia.org/wiki/Tony_Hoare#Apologies_and_retractions
        {'null-safety.html': 1}
http://try.kotlinlang.org/#/Examples/Longer examples/HTML Builder/HTML Builder.kt
        {'type-safe-builders.html': 1}
http://www.groovy-lang.org/dsls.html#_nodebuilder
        {'type-safe-builders.html': 1}
http://www.groovy-lang.org/processing-xml.html#_creating_xml
        {'type-safe-builders.html': 1}
https://www.manning.com/books/kotlin-in-action#downloads
        {'index.html': 1}
```
