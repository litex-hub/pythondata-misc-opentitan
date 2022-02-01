import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9944"
version_tuple = (0, 0, 9944)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9944")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9820"
data_version_tuple = (0, 0, 9820)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9820")
except ImportError:
    pass
data_git_hash = "0e847a6eab9830fa696822b449b54e01514768bb"
data_git_describe = "v0.0-9820-g0e847a6ea"
data_git_msg = """\
commit 0e847a6eab9830fa696822b449b54e01514768bb
Author: Eitan Shapira <eitanshapira89@gmail.com>
Date:   Thu Jan 27 15:48:32 2022 +0200

    [flash_ctrl/dv] Tiny change in tb power_down driving
    
    Signed-off-by: Eitan Shapira <eitanshapira89@gmail.com>

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
