import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14729"
version_tuple = (0, 0, 14729)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14729")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14587"
data_version_tuple = (0, 0, 14587)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14587")
except ImportError:
    pass
data_git_hash = "0ccf5d9703064f2eaa19ece04ea63021783f4508"
data_git_describe = "v0.0-14587-g0ccf5d9703"
data_git_msg = """\
commit 0ccf5d9703064f2eaa19ece04ea63021783f4508
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Fri Sep 23 15:05:21 2022 +0100

    [rom, e2e] add `keymgr_init` test
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
