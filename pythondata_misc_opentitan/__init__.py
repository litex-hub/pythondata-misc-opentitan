import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10882"
version_tuple = (0, 0, 10882)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10882")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10756"
data_version_tuple = (0, 0, 10756)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10756")
except ImportError:
    pass
data_git_hash = "74606dcd1d0f0d175d651b8e5e1046329f3d4a1c"
data_git_describe = "v0.0-10756-g74606dcd1"
data_git_msg = """\
commit 74606dcd1d0f0d175d651b8e5e1046329f3d4a1c
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 11 23:21:51 2022 +0000

    [otbn,dv] Allow traced changes from ISS when no operation is running
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
