import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13260"
version_tuple = (0, 0, 13260)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13260")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13118"
data_version_tuple = (0, 0, 13118)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13118")
except ImportError:
    pass
data_git_hash = "612efc49a499ff83af2632616b041f7ba23da6ab"
data_git_describe = "v0.0-13118-g612efc49a4"
data_git_msg = """\
commit 612efc49a499ff83af2632616b041f7ba23da6ab
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jul 25 10:05:32 2022 -0700

    [dv/kmac] Fix unmapped testplan
    
    This PR fixes unmapped stress_all tests because they have not been
    declared in the testplan.
    
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
