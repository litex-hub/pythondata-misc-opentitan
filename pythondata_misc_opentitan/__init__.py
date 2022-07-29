import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13335"
version_tuple = (0, 0, 13335)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13335")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13193"
data_version_tuple = (0, 0, 13193)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13193")
except ImportError:
    pass
data_git_hash = "ddf5ef1cf5d3ab92cbb4d35b90fb92750a99bda3"
data_git_describe = "v0.0-13193-gddf5ef1cf5"
data_git_msg = """\
commit ddf5ef1cf5d3ab92cbb4d35b90fb92750a99bda3
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed May 18 18:06:55 2022 +0100

    [otbn] Move to D2S
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
