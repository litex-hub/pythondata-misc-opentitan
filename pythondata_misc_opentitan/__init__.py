import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10480"
version_tuple = (0, 0, 10480)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10480")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10354"
data_version_tuple = (0, 0, 10354)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10354")
except ImportError:
    pass
data_git_hash = "4b470bc12e5da64e6c9c7eed538962d71cd698a4"
data_git_describe = "v0.0-10354-g4b470bc12"
data_git_msg = """\
commit 4b470bc12e5da64e6c9c7eed538962d71cd698a4
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Tue Feb 22 01:10:04 2022 +0000

    [kmac,dv] Using Key Sideload with parameters
    
    This commit includes using parameters when calling key sideload.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
