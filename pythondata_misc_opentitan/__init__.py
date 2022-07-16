import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13129"
version_tuple = (0, 0, 13129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12987"
data_version_tuple = (0, 0, 12987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12987")
except ImportError:
    pass
data_git_hash = "010a5a2c6a28d9ad06a4060417734af1af9e5d37"
data_git_describe = "v0.0-12987-g010a5a2c6a"
data_git_msg = """\
commit 010a5a2c6a28d9ad06a4060417734af1af9e5d37
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Jul 14 17:01:15 2022 -0700

    [dif/entropy_src] add alert threshold configs
    
    This updates the main entropy source configuration DIF (and all tests
    that use this DIF) to set the alert threshold CSR. Additionally,
    corresponding unit tests are also updated.
    
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
