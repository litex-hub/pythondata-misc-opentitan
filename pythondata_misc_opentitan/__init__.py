import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8443"
version_tuple = (0, 0, 8443)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8443")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8331"
data_version_tuple = (0, 0, 8331)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8331")
except ImportError:
    pass
data_git_hash = "a502032a3ecc8e9f3c0b9c935d935d8c78571f04"
data_git_describe = "v0.0-8331-ga502032a3"
data_git_msg = """\
commit a502032a3ecc8e9f3c0b9c935d935d8c78571f04
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Sat Oct 23 14:51:37 2021 -0700

    [chip, dv] Update autogen SW PLIC test
    
    - All peripherals (that emit IRQs) are now enabled
    - Removed helper macros to keep everything inline
    - Added workaround for rv_timer and aon_timer
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
