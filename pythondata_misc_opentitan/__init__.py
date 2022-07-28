import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13313"
version_tuple = (0, 0, 13313)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13313")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13171"
data_version_tuple = (0, 0, 13171)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13171")
except ImportError:
    pass
data_git_hash = "9a202b52d8a7c026ae9ac8f25f0c1a4d714bb9a1"
data_git_describe = "v0.0-13171-g9a202b52d8"
data_git_msg = """\
commit 9a202b52d8a7c026ae9ac8f25f0c1a4d714bb9a1
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jul 27 16:05:13 2022 -0700

    [dv/kmac] Add cfg_regwen register check
    
    This PR adds checkings that cfg_regwen will be reset to 0 when kmac is
    not idle.
    Also write locked registers with random values if the cfg_regwen is
    locked.
    
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
