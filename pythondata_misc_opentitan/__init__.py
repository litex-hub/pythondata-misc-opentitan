import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13233"
version_tuple = (0, 0, 13233)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13233")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13091"
data_version_tuple = (0, 0, 13091)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13091")
except ImportError:
    pass
data_git_hash = "afecb3eea7dfa78d83c6c7873df5d8678ea7f4dd"
data_git_describe = "v0.0-13091-gafecb3eea7"
data_git_msg = """\
commit afecb3eea7dfa78d83c6c7873df5d8678ea7f4dd
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jul 20 16:37:32 2022 -0700

    [dv/sw] Minor correction to flash_ctrl_testutil
    
    - see #13773
    
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
