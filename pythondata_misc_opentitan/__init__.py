import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5713"
version_tuple = (0, 0, 5713)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5713")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5618"
data_version_tuple = (0, 0, 5618)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5618")
except ImportError:
    pass
data_git_hash = "b02ea11fd3a8845b9ff5ab2d892ae85b8eba7774"
data_git_describe = "v0.0-5618-gb02ea11fd"
data_git_msg = """\
commit b02ea11fd3a8845b9ff5ab2d892ae85b8eba7774
Author: Weicai Yang <weicai@google.com>
Date:   Mon Mar 29 16:40:06 2021 -0700

    [dv] Document how to reproduce CI (Private) failure
    
    related to #5786
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
