import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15222"
version_tuple = (0, 0, 15222)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15222")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15080"
data_version_tuple = (0, 0, 15080)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15080")
except ImportError:
    pass
data_git_hash = "a84c93ccd75ce172c3ac207d44facb762d2833c2"
data_git_describe = "v0.0-15080-ga84c93ccd7"
data_git_msg = """\
commit a84c93ccd75ce172c3ac207d44facb762d2833c2
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Nov 3 14:00:42 2022 -0700

    [top/dv] Several x-ref updates to the testplan
    
    Also remove testpoints that are no longer required.
    
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
