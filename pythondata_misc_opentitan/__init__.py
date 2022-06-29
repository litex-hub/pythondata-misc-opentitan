import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12887"
version_tuple = (0, 0, 12887)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12887")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12745"
data_version_tuple = (0, 0, 12745)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12745")
except ImportError:
    pass
data_git_hash = "6e3829326c4f49ca43a47a554b96f0d0ba49d679"
data_git_describe = "v0.0-12745-g6e3829326c"
data_git_msg = """\
commit 6e3829326c4f49ca43a47a554b96f0d0ba49d679
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Jun 28 14:17:32 2022 -0700

    [dv/chip] Fix regression error on lc_ctrl_transition test
    
    This PR fixes the regression failure on lc_ctrl_transition_test where
    the testbench expects an external clock switch (PR #13141). However, the
    default setting for lc_ctrl_transition test is to use internal clock. So
    I fix it by adding a CSR read to check if the ctrl register is
    configured to use internal or external clock.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
