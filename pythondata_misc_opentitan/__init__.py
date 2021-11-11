import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8673"
version_tuple = (0, 0, 8673)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8673")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8561"
data_version_tuple = (0, 0, 8561)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8561")
except ImportError:
    pass
data_git_hash = "928a45f94807a9ccdc3fe01a08e7cc808ff1e2e5"
data_git_describe = "v0.0-8561-g928a45f94"
data_git_msg = """\
commit 928a45f94807a9ccdc3fe01a08e7cc808ff1e2e5
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Nov 8 14:32:13 2021 -0500

    [sw/silicon_creator] Add individual error codes for data and info read, write, and erase operations
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
