import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8710"
version_tuple = (0, 0, 8710)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8710")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8598"
data_version_tuple = (0, 0, 8598)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8598")
except ImportError:
    pass
data_git_hash = "1469f93bfd75eaeb35b87c734b2cdd01fa19ac21"
data_git_describe = "v0.0-8598-g1469f93bf"
data_git_msg = """\
commit 1469f93bfd75eaeb35b87c734b2cdd01fa19ac21
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Nov 11 05:00:21 2021 -0800

    [entropy_src/rtl] repcnt health tests fail pulses
    
    When rep count health tests fails, the signal is on solid.
    To properly predict counter values, the fail signal needs to be a pulse.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
