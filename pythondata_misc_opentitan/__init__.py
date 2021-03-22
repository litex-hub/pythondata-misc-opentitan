import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5512"
version_tuple = (0, 0, 5512)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5512")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5417"
data_version_tuple = (0, 0, 5417)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5417")
except ImportError:
    pass
data_git_hash = "0c0ece5e19d43c90f4dda64373915cff06394ed7"
data_git_describe = "v0.0-5417-g0c0ece5e1"
data_git_msg = """\
commit 0c0ece5e19d43c90f4dda64373915cff06394ed7
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Mon Mar 22 14:35:57 2021 +0000

    [dif] Add missing `extern "C"` declarations.
    
    DIFs are implemented in C and so the API requires C linkage in C++.
    The current template includes the necessary `extern "C"`
    declaration but the hmac and usbdev header files did not have it.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
