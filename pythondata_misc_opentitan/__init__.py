import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14536"
version_tuple = (0, 0, 14536)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14536")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14394"
data_version_tuple = (0, 0, 14394)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14394")
except ImportError:
    pass
data_git_hash = "709af834e3ba2b35f958f91e6c30508f73e0ce99"
data_git_describe = "v0.0-14394-g709af834e3"
data_git_msg = """\
commit 709af834e3ba2b35f958f91e6c30508f73e0ce99
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Sep 30 03:05:25 2022 +0000

    [flash_ctrl,dv] Update filesystem support test
    
    Update filesystem support test(#15037)
     - Shift focus from 'erase' to 'double write'
     - Improve access resolution from 'page' to '8bytes'
    
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
