#! /usr/bin/env python
# -*- coding: utf-8 -*-

name = "শুভদীপ মৈত্র"
name_utf8 = '\xe0\xa6\xb6\xe0\xa7\x81\xe0\xa6\xad\xe0\xa6\xa6\xe0\xa7\x80\xe0\xa6\xaa \xe0\xa6\xae\xe0\xa7\x88\xe0\xa6\xa4\xe0\xa7\x8d\xe0\xa6\xb0'
name_unicode = name.decode("utf-8")
# or name_unicode = name_utf8.decode("utf-8")

print(("My name is ",name_unicode.encode("utf-8")));

with open(name_unicode,"w") as fout : 
    fout.write("The filename is my name in Bengali :-)")

