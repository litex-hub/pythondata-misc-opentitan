import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5435"
version_tuple = (0, 0, 5435)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5435")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5340"
data_version_tuple = (0, 0, 5340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5340")
except ImportError:
    pass
data_git_hash = "6cc21b3666e2863e80067079ba96f6b5968d4c29"
data_git_describe = "v0.0-5340-g6cc21b366"
data_git_msg = """\
commit 6cc21b3666e2863e80067079ba96f6b5968d4c29
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 11 22:04:55 2021 -0800

    [tlul] Two minor adapter_reg fixes
    
    - return all 1's (similar to error case) on rdata for write transactions
    - correct the data used for integrity generation
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
