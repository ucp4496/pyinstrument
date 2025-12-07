from pyinstrument import Profiler
import time

def heavy_profile():
    p = Profiler()
    p.start()
    time.sleep(0.01)
    for _ in range(500):
        sum(range(20))
    p.stop()
    return len(p.output_text())
