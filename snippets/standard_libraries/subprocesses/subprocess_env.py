#!/usr/bin/env python3
import os
import subprocess

print("*" * 50)
subprocess.run(["env"], env=None)  # env=None is the default and returns the same as env=os.environ
print("*" * 50)

print("*" * 50)
subprocess.run(["env"], env={"ZZ": "My Value"})  # replace the entire environment with your variables
print("*" * 50)


print("*" * 50)
print("Empty environment")
subprocess.run(["env", "-i"])
print("*" * 50)

print("*" * 50)
print("Add something to the environment")
print("*" * 50)
my_env = os.environ
my_env["ZZ"] = "My Value"
subprocess.run(["env"], env=my_env)
