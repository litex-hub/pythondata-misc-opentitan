import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15321"
version_tuple = (0, 0, 15321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15179"
data_version_tuple = (0, 0, 15179)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15179")
except ImportError:
    pass
data_git_hash = "fb37d77073c4fce4157d5af847bccce0a29dd685"
data_git_describe = "v0.0-15179-gfb37d77073"
data_git_msg = """\
commit fb37d77073c4fce4157d5af847bccce0a29dd685
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 7 13:22:48 2022 -0800

    [top/dv] Fix addresse used for fault triggering.
    
    The current address used ends up being a "bad" out of range address
    that triggers the bus exception handler instead.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
