import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9547"
version_tuple = (0, 0, 9547)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9547")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9425"
data_version_tuple = (0, 0, 9425)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9425")
except ImportError:
    pass
data_git_hash = "e81c3258f6f9bb667f989e6ccefb32d8582e9dad"
data_git_describe = "v0.0-9425-ge81c3258f"
data_git_msg = """\
commit e81c3258f6f9bb667f989e6ccefb32d8582e9dad
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jan 14 14:37:09 2022 -0800

    [sysrst_ctrl] Trigger wakeup interrupt only when wkup_req rises
    
    See also: https://github.com/lowRISC/opentitan/pull/10034/files#r783573203
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
