import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10916"
version_tuple = (0, 0, 10916)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10916")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10790"
data_version_tuple = (0, 0, 10790)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10790")
except ImportError:
    pass
data_git_hash = "7c2486520585a8aad6d7c96ccde811540c206ed6"
data_git_describe = "v0.0-10790-g7c2486520"
data_git_msg = """\
commit 7c2486520585a8aad6d7c96ccde811540c206ed6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 10 14:32:44 2022 +0000

    [otbn,dv] Still print final instruction on escalation when running
    
    We run on_lc_escalation() earlier in the cycle than step(), but we
    want to make sure that we still generate a trace item for executing an
    instruction on that cycle (even though it will be cancelled).
    
    This commit adds explicit "pending error bits" to the state to make
    that possible.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
