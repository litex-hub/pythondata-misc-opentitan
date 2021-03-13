import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5375"
version_tuple = (0, 0, 5375)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5375")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5280"
data_version_tuple = (0, 0, 5280)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5280")
except ImportError:
    pass
data_git_hash = "8e56cfc0688e07bac071b46126b2317e202e6bd2"
data_git_describe = "v0.0-5280-g8e56cfc06"
data_git_msg = """\
commit 8e56cfc0688e07bac071b46126b2317e202e6bd2
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Mar 11 15:31:10 2021 -0800

    [otp_ctrl] Disable assertion due to esc_en failure
    
    This PR disables an assertion from `prim_arbiter_tree`. The assertion
    tries to check if req should stay high until grant signal is set.
    However, it does not work if `lc_escalate_en` signal is set.
    Please feel free to discard this PR if you prefer some other ways to fix
    it.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
