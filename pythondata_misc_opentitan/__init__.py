import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14178"
version_tuple = (0, 0, 14178)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14178")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14036"
data_version_tuple = (0, 0, 14036)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14036")
except ImportError:
    pass
data_git_hash = "2c9e03508018a54abe52198e8316eff15197e997"
data_git_describe = "v0.0-14036-g2c9e035080"
data_git_msg = """\
commit 2c9e03508018a54abe52198e8316eff15197e997
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Sep 13 12:15:24 2022 -0700

    Fix unit test
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
