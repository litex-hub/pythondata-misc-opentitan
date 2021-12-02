import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8973"
version_tuple = (0, 0, 8973)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8973")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8861"
data_version_tuple = (0, 0, 8861)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8861")
except ImportError:
    pass
data_git_hash = "a8347d0e91a7ed00e2d85f7c6f9f1ffe2e3ab356"
data_git_describe = "v0.0-8861-ga8347d0e9"
data_git_msg = """\
commit a8347d0e91a7ed00e2d85f7c6f9f1ffe2e3ab356
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Dec 1 16:29:34 2021 -0500

    [sw/silicon_creator] Integrate boot_data to boot_policy, update unittest
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
