import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12853"
version_tuple = (0, 0, 12853)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12853")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12711"
data_version_tuple = (0, 0, 12711)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12711")
except ImportError:
    pass
data_git_hash = "96bf7e38c1405e9ea3c213b66d2470dc432c6461"
data_git_describe = "v0.0-12711-g96bf7e38c1"
data_git_msg = """\
commit 96bf7e38c1405e9ea3c213b66d2470dc432c6461
Author: Dharanendra Kumar <dharanendra.kumar@ensilica.com>
Date:   Fri Jun 24 18:04:04 2022 +0100

    [PWM/DV] Updates For VCS Run
    
      Updated for VCS Run
      Changed some of the code to support VCS
    
    Signed-off-by: Dharanendra Kumar <dharanendra.kumar@ensilica.com>

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
