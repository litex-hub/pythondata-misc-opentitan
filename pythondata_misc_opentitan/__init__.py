import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8177"
version_tuple = (0, 0, 8177)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8177")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8065"
data_version_tuple = (0, 0, 8065)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8065")
except ImportError:
    pass
data_git_hash = "9e18b46e0a96355c3c163629c8a90b70b805f24e"
data_git_describe = "v0.0-8065-g9e18b46e0"
data_git_msg = """\
commit 9e18b46e0a96355c3c163629c8a90b70b805f24e
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Fri Oct 8 12:09:28 2021 +0100

    Use pycryptodome from upstream
    
    A new versin of pycryptodome has been released which includes support
    for cSHAKE.
    
    Release notes: https://www.pycryptodome.org/en/latest/src/changelog.html#october-2021
    
    Fixes #6694
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
