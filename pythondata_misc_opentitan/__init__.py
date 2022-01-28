import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9854"
version_tuple = (0, 0, 9854)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9854")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9730"
data_version_tuple = (0, 0, 9730)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9730")
except ImportError:
    pass
data_git_hash = "74a44cc57118949e5bcbda8175ec2c507fc2414c"
data_git_describe = "v0.0-9730-g74a44cc57"
data_git_msg = """\
commit 74a44cc57118949e5bcbda8175ec2c507fc2414c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Jan 26 16:31:23 2022 -0800

    [lc_ctrl/doc] Update system integration diagram
    
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
