import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15240"
version_tuple = (0, 0, 15240)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15240")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15098"
data_version_tuple = (0, 0, 15098)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15098")
except ImportError:
    pass
data_git_hash = "ae49ebc932e0711b1134aa0666197575a6f0cb10"
data_git_describe = "v0.0-15098-gae49ebc932"
data_git_msg = """\
commit ae49ebc932e0711b1134aa0666197575a6f0cb10
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Nov 3 23:26:48 2022 -0400

    [test] Complete rom_e2e_shutdown_watchdog
    
    Fixes #14272
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
