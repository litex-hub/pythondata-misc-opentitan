import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14174"
version_tuple = (0, 0, 14174)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14174")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14032"
data_version_tuple = (0, 0, 14032)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14032")
except ImportError:
    pass
data_git_hash = "b1cc27a98e2c21dbe93aceca6f1c34e0da852ac7"
data_git_describe = "v0.0-14032-gb1cc27a98e"
data_git_msg = """\
commit b1cc27a98e2c21dbe93aceca6f1c34e0da852ac7
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Sep 13 14:26:06 2022 +0100

    [otbn,dv] Fix OTBN block level tests for xlm
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
