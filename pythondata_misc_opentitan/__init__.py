import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10093"
version_tuple = (0, 0, 10093)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10093")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9969"
data_version_tuple = (0, 0, 9969)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9969")
except ImportError:
    pass
data_git_hash = "0b1c23022f1d1f2d7e5836379d3dc30d2dc91d86"
data_git_describe = "v0.0-9969-g0b1c23022"
data_git_msg = """\
commit 0b1c23022f1d1f2d7e5836379d3dc30d2dc91d86
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Feb 4 10:23:42 2022 -0800

    [entropy_src/rtl] Use mubi4_test_false_loose
    
    Changing the mubi check to "false_loose" for the register lock
    function.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
