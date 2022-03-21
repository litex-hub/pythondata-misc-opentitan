import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11013"
version_tuple = (0, 0, 11013)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11013")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10887"
data_version_tuple = (0, 0, 10887)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10887")
except ImportError:
    pass
data_git_hash = "87b087b65d5b852510a83267d9ae8e68bafc5061"
data_git_describe = "v0.0-10887-g87b087b65"
data_git_msg = """\
commit 87b087b65d5b852510a83267d9ae8e68bafc5061
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Mar 21 11:57:49 2022 -0700

    [sysrst_ctrl] Minor label cleanup in sysrst_ctrl_keyintr
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
