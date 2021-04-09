import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5790"
version_tuple = (0, 0, 5790)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5790")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5695"
data_version_tuple = (0, 0, 5695)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5695")
except ImportError:
    pass
data_git_hash = "7e26d6f4afaf1488e4987d3ee6cb991d4dc4fdab"
data_git_describe = "v0.0-5695-g7e26d6f4a"
data_git_msg = """\
commit 7e26d6f4afaf1488e4987d3ee6cb991d4dc4fdab
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Apr 8 14:05:11 2021 -0700

    [dv/sram] increase timeout for bijecttion test
    
    this PR increases the timeout period for the bijection test,
    fixing some nightly regression timeout failures.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
