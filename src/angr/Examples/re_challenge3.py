import angr


def main():
    proj = angr.Project('re_challenge3', load_options={"auto_load_libs": False})
    simgr = proj.factory.simgr()

    simgr.explore(find=lambda state: b"Good boy!" in state.posix.dumps(1),
                  avoid=lambda state: b"Invalid flag!!" in state.posix.dumps(1))
    s = simgr.found[0]

    print(s.posix.dumps(1))
    flag = s.posix.dumps(0).split(b'\0')[0]
    print(flag)


if __name__ == '__main__':
    main()
