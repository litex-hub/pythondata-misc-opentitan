import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14357"
version_tuple = (0, 0, 14357)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14357")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14215"
data_version_tuple = (0, 0, 14215)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14215")
except ImportError:
    pass
data_git_hash = "a339c389b819905dcc52c3dc3472b86df6364f70"
data_git_describe = "v0.0-14215-ga339c389b8"
data_git_msg = """\
commit a339c389b819905dcc52c3dc3472b86df6364f70
Author: Weicai Yang <weicai@google.com>
Date:   Tue Sep 20 16:33:35 2022 -0700

    [dv] Reduce the length of POR and fix regression failures
    
    Reset took too long which caused wait timeout.
    
    Addressed #15026 and fixed these 2 tests
    - chip_sw_lc_ctrl_transition
    - chip_sw_clkmgr_external_clk_src_for_lc
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
