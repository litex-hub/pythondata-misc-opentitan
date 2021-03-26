import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5601"
version_tuple = (0, 0, 5601)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5601")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5506"
data_version_tuple = (0, 0, 5506)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5506")
except ImportError:
    pass
data_git_hash = "fa60a60581561cfd5f616f95ee8af3ec84ce30d2"
data_git_describe = "v0.0-5506-gfa60a6058"
data_git_msg = """\
commit fa60a60581561cfd5f616f95ee8af3ec84ce30d2
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 23 14:29:40 2021 -0700

    [top, clkmgr] Add external clock switch support
    
    Address #5566
    
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
