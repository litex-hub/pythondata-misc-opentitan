import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8691"
version_tuple = (0, 0, 8691)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8691")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8579"
data_version_tuple = (0, 0, 8579)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8579")
except ImportError:
    pass
data_git_hash = "cdcb4e08f78703de0b2f7753040042071772c634"
data_git_describe = "v0.0-8579-gcdcb4e08f"
data_git_msg = """\
commit cdcb4e08f78703de0b2f7753040042071772c634
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Nov 11 10:01:23 2021 -0800

    [util] Add missing file
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
