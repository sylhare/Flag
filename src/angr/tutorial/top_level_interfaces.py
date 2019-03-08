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
print("\n\n Basic Properties:\n")
print(proj.arch)                    # architecture the program is compiled with
print(hex(proj.entry))              # entry is the entry point of the binary
print(proj.filename)                # is the absolute filename of the binary

# Loader
print("\n\n Loader:\n")
print(proj.loader)                             # Loader which has the virtual space address of the binary
print(proj.loader.shared_objects)
print(hex(proj.loader.min_addr))
print(hex(proj.loader.max_addr))

print(proj.loader.main_object)                 # we've loaded several binaries into this project. Here's the main one!
print(proj.loader.main_object.execstack)       # Does this binary have an executable stack?
print(proj.loader.main_object.pic)             # Is this binary position-independent?

# Factory
# Blocks
print("\n\n Blocks:\n")
block = proj.factory.block(proj.entry)                # lift a block of code from the program's entry point)
block.pp()                                            # pretty-print a disassembly to stdout
print(block.instructions)                             # how many instructions are there?
print(list(hex(x) for x in block.instruction_addrs))  # what are the addresses of the instructions?
# print(block.capstone)                               # capstone disassembly
# print(block.vex)                                    # VEX IRSB (that's a python internal address, not a program address)

# States
print("\n\n States:\n")
state = proj.factory.entry_state()
print(state)                                    # When you're performing execution with angr, you are working with a simulated program state - a SimState
print(state.regs.rip)                           # get the current instruction pointer in the register
print(state.mem[proj.entry].int.resolved)       # interpret the memory at the entry point as C int (bitvector != python int)

# For bitvector - int transformation
bv = state.solver.BVV(0x1234, 32)           # create a 32-bit-wide bitvector with value 0x1234
print(bv)                                   # BVV means BitVector Value
print(hex(state.solver.eval(bv)))           # convert to python int

state.regs.rsi = state.solver.BVV(3, 64)    # You can store these bitvectors back to registers
print(state.regs.rsi)
state.mem[0x1000].long = 4                  # and memory (.long for the <type> the memory should be interpreted)
print(state.mem[0x1000].long.resolved)      # .resolved to get the value as a bitvector
print(state.mem[0x1000].long.concrete)      # .concrete to get the value as a python int

# Simulation Managers
print("\n\n Simulation Managers:\n")
simgr = proj.factory.simulation_manager(state)
print(simgr.active)                         # A simulation manager is the primary interface in angr for performing execution, simulation, whatever you want to call it, with states
simgr.step()                                # Make some execution
print(simgr.active)
print(simgr.active[0].regs.rip)             # To get the first state in the simulation
print(state.regs.rip)                       # Still the same as before the step
if __name__ == '__main__':
    pass
