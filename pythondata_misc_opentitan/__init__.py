import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5710"
version_tuple = (0, 0, 5710)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5710")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5615"
data_version_tuple = (0, 0, 5615)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5615")
except ImportError:
    pass
data_git_hash = "e371842b0efb9a7d160f7909415190fd583b6c68"
data_git_describe = "v0.0-5615-ge371842b0"
data_git_msg = """\
commit e371842b0efb9a7d160f7909415190fd583b6c68
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Apr 2 18:25:42 2021 -0700

    [docs/hugo] Move to hugo version 0.82.0
    
    When adding more pinmux signals and pads, we run into a
    funny error where HUGO can't read the generated pinmux register
    documentation anymore since the file is too big. This file
    limitation has just recently (3 months ago) been removed.
    
    See https://github.com/gohugoio/hugo/pull/8172 for reference.
    
    This commit moves to HUGO 0.82.0 which contains this fix.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
