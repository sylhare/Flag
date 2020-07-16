#!/usr/bin/env python
# angr
import angr

# interactive plugin

# sensible logging
import logging
logging.getLogger("angr.sim_manager").setLevel(logging.INFO)

# Options for the Project
filename = "./md5_ex.elf"
use_libs = False

p = angr.Project(filename, auto_load_libs=use_libs)
print("[!] created angr project for "+p.filename)

class md5Hook(angr.SimProcedure):
    def run(self, inputBytes, length, resultBuffer):
        print("In Hook")
        lengths = self.state.solver.eval_upto(length, 10, cast_to=int)
        if len(lengths) > 1:
            print("WARNING, SYMBOLIC LENGTH")
            return
        l = lengths[0]
        data = self.state.memory.load(addr=inputBytes, size=l)
        datas = self.state.solver.eval_upto(data, 10, cast_to=bytes)
        if len(datas) > 1:
            print("WARNING, SYMBOLIC DATA")
            return
        from hashlib import md5
        m = md5()
        m.update(datas[0])
        h = m.digest()
        self.state.memory.store(addr=resultBuffer, data=h)

p.hook_symbol('MD5', md5Hook())

#p.execute()

e = p.factory.entry_state()
simgr = p.factory.simgr(e)
simgr.explore()
print(simgr)
print(simgr.one_deadended.posix.dumps(1))
# ...
