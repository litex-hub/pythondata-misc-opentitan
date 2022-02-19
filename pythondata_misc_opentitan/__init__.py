import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10450"
version_tuple = (0, 0, 10450)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10450")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10324"
data_version_tuple = (0, 0, 10324)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10324")
except ImportError:
    pass
data_git_hash = "143ebe944b7b67117d339f83146229dc52b3efb2"
data_git_describe = "v0.0-10324-g143ebe944"
data_git_msg = """\
commit 143ebe944b7b67117d339f83146229dc52b3efb2
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 16 14:22:21 2022 -0800

    [dv/jtag] Fix close source JTAG error
    
    This PR fixes close source JTAG error due to extra simulation delays
    in JTAG external clock.
    To avoid this issue, we will drive JTAG input at negedge.
    This PR also adds a max attempt to activate RV_DM to avoid simulation
    hanging.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
