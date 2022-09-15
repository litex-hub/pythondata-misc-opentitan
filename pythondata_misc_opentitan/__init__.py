import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14240"
version_tuple = (0, 0, 14240)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14240")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14098"
data_version_tuple = (0, 0, 14098)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14098")
except ImportError:
    pass
data_git_hash = "1923e596f5ad0cc4d3f3477b3c93eee001a8f7e6"
data_git_describe = "v0.0-14098-g1923e596f5"
data_git_msg = """\
commit 1923e596f5ad0cc4d3f3477b3c93eee001a8f7e6
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Sep 15 03:14:43 2022 -0700

    [chip dv] Fix for UARt smoketest signed
    
    Contention on IOC4 caused due to external weak pull up
    from the testbench and weak pull down by the ROM
    code. Quick and dirty patch applied for now, by
    disabling the X check on IOC4.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
