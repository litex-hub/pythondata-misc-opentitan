import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5349"
version_tuple = (0, 0, 5349)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5349")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5254"
data_version_tuple = (0, 0, 5254)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5254")
except ImportError:
    pass
data_git_hash = "4abf56b97dcfef7f74883fad73012a285983ebc1"
data_git_describe = "v0.0-5254-g4abf56b97"
data_git_msg = """\
commit 4abf56b97dcfef7f74883fad73012a285983ebc1
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Thu Mar 11 14:17:30 2021 +0000

    [aon_timer/lint] Minor lint fixes
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

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
