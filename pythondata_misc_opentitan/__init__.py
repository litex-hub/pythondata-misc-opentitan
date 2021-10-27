import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8478"
version_tuple = (0, 0, 8478)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8478")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8366"
data_version_tuple = (0, 0, 8366)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8366")
except ImportError:
    pass
data_git_hash = "76cb99e40384216db61c87ab40d0aa66829ca9db"
data_git_describe = "v0.0-8366-g76cb99e40"
data_git_msg = """\
commit 76cb99e40384216db61c87ab40d0aa66829ca9db
Author: Timothy Chen <timothytim@google.com>
Date:   Sat Oct 16 00:29:45 2021 -0700

    [sram_ctrl] Various fixes
    
    - Address issues listed in #8706
    - Swap the order of sram_byte and rsp_gen
    - Add read qualification to integrity data
    - Add outstanding transaction handling
    - Retain workarounds for #7461, that will be addressed separately.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
