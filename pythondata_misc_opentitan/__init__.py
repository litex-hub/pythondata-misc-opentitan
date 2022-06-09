import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12583"
version_tuple = (0, 0, 12583)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12583")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12441"
data_version_tuple = (0, 0, 12441)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12441")
except ImportError:
    pass
data_git_hash = "9350b8bea2bbb542417cafe86bc6edfc69cc8b88"
data_git_describe = "v0.0-12441-g9350b8bea"
data_git_msg = """\
commit 9350b8bea2bbb542417cafe86bc6edfc69cc8b88
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Jun 1 15:47:19 2022 +0100

    [rtl] Combine two case statements for each WDATA
    
    Found this one while looking at open issues. Combines two case
    statements for a single select signal (both for BN and Base).
    
    Fixes #12417
    
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
