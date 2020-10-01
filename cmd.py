#! /usr/bin/python3
import cgi
import subprocess as sp
print("context-type: text/html")
print()

field_storage_var = cgi.FieldStorage()
user_command = field_storage_var.getvalue("x")
sudo_command_user = "sudo " + user_command
output_var = sp.getoutput(sudo_command_user)
print("""<html><style>body{background-color:rgb(200,200,200);color:black;}</style><h2>Your Output: <h2></html>""")
print(output_var)
