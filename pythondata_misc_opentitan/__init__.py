import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8677"
version_tuple = (0, 0, 8677)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8677")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8565"
data_version_tuple = (0, 0, 8565)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8565")
except ImportError:
    pass
data_git_hash = "3653c65fa582c2104d2bf7295e6637a37b96b432"
data_git_describe = "v0.0-8565-g3653c65fa"
data_git_msg = """\
commit 3653c65fa582c2104d2bf7295e6637a37b96b432
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Nov 9 11:46:05 2021 +0000

    [sw/crypto] Clarify bounds assumptions for Montgomery R^2.
    
    The Ibex implementation, on closer inspection, doesn't actually require
    R / 2 < M, so the comment is rephrased to not state that it does. The
    OTBN implementation is greatly simplified by the assumption that R / 2
    < M, so it is modified to assume so and justify the assumption by citing
    FIPS.
    
    This commit also includes a minor adjustment to the R^2 loop, making it
    a loop instead of a loopi so as not to consume the loop stack
    unnecessarily.
    
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
