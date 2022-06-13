import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12657"
version_tuple = (0, 0, 12657)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12657")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12515"
data_version_tuple = (0, 0, 12515)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12515")
except ImportError:
    pass
data_git_hash = "5c33c1ab7ecd1ecf824549e3d49c9665d93cc970"
data_git_describe = "v0.0-12515-g5c33c1ab7"
data_git_msg = """\
commit 5c33c1ab7ecd1ecf824549e3d49c9665d93cc970
Author: Eitan Shapira <eitanshapira89@gmail.com>
Date:   Thu Jun 9 14:20:48 2022 +0300

    [flash_ctrl/tl/dv] Add timeout argument to tl_access methods
    
    Signed-off-by: Eitan Shapira <eitanshapira89@gmail.com>

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
