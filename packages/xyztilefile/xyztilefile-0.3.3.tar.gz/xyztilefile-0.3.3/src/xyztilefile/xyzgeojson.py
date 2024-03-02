
import geojson
from shapely.geometry import shape
from .xyzgeneric import *

# Default functions for loading and saving files
_loadfunc = lambda byteio: geojson.loads(byteio.read())

_savefunc = lambda filename, val : print(geojson.dumps(val), file=open(filename,"w"))

class XYZGeoJson(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)

class XYZHttpGeoJson(XYZHttpGeneric):
    def __init__(self, base, loadfunc=_loadfunc, **kwargs):
        super().__init__(base, loadfunc=_loadfunc, **kwargs)


# {"type string from the extension" : Class}
xyztiletype = {"geojson":XYZGeoJson}
xyzhttptype = {"geojson":XYZHttpGeoJson}
