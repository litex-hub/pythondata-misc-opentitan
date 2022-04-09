import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11494"
version_tuple = (0, 0, 11494)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11494")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11368"
data_version_tuple = (0, 0, 11368)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11368")
except ImportError:
    pass
data_git_hash = "43a24e6461673730a30de1c66d7c997f89bd7597"
data_git_describe = "v0.0-11368-g43a24e646"
data_git_msg = """\
commit 43a24e6461673730a30de1c66d7c997f89bd7597
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Apr 7 00:37:07 2022 -0700

    [cdc-rand] Enable CDC random delay injection
    
    This commit builds upon the work by @udinator and instantiates the CDC random
    delay model within the prim_flop_2sync module. It injects delays into the incoming
    source data before it passes through the 2 flop synchronizer.
    
    It also comes with its mini testbench, which currently lacks any checks, but
    serves as a way to view waves and check the behavior via visual inspection.
    
    The delay insertion is currently disabled due to smoke regr failures.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
