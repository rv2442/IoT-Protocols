#!/usr/bin/env python
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

# 200 OK

data1 = r1.read()  # This will return entire content.


# The following example demonstrates reading data in chunks.
conn.request("GET", "/")
r1 = conn.getresponse()
while r1.read(200):
	print(repr(r1.read(200)))


# Example of an invalid request
conn = http.client.HTTPSConnection("docs.python.org")
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)

# 404 Not Found

data2 = r2.read()
conn.close()