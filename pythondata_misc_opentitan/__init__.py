import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14294"
version_tuple = (0, 0, 14294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14152"
data_version_tuple = (0, 0, 14152)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14152")
except ImportError:
    pass
data_git_hash = "318a5af53ee41d4030ab6a4b3a81f2402ec62e77"
data_git_describe = "v0.0-14152-g318a5af53e"
data_git_msg = """\
commit 318a5af53ee41d4030ab6a4b3a81f2402ec62e77
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Sep 16 18:28:30 2022 +0000

    [flash_ctrl,dv] Add checker for flash_ctrl_sec_cm test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
