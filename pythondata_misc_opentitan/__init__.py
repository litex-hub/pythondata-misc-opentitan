import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12615"
version_tuple = (0, 0, 12615)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12615")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12473"
data_version_tuple = (0, 0, 12473)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12473")
except ImportError:
    pass
data_git_hash = "60b4fedbff0284f02eabfdaec07f4852f852e400"
data_git_describe = "v0.0-12473-g60b4fedbf"
data_git_msg = """\
commit 60b4fedbff0284f02eabfdaec07f4852f852e400
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Jun 6 13:51:49 2022 -0400

    [sw/silicon_creator] Set initial watchdog bite threshold to 1 s
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
