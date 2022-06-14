import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12681"
version_tuple = (0, 0, 12681)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12681")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12539"
data_version_tuple = (0, 0, 12539)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12539")
except ImportError:
    pass
data_git_hash = "9634d8677a6d28e80f6083568d98b310bb809248"
data_git_describe = "v0.0-12539-g9634d8677"
data_git_msg = """\
commit 9634d8677a6d28e80f6083568d98b310bb809248
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon May 30 23:00:08 2022 +0000

    [dv,pwrmgr,top] pwrmgr normal sleep all wake up test
    
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
