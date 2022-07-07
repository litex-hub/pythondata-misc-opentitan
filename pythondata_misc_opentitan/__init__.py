import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12951"
version_tuple = (0, 0, 12951)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12951")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12809"
data_version_tuple = (0, 0, 12809)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12809")
except ImportError:
    pass
data_git_hash = "96b1d5a9e293a9cf87b431444ffc2d1092a2d403"
data_git_describe = "v0.0-12809-g96b1d5a9e2"
data_git_msg = """\
commit 96b1d5a9e293a9cf87b431444ffc2d1092a2d403
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jul 6 12:14:11 2022 -0700

    [sram/dv] Fix d_error mismatch
    
    Fixed a mistake in #13135
    The `d_error` check should be added for chip_scoreboard, but wrongly added in
    sram_ctrl_scoreboard. sram_ctrl_scoreboard already checks it in another
    function.
    
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
