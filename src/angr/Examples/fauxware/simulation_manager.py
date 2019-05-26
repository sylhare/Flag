import angr


def main():
    proj = angr.Project('./test/fauxware', auto_load_libs=False)
    state = proj.factory.entry_state()
    simgr = proj.factory.simgr(state)

    # Step until the first symbolic branch
    while len(simgr.active) == 1:
        simgr.step()

    print(simgr)
    print(simgr.active)

    # Step until everything terminates
    simgr.run()
    print(simgr)

    # let's move everything that has a certain string in its output:
    simgr.move(from_stash='deadended', to_stash='authenticated',
               filter_func=lambda s: b'Welcome' in s.posix.dumps(1))
    print(simgr)

    """
    We were able to just create a new stash named "authenticated" 
    just by asking for states to be moved to it.
    All the states in this stash have "Welcome" in their stdout, which is a fine metric for now.
    """

    for s in simgr.deadended + simgr.authenticated:
        print(hex(s.addr))

    print(simgr.one_deadended)
    print(simgr.mp_authenticated)
    print(simgr.mp_authenticated.posix.dumps(0))


def simple():
    proj = angr.Project('./test/fauxware', auto_load_libs=False)
    state = proj.factory.entry_state()
    simgr = proj.factory.simgr(state)
    simgr.explore(find=lambda s: b'Welcome' in s.posix.dumps(1))
    print(simgr.found[0].posix.dumps(0))


if __name__ == '__main__':
    simple()
    # main()
