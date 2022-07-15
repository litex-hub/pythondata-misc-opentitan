import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13101"
version_tuple = (0, 0, 13101)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13101")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12959"
data_version_tuple = (0, 0, 12959)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12959")
except ImportError:
    pass
data_git_hash = "f4c69a028fe09d6cb0e7a66fc7f79f8442c9a6ea"
data_git_describe = "v0.0-12959-gf4c69a028f"
data_git_msg = """\
commit f4c69a028fe09d6cb0e7a66fc7f79f8442c9a6ea
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Jul 15 09:46:56 2022 +0200

    [otbn,rtl] Fix `adder_y_res_used`
    
    `adder_y_res_used` indicates whether `adder_y_res` is used in any way.
    This is relevant for determining if upstream integrity errors could
    possibly have any effect.  Prior to this commit, `adder_y_res_used` was
    `0` in one case where `adder_y_res` is used in an `if` condition.  This
    is wrong, and this commit fixes this flaw.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
