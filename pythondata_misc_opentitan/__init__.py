import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5824"
version_tuple = (0, 0, 5824)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5824")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5729"
data_version_tuple = (0, 0, 5729)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5729")
except ImportError:
    pass
data_git_hash = "6925c6f6d2d389f89751c58a574dd83c9150cf58"
data_git_describe = "v0.0-5729-g6925c6f6d"
data_git_msg = """\
commit 6925c6f6d2d389f89751c58a574dd83c9150cf58
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Apr 9 17:19:27 2021 -0700

    [top] Connect raw pad outputs to ast
    
    - pad2ast
    - external clock
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
