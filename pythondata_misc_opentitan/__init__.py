import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12635"
version_tuple = (0, 0, 12635)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12635")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12493"
data_version_tuple = (0, 0, 12493)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12493")
except ImportError:
    pass
data_git_hash = "6084cfa936b25826bab0db21a60e925a33fd6b0e"
data_git_describe = "v0.0-12493-g6084cfa93"
data_git_msg = """\
commit 6084cfa936b25826bab0db21a60e925a33fd6b0e
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Thu Jun 9 17:52:23 2022 +0100

    [otbn,dv] Illegal Bus Access fixup
    
    This commit includes changes in the do_mem_acc task.
    Main idea is to poll TL bus requests for DMEM and IMEM and send relevant
    error code to the model right when it happens.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
