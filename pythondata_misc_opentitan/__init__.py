import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5518"
version_tuple = (0, 0, 5518)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5518")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5423"
data_version_tuple = (0, 0, 5423)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5423")
except ImportError:
    pass
data_git_hash = "613d37f0a68ed1943a71e9b10fcf5c0a2d8c0d43"
data_git_describe = "v0.0-5423-g613d37f0a"
data_git_msg = """\
commit 613d37f0a68ed1943a71e9b10fcf5c0a2d8c0d43
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 17 20:22:37 2021 -0700

    [rstmgr] Fix several controllable reset issues
    
    See #5601 and #5602
    
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
