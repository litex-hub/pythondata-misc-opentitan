import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9345"
version_tuple = (0, 0, 9345)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9345")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9228"
data_version_tuple = (0, 0, 9228)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9228")
except ImportError:
    pass
data_git_hash = "4de8e8272eae0ebcebf037aa380992dbce6d984c"
data_git_describe = "v0.0-9228-g4de8e8272"
data_git_msg = """\
commit 4de8e8272eae0ebcebf037aa380992dbce6d984c
Author: Weicai Yang <weicai@google.com>
Date:   Tue Jan 4 20:49:56 2022 -0800

    [sram/dv] Fix stress_all_with_rand_reset
    
    Remove escalation test as it invokes another reset
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
