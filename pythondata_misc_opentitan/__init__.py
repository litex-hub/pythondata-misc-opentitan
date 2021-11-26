import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8869"
version_tuple = (0, 0, 8869)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8869")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8757"
data_version_tuple = (0, 0, 8757)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8757")
except ImportError:
    pass
data_git_hash = "4ca1caa9823a5009900de7f6845a2b543eab2f1b"
data_git_describe = "v0.0-8757-g4ca1caa98"
data_git_msg = """\
commit 4ca1caa9823a5009900de7f6845a2b543eab2f1b
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Nov 23 10:56:01 2021 +0000

    [otbn, rtl] Implement key sideload
    
    Fixes #8692
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
