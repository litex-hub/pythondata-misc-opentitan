import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11108"
version_tuple = (0, 0, 11108)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11108")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10982"
data_version_tuple = (0, 0, 10982)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10982")
except ImportError:
    pass
data_git_hash = "24b84fd02934dd395bff13cb412280dca1c6c59a"
data_git_describe = "v0.0-10982-g24b84fd02"
data_git_msg = """\
commit 24b84fd02934dd395bff13cb412280dca1c6c59a
Author: Weicai Yang <weicai@google.com>
Date:   Wed Mar 23 16:07:50 2022 -0700

    [chip dv] Fix uart unexpected watermark interrupt
    
    When RX watermark fires, read the data, but if remaining items are less
    than 16, RX watermark won't fire. In that case, changed to keep reading
    until all items are received.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
