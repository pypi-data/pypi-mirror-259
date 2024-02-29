import seissolxdmfwriter as sxw
import seissolxdmf as sx
import numpy as np
fn = '/home/ulrich/trash/fl33cpu-fault.xdmf'
# Read data from input file using seissolxdmf
sx = sx.seissolxdmf(fn)
geom = sx.ReadGeometry()
connect = sx.ReadConnect()
dt = sx.ReadTimeStep()
SRs = sx.ReadData('SRs')
SRd = sx.ReadData('SRd')
SR = np.sqrt(SRs**2 + SRd**2)
partition = sx.Read1dData("partition", sx.nElements, isInt=True)
# Write the 0,4 and 8th times steps of array SRs and SR in SRtest-fault.xdmf/SRtest-fault.h5
#sxw.write_seissol_output('test-fault', geom, connect, ['SRs', 'SR'], [SRs, SR], dt, [0, 4, 5], True, False)


dictTime = {dt * i: i for i in [3,4]}
#dictTime = {}
#sxw.write('test-fault', geom, connect, {'SRs': SRs, 'SR':SR, "fault-tag":faulttag}, dictTime, True, 'hdf5', 4)
#sxw.write('test-fault-raw', geom, connect, {'SRs': SRs, 'SR':SR, "fault-tag":faulttag}, dictTime, True, 'raw', 4)
#sxw.write('test-fault8', geom, connect, {'SRs': SRs, 'SR':SR, "fault-tag":faulttag}, dictTime, False, 'hdf5', 4)
#sxw.write('test-fault-raw8', geom, connect, {'SRs': SRs, 'SR':SR, "fault-tag":faulttag}, dictTime, False, 'raw', 4)
"""
sxw.write_from_seissolxdmf(
    'test-fault-sx',
    fn,
    ['SRs', 'SRd','fault-tag', 'partition'],
    [3,4],
    reduce_precision=False,
    backend="hdf5",
    compression_level=4,
)
"""
print(partition)
print(partition.shape)
ids = np.where(partition == 1)[1]
print(ids.shape)
print(partition.shape)
sxw.write_from_seissol_output(
    'test-fault-raw-sx',
    fn,
    ['SRs', 'SRd','fault-tag', 'partition'],
    [3,4],
    reduce_precision=True,
    backend="raw",
    compression_level=4,
    filtered_cells = ids
)

sxw.write_seissol_output(
    'cali',
    geom,
    connect,
    ['SRs', 'SRd'],
    [SRs, SRd],
    dt,
    [3,4],
    reduce_precision=False,
    backend="hdf5",
)


