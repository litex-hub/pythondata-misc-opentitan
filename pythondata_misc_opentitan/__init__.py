import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9484"
version_tuple = (0, 0, 9484)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9484")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9366"
data_version_tuple = (0, 0, 9366)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9366")
except ImportError:
    pass
data_git_hash = "03e6b7e5e60666d1cb9bdfca4f0a58afe279ac8b"
data_git_describe = "v0.0-9366-g03e6b7e5e"
data_git_msg = """\
commit 03e6b7e5e60666d1cb9bdfca4f0a58afe279ac8b
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Thu Dec 23 16:28:06 2021 +0100

    [kmac] made all invalid states of sparse fsm terminal
    
    Signed-off-by: Michael Tempelmeier <michael.tempelmeier@gi-de.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
