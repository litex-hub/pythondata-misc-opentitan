import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5075"
version_tuple = (0, 0, 5075)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5075")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4984"
data_version_tuple = (0, 0, 4984)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4984")
except ImportError:
    pass
data_git_hash = "7a0289c6eab343d266dfead12f52ac51c4e66aa6"
data_git_describe = "v0.0-4984-g7a0289c6e"
data_git_msg = """\
commit 7a0289c6eab343d266dfead12f52ac51c4e66aa6
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Feb 19 16:33:44 2021 -0800

    [top] Minor lint fixes
    
    - tie off undriven input due to #5260
    - tie off unused clocks / resets in scanmode muxing
    
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
