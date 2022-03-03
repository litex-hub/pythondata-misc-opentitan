import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10676"
version_tuple = (0, 0, 10676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10550"
data_version_tuple = (0, 0, 10550)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10550")
except ImportError:
    pass
data_git_hash = "196b79a1748d641d0ed237f763f4d47fdaf5e0e7"
data_git_describe = "v0.0-10550-g196b79a17"
data_git_msg = """\
commit 196b79a1748d641d0ed237f763f4d47fdaf5e0e7
Author: Alex Bradbury <asb@lowrisc.org>
Date:   Thu Mar 3 07:49:37 2022 +0000

    [misc] Remove myself from COMMITTERS/CODEOWNERS
    
    Signed-off-by: Alex Bradbury <asb@lowrisc.org>

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
