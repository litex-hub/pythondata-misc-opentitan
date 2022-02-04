import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10064"
version_tuple = (0, 0, 10064)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10064")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9940"
data_version_tuple = (0, 0, 9940)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9940")
except ImportError:
    pass
data_git_hash = "edbd0a0a8dc42d82ad6d36928aad0c7e51eac70d"
data_git_describe = "v0.0-9940-gedbd0a0a8"
data_git_msg = """\
commit edbd0a0a8dc42d82ad6d36928aad0c7e51eac70d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Feb 3 15:49:08 2022 -0800

    [foundry/CI] Fix close source OTP smoke test timeout
    
    Close source write takes long simulation time so to avoid timeout, we
    issue less read/write if it is CI check.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
