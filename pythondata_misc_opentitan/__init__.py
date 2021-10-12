import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8226"
version_tuple = (0, 0, 8226)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8226")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8114"
data_version_tuple = (0, 0, 8114)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8114")
except ImportError:
    pass
data_git_hash = "cd060f6286952190237cda16b5bccdad02db0e0a"
data_git_describe = "v0.0-8114-gcd060f628"
data_git_msg = """\
commit cd060f6286952190237cda16b5bccdad02db0e0a
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 11 22:20:35 2021 -0700

    [sram_ctrl/dv] Fix regression failure
    
    mask should be applied to both actual data and expected data
    Signed-off-by: Weicai Yang <weicai@google.com>

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
