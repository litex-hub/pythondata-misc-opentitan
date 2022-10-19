import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14846"
version_tuple = (0, 0, 14846)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14846")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14704"
data_version_tuple = (0, 0, 14704)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14704")
except ImportError:
    pass
data_git_hash = "68ec61ba0e02859f16ff8a9a4c95124d2ad9fb48"
data_git_describe = "v0.0-14704-g68ec61ba0e"
data_git_msg = """\
commit 68ec61ba0e02859f16ff8a9a4c95124d2ad9fb48
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Oct 18 08:00:55 2022 -0700

    [rom-e2e] Update sfdp test to check more fields
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
