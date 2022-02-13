import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10276"
version_tuple = (0, 0, 10276)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10276")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10150"
data_version_tuple = (0, 0, 10150)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10150")
except ImportError:
    pass
data_git_hash = "7f5112a95ae059cb6af5fd6a84772e2c463af509"
data_git_describe = "v0.0-10150-g7f5112a95"
data_git_msg = """\
commit 7f5112a95ae059cb6af5fd6a84772e2c463af509
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Sat Feb 5 00:18:48 2022 +0000

    [silicon_creator] Harden epmp_state_check return value
    
    Use a counter rather than a bool to track whether a mismatch has
    been detected.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
