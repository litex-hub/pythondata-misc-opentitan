import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8850"
version_tuple = (0, 0, 8850)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8850")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8738"
data_version_tuple = (0, 0, 8738)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8738")
except ImportError:
    pass
data_git_hash = "42406d3b9be7659c31f07f1f9fbaaa7b2726fd7c"
data_git_describe = "v0.0-8738-g42406d3b9"
data_git_msg = """\
commit 42406d3b9be7659c31f07f1f9fbaaa7b2726fd7c
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 23 11:04:46 2021 -0800

    [flash_ctrl] Officially move flash_ctrl to D2.
    
    - Previous PR forgot to change the actual design stage
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
