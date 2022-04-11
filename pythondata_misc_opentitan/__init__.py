import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11510"
version_tuple = (0, 0, 11510)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11510")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11384"
data_version_tuple = (0, 0, 11384)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11384")
except ImportError:
    pass
data_git_hash = "6dd70f761132e83bdc956bec993b1744228e6247"
data_git_describe = "v0.0-11384-g6dd70f761"
data_git_msg = """\
commit 6dd70f761132e83bdc956bec993b1744228e6247
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Apr 7 10:59:10 2022 -0700

    [flash_ctrl] Make FIFO level readable by software
    
    see #11882
    
    Also reduce program fifo depth for current flash instance
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
