import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14682"
version_tuple = (0, 0, 14682)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14682")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14540"
data_version_tuple = (0, 0, 14540)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14540")
except ImportError:
    pass
data_git_hash = "7c7151f57b26837e5774ea93cafd377c8a4496b7"
data_git_describe = "v0.0-14540-g7c7151f57b"
data_git_msg = """\
commit 7c7151f57b26837e5774ea93cafd377c8a4496b7
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 11 13:34:36 2022 -0700

    [dv/clkmgr] Declare V2S
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
