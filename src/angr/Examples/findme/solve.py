import sys

import angr


def main(argv):
    project = angr.Project("./findme")
    initial_state = project.factory.entry_state()
    simulation = project.factory.simgr(initial_state)

    simulation.explore(find=0x8048678)

    if simulation.found:
        solution_state = simulation.found[0]
        solution = solution_state.posix.dumps(sys.stdin.fileno())
        print("[+] Success! Solution is: {}".format(solution.decode("utf-8")))

    else:
        raise Exception('Could not find the solution')


project = angr.Project("./findme", auto_load_libs=False)


@project.hook(0x8048678)
def print_flag(state):
    print("FLAG SHOULD BE:", state.posix.dumps(0))
    project.terminate_execution()


project.execute()

if __name__ == '__main__':
    main(sys.argv)
