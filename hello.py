#!/usr/bin/env python
# ^ is called the shebang and tells the os how to run the file

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

print "Content-Type: text/html"
if username == "Bob" and password == "hunter2":
    print "Set-Cookie: logged_in=true"
print

print "<HTML><BODY>"
print "<H1>Hello World!</H1>"
print "Your color is: "
print form.getvalue('color')
print "</br>"
print "Your browser is: "

if "Firefox" in os.environ['HTTP_USER_AGENT']:
    print "Firefox"
if "Chrome" in os.environ['HTTP_USER_AGENT']:
    print "Chrome" 

print "</br></br>"

print "<FORM method='POST'>"
print "Login: "
print "<INPUT name='user' />"
print "</br>"
print "Password:"
print "<INPUT name='password' type='password'/>"
print "</br>"
print "<INPUT type='submit' /></FORM>"

print "</br></br>"

print "Username: " + str(username)
print "</br>"
print "Password: " + str(password)

if username == "Bob" and password == "hunter2":
    print "</br> Successful!!"

#print "</br></br>" + os.environ['HTTP_COOKIE']

#print "</br></br>" + json.dumps(dict(C), indent=2)

#print "</br></br> logged_in had value of " +C['logged_in'].value

if "logged_in" in C:
    print "</br></br> Cookie Exists"
else:
    print "</br></br> No Cookie"

#print json.dumps(dict(os.environ), indent=2, sort_keys=True)

print "</body></HTML>"




