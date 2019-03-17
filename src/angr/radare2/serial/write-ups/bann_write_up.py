import angr

"""
@author: Michael Bann
@source: https://bannsecurity.com/index.php/home/10-ctf-writeups/29-sharif-university-ctf-2016-serial
"""

proj = angr.Project("serial")
# Not valid since path have been replace with simulation manager
# Start angr up right at the point where we start validating
state = proj.factory.blank_state(addr=0x400A3C)

pg = proj.factory.path_group(state,immutable=False)

# Explore until we find the end state where we won
pg.explore(find=(0x400C5C))

# Ask angr what the answer is. Note, static analysis is how we know rbp-0x200 is us
# as well as knowing that it's 16 characters long
s = pg.found[0].state.copy()
s.se.any_str(s.memory.load(s.regs.rbp-0x200,16))

# flag: EZ9dmq4c8g9G7bAV
