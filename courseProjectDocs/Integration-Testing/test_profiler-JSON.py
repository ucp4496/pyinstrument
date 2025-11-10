from pyinstrument import Profiler
from pyinstrument.renderers.jsonrenderer import JSONRenderer
import json

def test_profiler_json_integration():
    p = Profiler()
    p.start()

    for x in range(1000):
        pass

    session = p.stop()
    renderer = JSONRenderer()
    output = renderer.render(session)

    parsed = json.loads(output)
    assert isinstance(parsed, dict)
