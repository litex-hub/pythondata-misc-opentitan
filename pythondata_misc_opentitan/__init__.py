import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15176"
version_tuple = (0, 0, 15176)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15176")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15034"
data_version_tuple = (0, 0, 15034)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15034")
except ImportError:
    pass
data_git_hash = "22b25ce20cb22e3e5f95e010b60ec2e5e26ab971"
data_git_describe = "v0.0-15034-g22b25ce20c"
data_git_msg = """\
commit 22b25ce20cb22e3e5f95e010b60ec2e5e26ab971
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Nov 3 10:40:39 2022 -0700

    [edn/doc] Update rw0c register description
    
    Fix a small typo in regwen. The RW0C should be write value zero to set
    the regwen.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
