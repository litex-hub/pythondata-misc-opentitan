import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11011"
version_tuple = (0, 0, 11011)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11011")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10885"
data_version_tuple = (0, 0, 10885)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10885")
except ImportError:
    pass
data_git_hash = "4ac33d98b562fb25a55fb3d9793bce8e534134e5"
data_git_describe = "v0.0-10885-g4ac33d98b"
data_git_msg = """\
commit 4ac33d98b562fb25a55fb3d9793bce8e534134e5
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 21 20:15:08 2022 +0100

    [doc] Fix markdown in firmware update documentation
    
    The sub-items are not rendered correctly if the numbering is wrong.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
