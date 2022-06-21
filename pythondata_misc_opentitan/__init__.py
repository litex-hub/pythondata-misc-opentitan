import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12763"
version_tuple = (0, 0, 12763)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12763")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12621"
data_version_tuple = (0, 0, 12621)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12621")
except ImportError:
    pass
data_git_hash = "146a13315d82a86f9fe587cefa19d8c360dfe98b"
data_git_describe = "v0.0-12621-g146a13315d"
data_git_msg = """\
commit 146a13315d82a86f9fe587cefa19d8c360dfe98b
Author: Alexander Williams <awill@google.com>
Date:   Tue Jun 21 08:24:29 2022 -0700

    [pinmux/dif] Fix check for output selection arg
    
    There are three fixed values (0, 1, Z) for the output mux, not just two.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
