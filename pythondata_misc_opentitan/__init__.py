import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14422"
version_tuple = (0, 0, 14422)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14422")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14280"
data_version_tuple = (0, 0, 14280)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14280")
except ImportError:
    pass
data_git_hash = "5ca06aa40bc864f0b903da1cebb0013a842ec08c"
data_git_describe = "v0.0-14280-g5ca06aa40b"
data_git_msg = """\
commit 5ca06aa40bc864f0b903da1cebb0013a842ec08c
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Sep 22 09:14:27 2022 -0700

    doc(chip): Revise testplan to cover any sleep modes.
    
    To cover `chip_sw_random_sleep_pin_wake` test, the
    `chip_sw_sleep_pin_wake` covers normal sleep mode too. This commit
    revises the testplan to mention the deep/ normal sleep states.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
