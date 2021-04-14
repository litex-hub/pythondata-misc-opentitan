import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5868"
version_tuple = (0, 0, 5868)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5868")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5773"
data_version_tuple = (0, 0, 5773)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5773")
except ImportError:
    pass
data_git_hash = "3b847a73a8f1eb302fa02c21c648d8271f2c82e4"
data_git_describe = "v0.0-5773-g3b847a73a"
data_git_msg = """\
commit 3b847a73a8f1eb302fa02c21c648d8271f2c82e4
Author: Weicai Yang <weicai@google.com>
Date:   Fri Apr 9 17:59:02 2021 -0700

    [dv] Support multi-ral (part 4)
    
    Just realized we should have different clock/rst for different TL
    interface.
    store multiple tl_vif in `clk_rst_vifs` and keep the default
    `clk_rst_vif`
    
    This is probably the final part of multi-ral support
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
