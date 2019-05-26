import angr


def main():
    proj = angr.Project('re_challenge3', load_options={"auto_load_libs": False})
    state = proj.factory.entry_state(addr=0x00400ec8)
    simgr = proj.factory.simgr(state)

    simgr.explore(find=lambda s: b"Good boy!" in s.posix.dumps(1),
                  avoid=lambda s: b"Invalid flag!!" in s.posix.dumps(1))

    print(simgr.found[0].posix.dumps(0))


if __name__ == '__main__':
    main()
