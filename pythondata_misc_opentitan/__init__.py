import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12278"
version_tuple = (0, 0, 12278)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12278")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12150"
data_version_tuple = (0, 0, 12150)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12150")
except ImportError:
    pass
data_git_hash = "bf25d8b4160c6a888933d3a224bac79851537a31"
data_git_describe = "v0.0-12150-gbf25d8b41"
data_git_msg = """\
commit bf25d8b4160c6a888933d3a224bac79851537a31
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Jan 31 15:46:22 2022 +0000

    [otbn] Clean up OTBN information-flow analysis scripts.
    
    Linting/formatting/general cleanup after recent changes to support
    reasoning about cycles.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
