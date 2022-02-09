import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10205"
version_tuple = (0, 0, 10205)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10205")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10081"
data_version_tuple = (0, 0, 10081)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10081")
except ImportError:
    pass
data_git_hash = "ffa395e7ab856be45e0fc759bde6f64efe2eb4c6"
data_git_describe = "v0.0-10081-gffa395e7a"
data_git_msg = """\
commit ffa395e7ab856be45e0fc759bde6f64efe2eb4c6
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Feb 9 20:39:14 2022 +0000

    [usbdev, rtl] Fix auto-generated files
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
