import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8851"
version_tuple = (0, 0, 8851)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8851")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8739"
data_version_tuple = (0, 0, 8739)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8739")
except ImportError:
    pass
data_git_hash = "36cbccbefa66530bfb94d219b1749e3b31f8331d"
data_git_describe = "v0.0-8739-g36cbccbef"
data_git_msg = """\
commit 36cbccbefa66530bfb94d219b1749e3b31f8331d
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 23 13:35:12 2021 -0800

    [top] Fix pinmux reset assignment
    
    Pinmux was assigned the wrong root reset and as a result was
    still held in reset with the strap signal was received.
    
    This means pinmux does not actually perform the strapping function
    since all its logic is held in reset.
    
    Fixes #9365
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
