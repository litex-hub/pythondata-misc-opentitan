import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14304"
version_tuple = (0, 0, 14304)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14304")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14162"
data_version_tuple = (0, 0, 14162)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14162")
except ImportError:
    pass
data_git_hash = "97ca83996d00a1865f60f8dc0604939d610110d2"
data_git_describe = "v0.0-14162-g97ca83996d"
data_git_msg = """\
commit 97ca83996d00a1865f60f8dc0604939d610110d2
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Sep 19 15:55:06 2022 -0700

    [dv/kmac] Add more coverage sampling points
    
    This PR fixes three empty fcov bins:
    1). Cmd_process_cg: this samples when command process is issued, what is
      the internal state. I created an interface to probe and sample it.
    2). Msgfifo_level_cg: add sampling in scb.
    3). Sha3_status_cg: add sampling in scb.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
