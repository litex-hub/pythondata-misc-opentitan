import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5515"
version_tuple = (0, 0, 5515)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5515")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5420"
data_version_tuple = (0, 0, 5420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5420")
except ImportError:
    pass
data_git_hash = "4c2b5f4338a93c7b48d33e48fb75478ee558772a"
data_git_describe = "v0.0-5420-g4c2b5f433"
data_git_msg = """\
commit 4c2b5f4338a93c7b48d33e48fb75478ee558772a
Author: Weicai Yang <weicai@google.com>
Date:   Fri Mar 19 14:25:13 2021 -0700

    [dv] Update driver to process item at active edge for 1st item
    
    Driver should process items at active edge. For 1st item, we didn't wait
    for clock edge
    
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
