#import seissolxdmfwriter as sxw
import seissolxdmf as sx
import numpy as np
fn = '/home/ulrich/trash/fl33cpu-fault.xdmf'
# Read data from input file using seissolxdmf
sx = sx.seissolxdmf(fn)
print(sx.ReadNElements())
print(sx.ReadNNodes())
print(sx.ReadNodesPerElement())
geom = sx.ReadGeometry()
