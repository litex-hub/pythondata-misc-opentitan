import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10712"
version_tuple = (0, 0, 10712)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10712")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10586"
data_version_tuple = (0, 0, 10586)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10586")
except ImportError:
    pass
data_git_hash = "819c80665ca1c7e586a7598c5bc5097060d36cd7"
data_git_describe = "v0.0-10586-g819c80665"
data_git_msg = """\
commit 819c80665ca1c7e586a7598c5bc5097060d36cd7
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 3 16:36:52 2022 +0000

    [flash_ctrl] Use an unsigned type for ExecEn
    
    This 32-bit value has its top bit set, so assigning it to an "int"
    causes sign overflow warnings.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
