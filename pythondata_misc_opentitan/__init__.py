import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14323"
version_tuple = (0, 0, 14323)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14323")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14181"
data_version_tuple = (0, 0, 14181)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14181")
except ImportError:
    pass
data_git_hash = "93dc5862ed78e85df8205dc252a8eee9696e5d1b"
data_git_describe = "v0.0-14181-g93dc5862ed"
data_git_msg = """\
commit 93dc5862ed78e85df8205dc252a8eee9696e5d1b
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Sep 20 12:31:07 2022 -0700

    [top/dv] Increase reseed for wdog sleep pause
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
