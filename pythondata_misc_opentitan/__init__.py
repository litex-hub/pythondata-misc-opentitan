import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5308"
version_tuple = (0, 0, 5308)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5308")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5213"
data_version_tuple = (0, 0, 5213)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5213")
except ImportError:
    pass
data_git_hash = "72cb99c3ab0a3e9798dfd62db3193fc5219e1e8c"
data_git_describe = "v0.0-5213-g72cb99c3a"
data_git_msg = """\
commit 72cb99c3ab0a3e9798dfd62db3193fc5219e1e8c
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Mar 8 15:58:44 2021 -0800

    [top] Change edn hook-up
    
    see #5487
    
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
