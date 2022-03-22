import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11022"
version_tuple = (0, 0, 11022)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11022")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10896"
data_version_tuple = (0, 0, 10896)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10896")
except ImportError:
    pass
data_git_hash = "ee05909e2a5a39be116484e537f62e35e5ae7573"
data_git_describe = "v0.0-10896-gee05909e2"
data_git_msg = """\
commit ee05909e2a5a39be116484e537f62e35e5ae7573
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Mar 18 13:22:10 2022 -0700

    [flah_ctrl] Fix alert indexing
    
    - standard fatal alerts are at position 1 instead of 0
    
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
