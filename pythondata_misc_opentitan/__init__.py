import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8339"
version_tuple = (0, 0, 8339)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8339")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8227"
data_version_tuple = (0, 0, 8227)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8227")
except ImportError:
    pass
data_git_hash = "102a025741e5371077259cd4052aebd31f0e4074"
data_git_describe = "v0.0-8227-g102a02574"
data_git_msg = """\
commit 102a025741e5371077259cd4052aebd31f0e4074
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 15 14:23:43 2021 +0100

    [sw] Add ECDSA/P-256 sign wrapper
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
