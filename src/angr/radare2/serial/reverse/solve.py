import angr

"""
Solving reserial - NOT WORKING
flag: EZAV

```
python solve.py
```
"""


def main():
    proj = angr.Project("reserial")

    state = proj.factory.blank_state(addr=0x100000ea4)
    simgr = proj.factory.simulation_manager(state)
    simgr.explore(find=0x100000f30)

    solution_state = simgr.found[0]
    print(print(solution_state.posix.dumps(0)))
    print(solution_state.solver.BVV(0x10, 4))
    print(solution_state.regs.rbp-0x10)


if __name__ == "__main__":
    main()
