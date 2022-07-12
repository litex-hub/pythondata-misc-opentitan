import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13042"
version_tuple = (0, 0, 13042)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13042")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12900"
data_version_tuple = (0, 0, 12900)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12900")
except ImportError:
    pass
data_git_hash = "ba51d069e96060409d83d770239748f4acc9ec88"
data_git_describe = "v0.0-12900-gba51d069e9"
data_git_msg = """\
commit ba51d069e96060409d83d770239748f4acc9ec88
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Jul 11 09:03:53 2022 -0700

    [doc] Add more links pointing to secure hw design guidelines
    
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
