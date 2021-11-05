import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8603"
version_tuple = (0, 0, 8603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8491"
data_version_tuple = (0, 0, 8491)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8491")
except ImportError:
    pass
data_git_hash = "ba3f6f9f1cebc380d85ceffe02215aa36db3238e"
data_git_describe = "v0.0-8491-gba3f6f9f1"
data_git_msg = """\
commit ba3f6f9f1cebc380d85ceffe02215aa36db3238e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Nov 3 15:41:12 2021 -0400

    [sw/silicon_creator] Simplify flash_ctrl_prog loop
    
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
