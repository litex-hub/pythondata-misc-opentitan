import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5888"
version_tuple = (0, 0, 5888)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5888")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5793"
data_version_tuple = (0, 0, 5793)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5793")
except ImportError:
    pass
data_git_hash = "683f9ece3b584737fdabf966c11548e8853cd73b"
data_git_describe = "v0.0-5793-g683f9ece3"
data_git_msg = """\
commit 683f9ece3b584737fdabf966c11548e8853cd73b
Author: Jacob Levy <jacob.levy@opentitan.org>
Date:   Thu Apr 15 11:40:29 2021 +0300

    [AST] Update parameters
    
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
