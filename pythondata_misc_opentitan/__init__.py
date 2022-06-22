import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12793"
version_tuple = (0, 0, 12793)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12793")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12651"
data_version_tuple = (0, 0, 12651)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12651")
except ImportError:
    pass
data_git_hash = "4f93cd7465c9ffa1491cd42041c6dbff62a7fd8c"
data_git_describe = "v0.0-12651-g4f93cd7465"
data_git_msg = """\
commit 4f93cd7465c9ffa1491cd42041c6dbff62a7fd8c
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jun 21 16:46:45 2022 -0700

    [top] Update jitter enable
    
    - backdoor load otp value based on jitter_en arg
    - also add default values for jitter_en in the otp hjsons
    
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
