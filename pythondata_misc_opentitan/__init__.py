import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13047"
version_tuple = (0, 0, 13047)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13047")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12905"
data_version_tuple = (0, 0, 12905)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12905")
except ImportError:
    pass
data_git_hash = "0365a3d0b4859c1898a6a2ec133f4fb3691a8874"
data_git_describe = "v0.0-12905-g0365a3d0b4"
data_git_msg = """\
commit 0365a3d0b4859c1898a6a2ec133f4fb3691a8874
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Jul 11 17:21:53 2022 -0700

    [dif/entropy_src] add health test configuration DIFs
    
    This adds DIFs to configure the various health tests and adds a missing
    health test (the repetition symbol count).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
