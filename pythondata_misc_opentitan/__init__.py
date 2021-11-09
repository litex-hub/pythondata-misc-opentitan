import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8639"
version_tuple = (0, 0, 8639)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8639")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8527"
data_version_tuple = (0, 0, 8527)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8527")
except ImportError:
    pass
data_git_hash = "ac4e5d561cfc8f64e78fe4cf47e79f3cf73403a6"
data_git_describe = "v0.0-8527-gac4e5d561"
data_git_msg = """\
commit ac4e5d561cfc8f64e78fe4cf47e79f3cf73403a6
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Fri Oct 29 12:56:22 2021 +0100

    [doc, sram_ctrl] Fix incorrect table values
    
    In `prim_mubi_pkg.sv` and `multibits.h` `MuBi4True` value is 0xA,
    whilst in the SRAM documentation it was set as 0x5, which corresponds
    to `MuBi4False` of the above.
    
    closes #8917
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
