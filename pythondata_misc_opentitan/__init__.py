import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8419"
version_tuple = (0, 0, 8419)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8419")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8307"
data_version_tuple = (0, 0, 8307)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8307")
except ImportError:
    pass
data_git_hash = "3e25bcd12336f774069a2b2d037d864da007c3cc"
data_git_describe = "v0.0-8307-g3e25bcd12"
data_git_msg = """\
commit 3e25bcd12336f774069a2b2d037d864da007c3cc
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Oct 25 12:05:36 2021 +0100

    [otbn] Suppress bad_insn_addr error on other software errors
    
    Fixes #8645
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
