import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10738"
version_tuple = (0, 0, 10738)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10738")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10612"
data_version_tuple = (0, 0, 10612)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10612")
except ImportError:
    pass
data_git_hash = "54b21340f7f41f5ff378033e0ae4480333e14291"
data_git_describe = "v0.0-10612-g54b21340f"
data_git_msg = """\
commit 54b21340f7f41f5ff378033e0ae4480333e14291
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 7 10:41:11 2022 +0000

    Revert "[adc_ctrl/dv] Added counter tests"
    
    This reverts commit fe294ca0b6e02ff8f3f9d87e9ba54579139edc0e, which
    breaks CI.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
