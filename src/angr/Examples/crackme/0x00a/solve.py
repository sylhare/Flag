import angr

# mov dword [esp], str.Congrats_ ; [0x8048654:4]=0x676e6f43 LEA str.Congrats_ ; "Congrats!" @ 0x8048654
# mov dword [esp], str.Wrong_ ; [0x804865e:4]=0x6e6f7257 LEA str.Wrong_ ; "Wrong!" @ 0x804865e


def main():
    proj = angr.Project('crackme0x00a', load_options={"auto_load_libs": False})
    simgr = proj.factory.simgr()

    simgr.explore(find=lambda x: b"Congrats" in x.posix.dumps(1))
    s = simgr.found[0]

    print(s.posix.dumps(1))
    flag = s.posix.dumps(0).split(b'\0')[0]
    print(flag)


if __name__ == '__main__':
    main()
