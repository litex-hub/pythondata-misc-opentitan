import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14804"
version_tuple = (0, 0, 14804)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14804")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14662"
data_version_tuple = (0, 0, 14662)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14662")
except ImportError:
    pass
data_git_hash = "349d1a0dba9771ba64d070ad64459a85db91922e"
data_git_describe = "v0.0-14662-g349d1a0dba"
data_git_msg = """\
commit 349d1a0dba9771ba64d070ad64459a85db91922e
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Oct 13 11:29:20 2022 -0700

    refactor(reggen): Add Interrupt class
    
    Interrupt class is derived from Signal class. It defines `intr_type` on
    top of Signal class. The `intr_type` provides the way reggen
    distinguishes between event and status types. Each type creates their
    own access type for `INTR_STATE` and `INTR_TEST`.
    
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
