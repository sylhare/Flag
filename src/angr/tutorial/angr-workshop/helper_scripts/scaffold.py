#!/usr/bin/env python
# angr
import angr

# interactive plugin

# sensible logging
import logging
logging.getLogger("angr.sim_manager").setLevel(logging.INFO)

# Options for the Project
filename = "/bin/ls"
use_libs = False

p = angr.Project(filename, auto_load_libs=use_libs)
print("[!] created angr project for "+p.filename)

### YOUR CODE HERE

# cfg = p.analyses.CFGFast(show_progressbar=True)
# e = p.factory.entry_state()
# simgr = p.factory.simgr(e)
# ...