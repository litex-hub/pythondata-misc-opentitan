import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8287"
version_tuple = (0, 0, 8287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8175"
data_version_tuple = (0, 0, 8175)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8175")
except ImportError:
    pass
data_git_hash = "e2175e2e3538235dc1de4447f6d53cd8fccc8c63"
data_git_describe = "v0.0-8175-ge2175e2e3"
data_git_msg = """\
commit e2175e2e3538235dc1de4447f6d53cd8fccc8c63
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Oct 14 14:03:21 2021 +0100

    [otbn] Pick values for CMD register with large Hamming distance
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
