import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9489"
version_tuple = (0, 0, 9489)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9489")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9371"
data_version_tuple = (0, 0, 9371)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9371")
except ImportError:
    pass
data_git_hash = "c759af5274d11276c006d661ce14fb99d0e7774b"
data_git_describe = "v0.0-9371-gc759af527"
data_git_msg = """\
commit c759af5274d11276c006d661ce14fb99d0e7774b
Author: Michael Schaffner <msf@google.com>
Date:   Tue Jan 11 18:51:23 2022 -0800

    Revert "Revert "[pinmux_wkup] Change comparison to GE to stay on the safe side""
    
    This reverts commit 2d6cd7a7e3e112a8c73881e0330bbd5a26d3bce4.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
