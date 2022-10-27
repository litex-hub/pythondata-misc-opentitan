import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14976"
version_tuple = (0, 0, 14976)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14976")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14834"
data_version_tuple = (0, 0, 14834)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14834")
except ImportError:
    pass
data_git_hash = "517edba6abe68b919742d7c1d0a687361b9fe32b"
data_git_describe = "v0.0-14834-g517edba6ab"
data_git_msg = """\
commit 517edba6abe68b919742d7c1d0a687361b9fe32b
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Oct 26 11:52:10 2022 -0700

    [top/dv] Address review comments
    
    Address comments from #15297
    
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
