#coding=utf-8
#!/usr/bin/python


import cgi,cgitb
import MySQLdb

if environ.has_key('HTTP_COOKIE'):
    for cookie in map(strip,split(envirion['HTTP_COOKIE'],';')):
        (key,value) = split(cookie,'=');
        if key == "UserID":
            user_id = value
        if key == "Password":
            password = value

print "User ID = %s " % user_id
print "Password = %s " % password
