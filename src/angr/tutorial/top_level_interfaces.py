"""
https://docs.angr.io/core-concepts/toplevel
"""
import angr
import logging

logging.getLogger('cle').setLevel('ERROR')

# Create Angr project
proj = angr.Project('./bin/true')

# For hex - non hex transformation
# import monkeyhex # this will format numerical results in hexadecimal automatically in command line
assert proj.entry == int(hex(proj.entry), 16)

# Basic properties
print(proj.arch)  # architecture the program is compiled with
print(hex(proj.entry))  # entry is the entry point of the binary
print(proj.filename)  # is the absolute filename of the binary

# Loader
print(proj.loader)

if __name__ == '__main__':
    pass
