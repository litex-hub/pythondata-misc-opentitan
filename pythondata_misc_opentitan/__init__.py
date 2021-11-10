import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8663"
version_tuple = (0, 0, 8663)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8663")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8551"
data_version_tuple = (0, 0, 8551)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8551")
except ImportError:
    pass
data_git_hash = "42b3e66d7ca3aee8e748c20e4c7bc1cdd523b413"
data_git_describe = "v0.0-8551-g42b3e66d7"
data_git_msg = """\
commit 42b3e66d7ca3aee8e748c20e4c7bc1cdd523b413
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Oct 29 11:27:50 2021 +0100

    [sw/silicon_creator] Separate OTBN error codes in mask ROM.
    
    In order to make the crypto library more portable, we change the error
    types in the mask ROM OTBN driver to be OTBN-specific errors instead of
    generic ROM errors, and then use those error codes in the crypto library
    as well.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
