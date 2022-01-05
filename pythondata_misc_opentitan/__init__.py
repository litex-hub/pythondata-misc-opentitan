import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9342"
version_tuple = (0, 0, 9342)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9342")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9225"
data_version_tuple = (0, 0, 9225)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9225")
except ImportError:
    pass
data_git_hash = "73a8c733d890bb9769ac354524e3b07af995aabd"
data_git_describe = "v0.0-9225-g73a8c733d"
data_git_msg = """\
commit 73a8c733d890bb9769ac354524e3b07af995aabd
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jan 4 15:52:20 2022 -0800

    [dv/tools] Fix alert ping exclusion
    
    Fix alert ping exclusion only apply to DUT level but not
    prim_alert_sender level.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
