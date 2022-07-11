import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13012"
version_tuple = (0, 0, 13012)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13012")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12870"
data_version_tuple = (0, 0, 12870)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12870")
except ImportError:
    pass
data_git_hash = "564f8fe63ef37bbed2ce91c0485d9bebdd9a8196"
data_git_describe = "v0.0-12870-g564f8fe63e"
data_git_msg = """\
commit 564f8fe63ef37bbed2ce91c0485d9bebdd9a8196
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu May 26 14:50:17 2022 -0700

    chore(gpio): GPIO to D3 for v1.1
    
    This commit moves GPIO HWIP to D3 for version 1.1
    
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
