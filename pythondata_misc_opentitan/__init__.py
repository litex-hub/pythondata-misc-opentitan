import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12676"
version_tuple = (0, 0, 12676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12534"
data_version_tuple = (0, 0, 12534)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12534")
except ImportError:
    pass
data_git_hash = "edbd61c6633f87650846d3f07053d24dbf535f90"
data_git_describe = "v0.0-12534-gedbd61c66"
data_git_msg = """\
commit edbd61c6633f87650846d3f07053d24dbf535f90
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jun 13 14:33:17 2022 +0200

    [otp_ctrl] Remove TODO from RTL
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
