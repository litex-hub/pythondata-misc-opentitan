import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5497"
version_tuple = (0, 0, 5497)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5497")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5402"
data_version_tuple = (0, 0, 5402)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5402")
except ImportError:
    pass
data_git_hash = "83d1208879fd37e6c31ee357615bee0508f525b1"
data_git_describe = "v0.0-5402-g83d120887"
data_git_msg = """\
commit 83d1208879fd37e6c31ee357615bee0508f525b1
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 19 17:57:20 2021 +0000

    [doc] Update OpenOCD instructions for Verilator
    
    Adds a link to the OpenOCD installation instructions and removes
    mention of the compliance test as whilst it is still present in OpenOCD
    it is incomplete and unsupported
    (https://github.com/riscv/riscv-openocd/issues/462#issuecomment-606155696)
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
