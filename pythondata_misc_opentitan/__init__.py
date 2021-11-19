import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8770"
version_tuple = (0, 0, 8770)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8770")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8658"
data_version_tuple = (0, 0, 8658)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8658")
except ImportError:
    pass
data_git_hash = "2a78a93ac3226c2ba8343c863023f036eda8f179"
data_git_describe = "v0.0-8658-g2a78a93ac"
data_git_msg = """\
commit 2a78a93ac3226c2ba8343c863023f036eda8f179
Author: Weicai Yang <weicai@google.com>
Date:   Thu Nov 18 15:59:59 2021 -0800

    [dv] Fix intg_err test
    
    This addressed the regression failures in all the intg_err test which is
    due to the update from #9243
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
