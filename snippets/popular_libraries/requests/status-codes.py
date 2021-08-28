from requests.status_codes import codes

print(codes)  # <lookup 'status_codes'>

print(codes["ok"])  # 200
print(codes["OK"])  # 200
print(codes.ok)  # 200
print(codes.okay)  # 200
print(codes.OK)  # 200

print(codes["\o/"])  # I believe this is an inside joke


print(codes.teapot)
