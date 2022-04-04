import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11336"
version_tuple = (0, 0, 11336)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11336")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11210"
data_version_tuple = (0, 0, 11210)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11210")
except ImportError:
    pass
data_git_hash = "5852b71c5c0d70709699b4a18fc6de921bc34836"
data_git_describe = "v0.0-11210-g5852b71c5"
data_git_msg = """\
commit 5852b71c5c0d70709699b4a18fc6de921bc34836
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Apr 1 16:06:15 2022 -0700

    [sensor_ctrl] move to D2
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
