import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5889"
version_tuple = (0, 0, 5889)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5889")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5794"
data_version_tuple = (0, 0, 5794)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5794")
except ImportError:
    pass
data_git_hash = "9ffffe099c3605b27e21993dd8cb857e717566f7"
data_git_describe = "v0.0-5794-g9ffffe099"
data_git_msg = """\
commit 9ffffe099c3605b27e21993dd8cb857e717566f7
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Apr 14 11:04:08 2021 -0700

    [entropy_src/rtl] add a clean halt/start sequence
    
    This change allows entropy_src to stop immediately when disabled.
    It also locks all registers when enabled, except for the CONF register.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
