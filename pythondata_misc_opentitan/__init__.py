import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5795"
version_tuple = (0, 0, 5795)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5795")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5700"
data_version_tuple = (0, 0, 5700)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5700")
except ImportError:
    pass
data_git_hash = "f479b9e782c4ecab04b08ce2c9081809129524b2"
data_git_describe = "v0.0-5700-gf479b9e78"
data_git_msg = """\
commit f479b9e782c4ecab04b08ce2c9081809129524b2
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Apr 8 16:03:11 2021 -0700

    [dvsim] Scratch root default to $REPO_TOP/scratch
    
    Use $REPO_TOP/scratch rather than CWD/scratch as the default scratch
    area.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
