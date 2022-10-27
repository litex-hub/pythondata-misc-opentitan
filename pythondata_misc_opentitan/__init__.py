import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15002"
version_tuple = (0, 0, 15002)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15002")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14860"
data_version_tuple = (0, 0, 14860)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14860")
except ImportError:
    pass
data_git_hash = "a6f5f00b38decb430bed51c9a072918980e1f915"
data_git_describe = "v0.0-14860-ga6f5f00b38"
data_git_msg = """\
commit a6f5f00b38decb430bed51c9a072918980e1f915
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 27 08:31:26 2022 -0700

    [top] X-ref ast_sys_clk_jitter testpoint
    
    - The ast_sys_clk_jitter testpoint is already covered
      by chip_sw_clkmgr_jitter, x-ref the two instead of
      adding more tests.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
