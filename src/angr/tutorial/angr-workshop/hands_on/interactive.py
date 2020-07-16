import angr
import claripy

# from angrcli.interaction.explore import ExploreInteractive
#import angrcli.plugins.watches
#import angrcli.plugins.context_view

#import angr.sim_state
#angr.sim_state.SimState.__repr__ = lambda self: self.context_view.pprint()

#from angrcli.interaction.explore import ExploreInteractive

#proj = angr.Project("hostcwd/10.8.217.27:8000/hands_on/sym_exec.elf")
#proj = angr.Project("hostcwd/10.8.217.27:8000/exercise/ex_symexec.elf") # Needs two arguments
proj = angr.Project("hands_on/sym_exec.elf", auto_load_libs=False)

argv = claripy.BVS("argv1", 8 * 8) # Represents an absract of 8bits long variable that is passed to the program
argv2 = claripy.BVS("args2", 8 * 8)
state = proj.factory.entry_state(args=[proj.filename, argv])
state.watches.watch_bv(argv, cast_to=bytes)

# state = proj.factory.entry_state(args=[proj.filename, argv, argv2])
state = proj.factory.entry_state(args=[proj.filename, argv])

# entry = proj.factory.entry_state()
# simgr = proj.factory.simulation_manager(entry)
# simgr = proj.factory.simgr(state)
# simgr.explore()
#state.watches.watch_bv(argv, cast_to=bytes) # Watches the state and print the value of the defined argv in bytes
#state.watches.watch_bv(argv2, cast_to=bytes)

# print(simgr.stashes) # all of the stashes
# print(simgr.found[0].posix.dumps(0))

e = ExploreInteractive(proj, state)

# print to show the code
# step to go to the next step
# pick (1 or 0) to go to choose a branch
e.cmdloop()

# entry = proj.factory.entry_state()
# simgr = proj.factory.simulation_manager(entry)
# simgr.explore(find=lambda state: b'WIN' in state.posix.dumps(1))
              #avoid=lambda state: b'FAIL\n' in state.posix.dumps(1))
# print(simgr)
# print(simgr.deadended)
# print(simgr.stashes) # all of the stashes
# print(simgr.found[0].posix.dumps(0))

if __name__ == "__main__":
    pass