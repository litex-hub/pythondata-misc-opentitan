import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5133"
version_tuple = (0, 0, 5133)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5133")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5042"
data_version_tuple = (0, 0, 5042)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5042")
except ImportError:
    pass
data_git_hash = "d2c08a5e0488ef60b8ed7a47cfb840f1b6413863"
data_git_describe = "v0.0-5042-gd2c08a5e0"
data_git_msg = """\
commit d2c08a5e0488ef60b8ed7a47cfb840f1b6413863
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 12 15:39:24 2021 -0800

    [top] Auto generate regfiles
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
