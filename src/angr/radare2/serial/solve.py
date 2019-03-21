import angr

"""
Solving serial

0x00400A3C is where the input is loaded
0x00400c5c is the address where there is "success"
0x00400c84 is the address where it is wrong

flag: EZ9dmq4c8g9G7bAV
"""


def main():
    proj = angr.Project("serial")

    state = proj.factory.blank_state(addr=0x00400A3C)
    simgr = proj.factory.simulation_manager(state)
    simgr.explore(find=0x00400c5c, avoid=0x00400c84)

    solution_state = simgr.found[0]
    print(print(solution_state.posix.dumps(0)))
    print(solution_state.solver.BVV(0x200, 16))
    print(solution_state.regs.rbp-0x200)


if __name__ == "__main__":
    main()
