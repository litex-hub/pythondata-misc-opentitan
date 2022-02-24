import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10523"
version_tuple = (0, 0, 10523)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10523")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10397"
data_version_tuple = (0, 0, 10397)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10397")
except ImportError:
    pass
data_git_hash = "40201ee8231700e49b089ee04aa453d3208223d1"
data_git_describe = "v0.0-10397-g40201ee82"
data_git_msg = """\
commit 40201ee8231700e49b089ee04aa453d3208223d1
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 17 14:23:39 2022 -0800

    [sram/dv] Update sec_cm testplan
    
    Add details in description and link tests
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
