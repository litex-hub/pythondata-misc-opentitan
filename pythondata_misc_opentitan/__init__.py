import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9666"
version_tuple = (0, 0, 9666)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9666")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9544"
data_version_tuple = (0, 0, 9544)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9544")
except ImportError:
    pass
data_git_hash = "cd01ed7c5d6835840b598215e726aed6add77064"
data_git_describe = "v0.0-9544-gcd01ed7c5"
data_git_msg = """\
commit cd01ed7c5d6835840b598215e726aed6add77064
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Jan 14 15:42:08 2022 -0500

    [sw/silicon_creator] Harden flash_ctrl_info_page_enum_t
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
