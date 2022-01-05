import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9331"
version_tuple = (0, 0, 9331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9214"
data_version_tuple = (0, 0, 9214)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9214")
except ImportError:
    pass
data_git_hash = "66acab0f4de6194018614771c65399a6a6013fe0"
data_git_describe = "v0.0-9214-g66acab0f4"
data_git_msg = """\
commit 66acab0f4de6194018614771c65399a6a6013fe0
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jan 4 12:26:20 2022 -0800

    [fpv/pinmux] Add aon_clock and reset to run script
    
    This PR adds aon_clk and aon_rst to the fpv.tcl script.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
