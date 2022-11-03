import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15189"
version_tuple = (0, 0, 15189)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15189")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15047"
data_version_tuple = (0, 0, 15047)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15047")
except ImportError:
    pass
data_git_hash = "1a0c43025eb0a475db5cf1ae5944e2063736629c"
data_git_describe = "v0.0-15047-g1a0c43025e"
data_git_msg = """\
commit 1a0c43025eb0a475db5cf1ae5944e2063736629c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Nov 3 10:34:02 2022 -0700

    [dv/csrng_agent] Update coverage collection
    
    This PR splits CSRNG command coverage to two parts:
    On device mode, some acmd values are illegal,
    but in host mode, we want to check how csrng response to these illegal
    cmds.
    
    Related issue: #15947
    
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
