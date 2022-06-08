import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12571"
version_tuple = (0, 0, 12571)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12571")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12429"
data_version_tuple = (0, 0, 12429)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12429")
except ImportError:
    pass
data_git_hash = "d957c8654e10f029263a1bf10776eb0c7c98f536"
data_git_describe = "v0.0-12429-gd957c8654"
data_git_msg = """\
commit d957c8654e10f029263a1bf10776eb0c7c98f536
Author: Weicai Yang <weicai@google.com>
Date:   Tue Jun 7 15:00:30 2022 -0700

    [dv] Enable reg_wr_check test for all blocks
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
