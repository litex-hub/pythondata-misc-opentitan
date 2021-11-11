import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8685"
version_tuple = (0, 0, 8685)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8685")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8573"
data_version_tuple = (0, 0, 8573)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8573")
except ImportError:
    pass
data_git_hash = "0c9b95ebdd57e1424346a1c8d70b416dba7015e9"
data_git_describe = "v0.0-8573-g0c9b95ebd"
data_git_msg = """\
commit 0c9b95ebdd57e1424346a1c8d70b416dba7015e9
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Nov 10 15:57:11 2021 +0000

    [prim] Add missing include to prim_xilinx_pad_wrapper
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
