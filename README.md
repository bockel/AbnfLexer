# IETF ABNF Lexer

A [pygments][] lexer for the Augmented Backus-Naur Format ([ABNF][])
used by the IETF.

A formal definition of the IETF ABNF format is defined in [RFC5234][]
and available at http://tools.ietf.org/html/rfc5234.

The lexer can be used to parse the following

```abnf
; IEFT ABNF Grammar defined in ABNF
; RFC5234: http://tools.ietf.org/html/rfc5234

rulelist       =  1*( rule / (*c-wsp c-nl) )
rule           =  rulename defined-as elements c-nl
                    ; continues if next line starts
                    ;  with white space
rulename       =  ALPHA *(ALPHA / DIGIT / "-")
defined-as     =  *c-wsp ("=" / "=/") *c-wsp
                    ; basic rules definition and
                    ;  incremental alternatives
elements       =  alternation *c-wsp
c-wsp          =  WSP / (c-nl WSP)
c-nl           =  comment / CRLF
                    ; comment or newline
comment        =  ";" *(WSP / VCHAR) CRLF
alternation    =  concatenation *(*c-wsp "/" *c-wsp concatenation)
concatenation  =  repetition *(1*c-wsp repetition)
repetition     =  [repeat] element
repeat         =  1*DIGIT / (*DIGIT "*" *DIGIT)
element        =  rulename / group / option / char-val / num-val / prose-val
group          =  "(" *c-wsp alternation *c-wsp ")"
option         =  "[" *c-wsp alternation *c-wsp "]"
char-val       =  DQUOTE *(%x20-21 / %x23-7E) DQUOTE
                    ; quoted string of SP and VCHAR
                    ;  without DQUOTE
num-val        =  "%" (bin-val / dec-val / hex-val)
bin-val        =  "b" 1*BIT [ 1*("." 1*BIT) / ("-" 1*BIT) ]
                    ; series of concatenated bit values
                    ;  or single ONEOF range
dec-val        =  "d" 1*DIGIT [ 1*("." 1*DIGIT) / ("-" 1*DIGIT) ]
hex-val        =  "x" 1*HEXDIG [ 1*("." 1*HEXDIG) / ("-" 1*HEXDIG) ]
prose-val      =  "<" *(%x20-3D / %x3F-7E) ">"
                    ; bracketed string of SP and VCHAR
                    ;  without angles
                    ; prose description, to be used as
                    ;  last resort
```

## Install

First, ensure that both [setuptools][] and [pygments][] are installed.

Then,  install using `setuptools`. This will use setuptools entrypoint
to install the lexer and make it accessible from pygments

```
python setup.py install
```

## Test

Now the lexer can be accessed via pygments.

`pygmentize` can be used to verify that the lexer was properly
installed. To run `pygmentize` on the provided w3c.ebnf grammar:

```
pygmentize -f html -l abnf -O full ietf.abnf > temp.html
```

and view the results in any browser.


# License

Copyright 2013 William Heinbockel

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


[pygments]: http://pygments.org/
[ABNF]: http://en.wikipedia.org/wiki/Augmented_Backus%E2%80%93Naur_Form
[RFC5234]: http://tools.ietf.org/html/rfc5234
[setuptools]: https://pypi.python.org/pypi/setuptools
