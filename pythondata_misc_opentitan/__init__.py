import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10382"
version_tuple = (0, 0, 10382)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10382")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10256"
data_version_tuple = (0, 0, 10256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10256")
except ImportError:
    pass
data_git_hash = "3d4b2f528dea1191fcfc340b4482ae0acd598b65"
data_git_describe = "v0.0-10256-g3d4b2f528"
data_git_msg = """\
commit 3d4b2f528dea1191fcfc340b4482ae0acd598b65
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Thu Feb 10 14:04:39 2022 +0100

    [kmac] increased HD of mux_sel
    
    Signed-off-by: Michael Tempelmeier <michael.tempelmeier@gi-de.com>

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
