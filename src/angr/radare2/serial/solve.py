import angr

"""
Solving serial

0x00400A3C is where the input is loaded
0x00400c5c is the address where there is "success"
0x00400c84 is the address where it is wrong

flag: EZ9dmq4c8g9G7bAV
"""


def main():
    project = angr.Project("./serial")
    state = project.factory.blank_state(addr=0x400A3C)

    simulation = project.factory.simgr(state)
    simulation.explore(find=0x400C5C)

    solution_state = simulation.found[0]
    # pointer for registry rbp-0x200 where the password is saved
    pointer = solution_state.regs.rbp-0x200
    # content is a bit vector of size 16
    state_bit_vector = solution_state.memory.load(pointer, 16)
    # return the eval bit vector to data
    return solution_state.solver.eval(state_bit_vector, cast_to=bytes)


if __name__ == "__main__":
    print(main())
    # >> b'EZ9dmq4c8g9G7bAV'
