import angr

"""
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

flag: EZ9dmq4c8g9G7bAV
"""


def main():
    proj = angr.Project("serial")

    state = proj.factory.blank_state(addr=0x400A3C)
    simgr = proj.factory.simulation_manager(state)
    simgr.explore(find=(0x400C5C))

    solution_state = simgr.found[0]
    print(print(solution_state.posix.dumps(0)))
    print(solution_state.solver.BVV(0x200, 16))
    print(solution_state.regs.rbp-0x200)


if __name__ == "__main__":
    main()
