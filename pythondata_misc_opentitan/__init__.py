import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12885"
version_tuple = (0, 0, 12885)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12885")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12743"
data_version_tuple = (0, 0, 12743)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12743")
except ImportError:
    pass
data_git_hash = "badbbac145fce9f37c822883e3faf6ba777104d1"
data_git_describe = "v0.0-12743-gbadbbac145"
data_git_msg = """\
commit badbbac145fce9f37c822883e3faf6ba777104d1
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Jun 28 15:41:41 2022 +0200

    [alert_handler] Add some more assertions to check wait cycle mask
    
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
