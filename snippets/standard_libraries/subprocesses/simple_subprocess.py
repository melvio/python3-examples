#!/usr/bin/env python3
import os
import subprocess

result = subprocess.run(["ls", "-l"])
print(result)  # CompletedProcess(args=['ls', '-l'], returncode=0)
print(result.args)  # ['ls', '-l']
print(result.returncode)  # 0

result = subprocess.run(["echo", "${PATH}"])  # This will echo ${PATH} literally
print(result)  # CompletedProcess(args=['echo', '${PATH}'], returncode=0)

result = subprocess.run(["echo", "${PATH}"], capture_output=True)
print(result)  # CompletedProcess(args=['echo', '${PATH}'], returncode=0, stdout=b'${PATH}\n', stderr=b'')
print(result.stdout)  # b'${PATH}\n'

