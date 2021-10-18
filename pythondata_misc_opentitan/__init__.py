import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8313"
version_tuple = (0, 0, 8313)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8313")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8201"
data_version_tuple = (0, 0, 8201)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8201")
except ImportError:
    pass
data_git_hash = "59ce35158fe4ea004c7c5cc355b41c3fb12b7b1f"
data_git_describe = "v0.0-8201-g59ce35158"
data_git_msg = """\
commit 59ce35158fe4ea004c7c5cc355b41c3fb12b7b1f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Sep 29 12:05:18 2021 +0100

    [otbn,dv] Allow the testbench to trigger IMEM errors in ISS
    
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
