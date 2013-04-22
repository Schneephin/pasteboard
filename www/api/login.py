#! /usr/bin/python2
import cgi
import cgitb; cgitb.enable()
import json

#get POST Data
form = cgi.FieldStorage() 
data = form.getvalue('data')
email = json.loads(data)['email']
passwd = json.loads(data)['password']

def generate_hash():
    """
        generate_hash 
        function to generate hash-key 
        @access public
    """
    import hashlib, time
    return hashlib.md5(email + str(time.time()).encode('utf-8')).hexdigest()

# @TODO: check values
# lookup on db and generate Token + timeout
# dummydata :
if not email or not passwd:
    retrun = { 'error': 'email or password is wrong' }
else:
    retrun = { 'token': generate_hash() }

# return access-Token
print "Content-Type: text/html\n"
print json.dumps(retrun)
