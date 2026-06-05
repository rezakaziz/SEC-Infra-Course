import sys, os
print("Python:", sys.version)
print("Executable:", sys.executable)
print("Prefix:", sys.prefix)
print("Base Prefix:", sys.base_prefix)
print("In virtual env:", sys.prefix != sys.base_prefix)
print("VIRTUAL_ENV:", os.environ.get("VIRTUAL_ENV"))
