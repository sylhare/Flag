import angr
import claripy

proj = angr.Project("sym_exec.elf", auto_load_libs=False)

argv = claripy.BVS("argv1", 8 * 8)  # Represents an absract of 8bits long variable that is passed to the program
state = proj.factory.entry_state(args=[proj.filename, argv])

simgr = proj.factory.simgr(state)
simgr.explore(find=lambda s: b'WIN' in s.posix.dumps(1),
              avoid=lambda s: b'FAIL\n' in s.posix.dumps(1))

print(simgr.stashes)  # all of the stashes
print(simgr.found[0].posix.dumps(1))

if __name__ == "__main__":
    pass
