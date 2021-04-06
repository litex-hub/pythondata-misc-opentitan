import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5734"
version_tuple = (0, 0, 5734)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5734")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5639"
data_version_tuple = (0, 0, 5639)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5639")
except ImportError:
    pass
data_git_hash = "9bff8eae22c7aef750394cc36b76f3c696025e38"
data_git_describe = "v0.0-5639-g9bff8eae2"
data_git_msg = """\
commit 9bff8eae22c7aef750394cc36b76f3c696025e38
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Fri Apr 2 15:14:04 2021 -0700

    [dvsim] Fix remaining comments  from #5876
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
