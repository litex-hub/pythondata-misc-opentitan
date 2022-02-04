import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10087"
version_tuple = (0, 0, 10087)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10087")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9963"
data_version_tuple = (0, 0, 9963)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9963")
except ImportError:
    pass
data_git_hash = "079a63dec851f09b7fe5a10d8691190b8aa11818"
data_git_describe = "v0.0-9963-g079a63dec"
data_git_msg = """\
commit 079a63dec851f09b7fe5a10d8691190b8aa11818
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Fri Feb 4 16:21:13 2022 +0000

    [jtag_riscv_agent] Fixed bug in jtag_riscv_monitor
    
    - Small bug injected by PR #10415
    We need to record the operation field from the initial DMI request
    as the same field is used by the status transaction to indicate
    the access has succeded failed or is still in progress.
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
