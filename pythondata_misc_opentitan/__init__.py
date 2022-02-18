import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10418"
version_tuple = (0, 0, 10418)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10418")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10292"
data_version_tuple = (0, 0, 10292)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10292")
except ImportError:
    pass
data_git_hash = "334a1d7732c8df74af636c966cd4eb231cf08c9e"
data_git_describe = "v0.0-10292-g334a1d773"
data_git_msg = """\
commit 334a1d7732c8df74af636c966cd4eb231cf08c9e
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Feb 17 07:13:23 2022 -0800

    [entropy_src/rtl] Remove gating on err_code status register
    
    The REGWEN change has created conflicting conditions for testing the ERR_CODE register.
    Two possible ways to resolve, either remove the redundant gating, or remove the
    REGWEN keyword on the ERROR_CODE_TEST register.
    Removing the enable gating makes it consistant with other bits in this register.
    Removing the REGWEN keyword seems to be a system exposure so not doing that.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
