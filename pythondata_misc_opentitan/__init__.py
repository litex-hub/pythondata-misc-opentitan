import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8892"
version_tuple = (0, 0, 8892)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8892")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8780"
data_version_tuple = (0, 0, 8780)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8780")
except ImportError:
    pass
data_git_hash = "051133de722181cdcaa8d4e62daf9ec1dc043c9d"
data_git_describe = "v0.0-8780-g051133de7"
data_git_msg = """\
commit 051133de722181cdcaa8d4e62daf9ec1dc043c9d
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Nov 24 12:09:10 2021 +0000

    [otbn,dv] Modelling EDN Request
    
    This commit includes changes in OTBN DV environment to support
    modelling EDN requests by RND or URND.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
