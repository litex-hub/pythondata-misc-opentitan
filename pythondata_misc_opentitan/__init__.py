import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14939"
version_tuple = (0, 0, 14939)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14939")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14797"
data_version_tuple = (0, 0, 14797)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14797")
except ImportError:
    pass
data_git_hash = "051e25944b558ca9c8c8ccce837cc4f3e36d2d60"
data_git_describe = "v0.0-14797-g051e25944b"
data_git_msg = """\
commit 051e25944b558ca9c8c8ccce837cc4f3e36d2d60
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Oct 24 12:21:19 2022 -0400

    [test] Add rom_e2e_weak_straps to the rom e2e testplan
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
