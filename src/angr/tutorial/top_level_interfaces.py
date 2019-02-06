import angr
import monkeyhex # this will format numerical results in hexadecimal

proj = angr.Project('./bin/true')

print(proj.arch)
print(proj.entry)
print(proj.filename)

if __name__ == '__main__':
    ''
