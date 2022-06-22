import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12786"
version_tuple = (0, 0, 12786)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12786")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12644"
data_version_tuple = (0, 0, 12644)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12644")
except ImportError:
    pass
data_git_hash = "7dfc681a138e2eb4773dec309744a823d20ef2fe"
data_git_describe = "v0.0-12644-g7dfc681a13"
data_git_msg = """\
commit 7dfc681a138e2eb4773dec309744a823d20ef2fe
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jun 21 16:21:25 2022 -0700

    [dv,chip,clk_measurements] Streamline testutils
    
    Put all the logic to determine the expected cycle counts in testutils.
    Tighten up ast_clk_outs test by running with calibrated USB clock.
    Fix the dif bit assignment of the clkmgr RECOV_ERR_CODE CSR.
    Modify tests that measure cycle counts for the changes in testutils.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
