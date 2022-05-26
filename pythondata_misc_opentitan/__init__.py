import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12343"
version_tuple = (0, 0, 12343)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12343")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12209"
data_version_tuple = (0, 0, 12209)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12209")
except ImportError:
    pass
data_git_hash = "61de2fda0e35a5b5f74675ba5d6a295988c253df"
data_git_describe = "v0.0-12209-g61de2fda0"
data_git_msg = """\
commit 61de2fda0e35a5b5f74675ba5d6a295988c253df
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu May 19 16:57:43 2022 +0100

    [otbn,rtl] Fix overflow in stack_top_idx
    
    We use next_stack_top_idx to derive next_top_valid_o, which says
    whether the stack has data in it. This check is based on seeing
    whether the index just above the top of the stack is nonzero or not.
    We were using StackDepthW bits and got an overflow when the stack
    filled up.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post134"
tool_version_tuple = (0, 0, 134)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post134")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
