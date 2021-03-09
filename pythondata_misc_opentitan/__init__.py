import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5312"
version_tuple = (0, 0, 5312)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5312")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5217"
data_version_tuple = (0, 0, 5217)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5217")
except ImportError:
    pass
data_git_hash = "046a56b31a495d7fe461029fa494e3e509903dba"
data_git_describe = "v0.0-5217-g046a56b31"
data_git_msg = """\
commit 046a56b31a495d7fe461029fa494e3e509903dba
Author: Weicai Yang <weicai@google.com>
Date:   Thu Nov 12 13:25:04 2020 -0800

    [uart/dv] Update uart baud rate and add coverage
    
    Address #3599
    Signed-off-by: Weicai Yang <weicai@google.com>

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
