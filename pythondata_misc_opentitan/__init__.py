import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14193"
version_tuple = (0, 0, 14193)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14193")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14051"
data_version_tuple = (0, 0, 14051)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14051")
except ImportError:
    pass
data_git_hash = "178fab89009e7290fb1c01a95a81b9b583c233ba"
data_git_describe = "v0.0-14051-g178fab8900"
data_git_msg = """\
commit 178fab89009e7290fb1c01a95a81b9b583c233ba
Author: Michael Schaffner <msf@google.com>
Date:   Tue Sep 13 11:42:41 2022 -0700

    [test] Correct cross referenced testpoint name
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
