import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8514"
version_tuple = (0, 0, 8514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8402"
data_version_tuple = (0, 0, 8402)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8402")
except ImportError:
    pass
data_git_hash = "0edab912c4fadd61d76ee5ed13fa8c0d46c4024a"
data_git_describe = "v0.0-8402-g0edab912c"
data_git_msg = """\
commit 0edab912c4fadd61d76ee5ed13fa8c0d46c4024a
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 26 12:54:11 2021 +0100

    [otbn,doc] Document the bus-accessible part of DMEM
    
    This doesn't yet change the implementation, nor does it change DV or
    tooling code.
    
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
