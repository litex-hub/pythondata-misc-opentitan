import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9387"
version_tuple = (0, 0, 9387)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9387")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9270"
data_version_tuple = (0, 0, 9270)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9270")
except ImportError:
    pass
data_git_hash = "0eb98eb2d1b72c72e9577b1d7c5a38b72cbe4933"
data_git_describe = "v0.0-9270-g0eb98eb2d"
data_git_msg = """\
commit 0eb98eb2d1b72c72e9577b1d7c5a38b72cbe4933
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 6 14:15:15 2022 -0800

    [fpv/pinmux] Add an entry for chip_earlgrey settings
    
    This PR adds a hjson entry for pinmux with chip_earlgrey settings.
    
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
