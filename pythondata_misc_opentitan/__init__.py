import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14280"
version_tuple = (0, 0, 14280)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14280")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14138"
data_version_tuple = (0, 0, 14138)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14138")
except ImportError:
    pass
data_git_hash = "4e3eac69d6bd3d17cb106f2507834546ff256f0d"
data_git_describe = "v0.0-14138-g4e3eac69d6"
data_git_msg = """\
commit 4e3eac69d6bd3d17cb106f2507834546ff256f0d
Author: Eli Kim <eli@opentitan.org>
Date:   Fri Sep 16 13:27:56 2022 -0700

    refactor(chip): Remove unused tasks
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
