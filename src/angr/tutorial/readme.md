# Angr Tutorial

From [Angr Docs](https://docs.angr.io/core-concepts/)

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