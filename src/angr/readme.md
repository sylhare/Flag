# Angr Tutorial

From [Angr Docs](https://docs.angr.io/core-concepts/)

## Installation

You should check [here](https://docs.angr.io/introductory-errata/install)
If you follow the instruction and it doesn't work on kali linux, try:

```bash
apt install python3-pip
pip3 install angr
```

## Notes

For the `/bin/true` file:

```bash
file tutorial/bin/true 
tutorial/bin/true: Mach-O 64-bit executable x86_64
```

## Glossary

- **Position Independant executable ([PIE](https://en.wikipedia.org/wiki/Position-independent_code)):**
 is a body of machine code that, being placed somewhere in the primary memory, 
 executes properly regardless of its absolute address. It is suppose to be more secure. 
 
 
## Links

- [Unleash the angr](https://www.akulpillai.com/reverse-engineering/unleash-the-angr.php) 
- [jakespringer/angr_ctf](https://github.com/jakespringer/angr_ctf)