import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11201"
version_tuple = (0, 0, 11201)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11201")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11075"
data_version_tuple = (0, 0, 11075)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11075")
except ImportError:
    pass
data_git_hash = "65472db50ce42debe517557dde8f2d30baeaf275"
data_git_describe = "v0.0-11075-g65472db50"
data_git_msg = """\
commit 65472db50ce42debe517557dde8f2d30baeaf275
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 22 15:48:28 2022 -0700

    [flash_ctrl] more error clarification and updates
    
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
