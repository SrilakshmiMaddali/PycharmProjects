#!/usr/bin/env python3

import os

print("HOME: "+os.environ.get("HOME",""))
print("SHELL: "+os.environ.get("SHELL",""))
print("FRUIT:" +os.environ.get("FRUIT",""))

import sys
print(sys.argv)

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep","2"])
result=subprocess.run(["ls","This_file_does_not_exist"])
print(result.returncode)

result = subprocess.run(["host","8.8.8.8"],capture_output=True)
print(result.returncode)
print(result.stdout) # results in a bites form starts with b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
print(result.stdout.decode())# converts the output to utf-8 standard form 8.8.8.8.in-addr.arpa domain name pointer dns.google.
print(result.stdout.decode().split())#['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
result=subprocess.run(["rm","file_does_not_exist"],capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)


import os
import subprocess

my_env=os.environ.copy()
my_env["PATH"] = os.pathsep.join(["opt/myapp/",my_env["PATH"]])
result = subprocess.run(["myapp"],env=my_env)