import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10830"
version_tuple = (0, 0, 10830)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10830")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10704"
data_version_tuple = (0, 0, 10704)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10704")
except ImportError:
    pass
data_git_hash = "fc179870ee04daba0275b0920d73c46bf1d207ef"
data_git_describe = "v0.0-10704-gfc179870e"
data_git_msg = """\
commit fc179870ee04daba0275b0920d73c46bf1d207ef
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 9 19:21:19 2022 -0800

    [keymgr] Detect spurious done's from kmac as a fault
    
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
