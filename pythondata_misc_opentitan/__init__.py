import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12930"
version_tuple = (0, 0, 12930)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12930")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12788"
data_version_tuple = (0, 0, 12788)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12788")
except ImportError:
    pass
data_git_hash = "1f7ba3b020414e535637ca066149323d0141ff19"
data_git_describe = "v0.0-12788-g1f7ba3b020"
data_git_msg = """\
commit 1f7ba3b020414e535637ca066149323d0141ff19
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Jul 1 13:38:19 2022 -0700

    [dvsim] Indicate what is currently running
    
    This commit enhances the dvsim status bar to indicate what
    job is currently running, truncated to 30 characters.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
