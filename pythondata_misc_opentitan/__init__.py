import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9534"
version_tuple = (0, 0, 9534)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9534")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9412"
data_version_tuple = (0, 0, 9412)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9412")
except ImportError:
    pass
data_git_hash = "f81c8aca4edcd5420f972513fbbc39f17af0ac5e"
data_git_describe = "v0.0-9412-gf81c8aca4"
data_git_msg = """\
commit f81c8aca4edcd5420f972513fbbc39f17af0ac5e
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Jan 13 11:03:25 2022 +0000

    [rom_ctrl, dv] Added new checker and coverpoint to testplan
    
    Enhanced testplan to include checkers and covergroups to ensure that
    tilelink accesses are blocked until pwrmgr_data_o.done is asserted
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
