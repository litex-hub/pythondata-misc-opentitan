import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9857"
version_tuple = (0, 0, 9857)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9857")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9733"
data_version_tuple = (0, 0, 9733)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9733")
except ImportError:
    pass
data_git_hash = "b8141a041a6e1f906cbbdfd538d164695b5bca91"
data_git_describe = "v0.0-9733-gb8141a041"
data_git_msg = """\
commit b8141a041a6e1f906cbbdfd538d164695b5bca91
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Jan 18 12:15:01 2022 +0000

    [aon_timer,dv] V1 Signoff
    
    All action items from V1 review have been finished and PRs have been merged.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
