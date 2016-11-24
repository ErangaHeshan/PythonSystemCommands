import os

# get current working directory
cwd = os.getcwd()
# get the full path to the directory a Python file is contained in
cfp = os.path.dirname(os.path.realpath(__file__))
print(cwd)
print(cfp)
