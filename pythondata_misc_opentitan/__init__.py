import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5360"
version_tuple = (0, 0, 5360)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5360")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5265"
data_version_tuple = (0, 0, 5265)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5265")
except ImportError:
    pass
data_git_hash = "4d8438cfc7769fbc4a5c1ea7f25e5c306c8e01b3"
data_git_describe = "v0.0-5265-g4d8438cfc"
data_git_msg = """\
commit 4d8438cfc7769fbc4a5c1ea7f25e5c306c8e01b3
Author: Matute <maturana@google.com>
Date:   Thu Mar 11 14:32:08 2021 -0800

    [doc/dv] Fixes typos and formatting changes.
    
    Signed-off-by: Matute <maturana@google.com>

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
