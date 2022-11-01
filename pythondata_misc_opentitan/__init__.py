import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15084"
version_tuple = (0, 0, 15084)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15084")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14942"
data_version_tuple = (0, 0, 14942)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14942")
except ImportError:
    pass
data_git_hash = "497b88290491f8655aaca873c4cbc6ab4d8df423"
data_git_describe = "v0.0-14942-g497b882904"
data_git_msg = """\
commit 497b88290491f8655aaca873c4cbc6ab4d8df423
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Oct 31 14:21:08 2022 -0700

    [rust] Update serde-annotate
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
