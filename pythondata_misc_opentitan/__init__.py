import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5580"
version_tuple = (0, 0, 5580)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5580")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5485"
data_version_tuple = (0, 0, 5485)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5485")
except ImportError:
    pass
data_git_hash = "9855d4bb1e0d6664c4a33882fd896c4ebabef02b"
data_git_describe = "v0.0-5485-g9855d4bb1"
data_git_msg = """\
commit 9855d4bb1e0d6664c4a33882fd896c4ebabef02b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Dec 2 08:41:35 2020 +0000

    [rom_ctrl] Add initial RTL
    
    This doesn't really do anything very interesting: it just replaces the
    ROM instantiation that was in top_earlgrey.sv and generates a verbose
    wrapper around it.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
