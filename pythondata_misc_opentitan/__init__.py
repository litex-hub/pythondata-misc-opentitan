import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15025"
version_tuple = (0, 0, 15025)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15025")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14883"
data_version_tuple = (0, 0, 14883)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14883")
except ImportError:
    pass
data_git_hash = "0f3344d516febba6bc6857f1785803749be0a642"
data_git_describe = "v0.0-14883-g0f3344d516"
data_git_msg = """\
commit 0f3344d516febba6bc6857f1785803749be0a642
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Oct 28 09:52:24 2022 -0400

    [sw/silicon_creator] Use sh256 instead of crc32 to check boot_data integrity
    
    This commit reverts ba9d370d821c84fedc514f8186f7ff06ba45e86c added in
     #15397 as discussed in the security meeting.
    
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
