import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13162"
version_tuple = (0, 0, 13162)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13162")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13020"
data_version_tuple = (0, 0, 13020)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13020")
except ImportError:
    pass
data_git_hash = "936431c28847c7f740daca6882fa8975f2f9e8ad"
data_git_describe = "v0.0-13020-g936431c288"
data_git_msg = """\
commit 936431c28847c7f740daca6882fa8975f2f9e8ad
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Jul 15 15:14:49 2022 -0700

    fix(rdc): typo
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
