# https://blog.rpis.ec/2018/05/northsec-2018-marsanalytica.html
import angr


def constrain_stdin(st):
    for _ in range(19):
        k = st.posix.files[0].read_from(1)
        st.solver.add(k > 0x20)
        st.solver.add(k < 0x7f)
    st.posix.files[0].seek(0)
    st.posix.files[0].length = 19


p = angr.Project("./MarsAnalytica")
s = p.factory.entry_state(add_options=angr.options.unicorn)
constrain_stdin(s)
sm = p.factory.simulation_manager(s)

sm.step(until=lambda lpg: len(lpg.active) > 1)
while len(sm.deadended) == 0:
    sm.drop(stash='active', filter_func=lambda s: s != sm.active[0])
    print(sm.one_active.state.posix.dumps(0))
    sm.step(until=lambda lpg: len(lpg.deadended) > 1 or len(lpg.active) > 1)
