# Fauxware

Fauxware is an example of how to use `angr` from the [angr docs](https://docs.angr.io/examples).
I have added the source here for experimentation.

## Introduction

Look at `fauxware.c`! This is the source code for a "faux firmware".
It's meant to be a simple representation of a firmware that can authenticate users but also has a backdoor.
The backdoor is that anybody who provides the string `SOSNEAKY` as their password will be automatically authenticated.

## Make it work

First of all, you can re-compile the binary using `gcc` (it needs to be installed):
```bash
gcc -o fauxware fauxware.c
```

Then you can give it `executable` permission with:

```bash
chmod +x fauxware
```

Then if you run it alone, it should output ([angr-docs#238](https://github.com/angr/angr-doc/issues/248))
```bash
[+] ~/angr/angr-doc/examples/fauxware% ./fauxware
Username:
Password:
Go away!
```

Now if you run it, piping `solve.py` it will use the found backdoor:
```bash
[+] ~/angr/angr-doc/examples/fauxware% python solve.py | ./fauxware
Username: 
[[ a bunch of warnings ]]
Password: 
Welcome to the admin console, trusted user!
```

Et voilà, it works!