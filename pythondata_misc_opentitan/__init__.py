import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9000"
version_tuple = (0, 0, 9000)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9000")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8888"
data_version_tuple = (0, 0, 8888)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8888")
except ImportError:
    pass
data_git_hash = "ad7f46d67644239ab81d6572d87554e5d3eacc40"
data_git_describe = "v0.0-8888-gad7f46d67"
data_git_msg = """\
commit ad7f46d67644239ab81d6572d87554e5d3eacc40
Author: Alexander Williams <awill@google.com>
Date:   Thu Sep 30 09:15:08 2021 -0700

    [doc] Set up PLL when getting started with CW310
    
    If the --set-pll-defaults argument is missing, the new user will have
    no clock.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
