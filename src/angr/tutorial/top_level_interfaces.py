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
print(proj.loader)  # Loader which has the virtual space address of the binary
print(proj.loader.shared_objects)
print(hex(proj.loader.min_addr))
print(hex(proj.loader.max_addr))

print(proj.loader.main_object)  # we've loaded several binaries into this project. Here's the main one!
print(proj.loader.main_object.execstack)  # Does this binary have an executable stack?
print(proj.loader.main_object.pic)  # Is this binary position-independent?



if __name__ == '__main__':
    pass
