import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11460"
version_tuple = (0, 0, 11460)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11460")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11334"
data_version_tuple = (0, 0, 11334)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11334")
except ImportError:
    pass
data_git_hash = "0ef9e04697ab2f484bd588795c1e6a49ec892a56"
data_git_describe = "v0.0-11334-g0ef9e0469"
data_git_msg = """\
commit 0ef9e04697ab2f484bd588795c1e6a49ec892a56
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Apr 7 17:52:37 2022 +0100

    [rom_ctrl,rtl] Tweak extraction of in_state_done to avoid lint error
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
