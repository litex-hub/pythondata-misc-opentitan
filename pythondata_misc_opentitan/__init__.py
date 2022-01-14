import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9546"
version_tuple = (0, 0, 9546)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9546")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9424"
data_version_tuple = (0, 0, 9424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9424")
except ImportError:
    pass
data_git_hash = "ac99d1644ae8ec11b02e211a98281d89f9084fb1"
data_git_describe = "v0.0-9424-gac99d1644"
data_git_msg = """\
commit ac99d1644ae8ec11b02e211a98281d89f9084fb1
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jan 13 20:06:32 2022 +0000

    [spi_device] Connect SRAM arbiter grant signal
    
    SW access port (TL-UL) can handle the grant signal. Other requesters
    from the HW can't handle. The assertion catches the case but the better
    approach is to lower the SW access priority in prim_sram_arbiter and
    also block the requeset when SPI transaction is active.
    
    In this commmit, the SW access has lowest priority. When HW (upload)
    requests, the Sw loses the access.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
