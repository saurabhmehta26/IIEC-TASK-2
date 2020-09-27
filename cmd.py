#! /usr/bin/python3
import cgi
import subprocess
print("context-type: text/html")
print()

i = cgi.FieldStorage()
c = i.getvalue("x")
cm = "sudo " + c
op = subprocess.getoutput(cm)
print("""<html><style>body{background-color:rgb(200,200,200);color:black;}</style><h2>Your Output: <h2></html>""")
print(op)
