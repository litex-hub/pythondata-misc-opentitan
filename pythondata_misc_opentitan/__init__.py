import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14402"
version_tuple = (0, 0, 14402)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14402")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14260"
data_version_tuple = (0, 0, 14260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14260")
except ImportError:
    pass
data_git_hash = "a3f32c34d8121f811d1f7ae367facc50c2b46195"
data_git_describe = "v0.0-14260-ga3f32c34d8"
data_git_msg = """\
commit a3f32c34d8121f811d1f7ae367facc50c2b46195
Author: Weicai Yang <weicai@google.com>
Date:   Wed Sep 21 22:45:45 2022 -0700

    [chip, dv] chip_sw_rv_dm_jtag_tap_sel
    
    It's a subset of chip_sw_tap_strap_sampling.
    
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
