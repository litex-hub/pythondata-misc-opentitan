import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12370"
version_tuple = (0, 0, 12370)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12370")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12230"
data_version_tuple = (0, 0, 12230)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12230")
except ImportError:
    pass
data_git_hash = "c938c1833f7477e204f07e665584c87396ac3265"
data_git_describe = "v0.0-12230-gc938c1833"
data_git_msg = """\
commit c938c1833f7477e204f07e665584c87396ac3265
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu May 26 17:51:39 2022 -0400

    Remove sw/host/vendor directory
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
