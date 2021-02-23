import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5110"
version_tuple = (0, 0, 5110)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5110")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5019"
data_version_tuple = (0, 0, 5019)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5019")
except ImportError:
    pass
data_git_hash = "40c21eb946682b665112223d2b299df3c9385037"
data_git_describe = "v0.0-5019-g40c21eb94"
data_git_msg = """\
commit 40c21eb946682b665112223d2b299df3c9385037
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Feb 22 15:58:34 2021 -0800

    [top] Correct top level parameters for sram execution
    
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
