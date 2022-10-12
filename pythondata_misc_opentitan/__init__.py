import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14694"
version_tuple = (0, 0, 14694)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14694")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14552"
data_version_tuple = (0, 0, 14552)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14552")
except ImportError:
    pass
data_git_hash = "e79e3525c284efe83f957ba62a24cd91be94370b"
data_git_describe = "v0.0-14552-ge79e3525c2"
data_git_msg = """\
commit e79e3525c284efe83f957ba62a24cd91be94370b
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Oct 11 13:42:29 2022 -0700

    [flash_ctrl] Clean-up comments
    
    - Address #15392
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
