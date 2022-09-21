import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14354"
version_tuple = (0, 0, 14354)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14354")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14212"
data_version_tuple = (0, 0, 14212)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14212")
except ImportError:
    pass
data_git_hash = "3ecad13714190fb493897e02fc14805eaf43aa7a"
data_git_describe = "v0.0-14212-g3ecad13714"
data_git_msg = """\
commit 3ecad13714190fb493897e02fc14805eaf43aa7a
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Sep 20 08:19:29 2022 -0700

    [dif/sysrst_ctrl] move to S2
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
