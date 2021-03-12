import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5367"
version_tuple = (0, 0, 5367)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5367")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5272"
data_version_tuple = (0, 0, 5272)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5272")
except ImportError:
    pass
data_git_hash = "1ae03937f0bb4b146bb6e736bccb4821bfda556b"
data_git_describe = "v0.0-5272-g1ae03937f"
data_git_msg = """\
commit 1ae03937f0bb4b146bb6e736bccb4821bfda556b
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Fri Jan 29 10:54:42 2021 +0000

    [prim/fifo_async] Add assertions on pointers
    
    Check that pointers are correctly gray coded by checking for one bit
    transitions.
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
