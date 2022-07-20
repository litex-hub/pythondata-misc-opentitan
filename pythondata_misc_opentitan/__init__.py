import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13196"
version_tuple = (0, 0, 13196)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13196")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13054"
data_version_tuple = (0, 0, 13054)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13054")
except ImportError:
    pass
data_git_hash = "9a9f97f35d0f0595e576869b6db0ad503ad359dd"
data_git_describe = "v0.0-13054-g9a9f97f35d"
data_git_msg = """\
commit 9a9f97f35d0f0595e576869b6db0ad503ad359dd
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Jul 19 03:59:01 2022 -0700

    [aes/dv] added FI for ctr fsm
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
