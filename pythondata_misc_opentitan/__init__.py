import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8780"
version_tuple = (0, 0, 8780)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8780")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8668"
data_version_tuple = (0, 0, 8668)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8668")
except ImportError:
    pass
data_git_hash = "839dcdc719634e951e372255e5046595d2afa4e2"
data_git_describe = "v0.0-8668-g839dcdc71"
data_git_msg = """\
commit 839dcdc719634e951e372255e5046595d2afa4e2
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Nov 19 09:28:43 2021 -0500

    [sw/silicon_creator] Minor fixes in sec_mmio_unittest.cc
    
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
