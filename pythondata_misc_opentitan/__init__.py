import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14684"
version_tuple = (0, 0, 14684)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14684")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14542"
data_version_tuple = (0, 0, 14542)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14542")
except ImportError:
    pass
data_git_hash = "90c670abcbfdeb55ae5c0ef9af4406d25c8cef1c"
data_git_describe = "v0.0-14542-g90c670abcb"
data_git_msg = """\
commit 90c670abcbfdeb55ae5c0ef9af4406d25c8cef1c
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Oct 11 13:20:37 2022 -0700

    [dv/pwrmgr] Remove pwrmgr_clk_ctrl code
    
    The code under pwrmgr_clk_ctrl_agent was disabled some time ago. This
    just removes the code.
    
    Fixes #15315
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
