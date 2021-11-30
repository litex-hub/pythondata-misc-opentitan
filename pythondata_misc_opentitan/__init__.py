import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8890"
version_tuple = (0, 0, 8890)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8890")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8778"
data_version_tuple = (0, 0, 8778)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8778")
except ImportError:
    pass
data_git_hash = "f23cf6c309ac37c3270d27c5960e38bf60973ea4"
data_git_describe = "v0.0-8778-gf23cf6c30"
data_git_msg = """\
commit f23cf6c309ac37c3270d27c5960e38bf60973ea4
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Nov 26 10:47:16 2021 +0000

    [rom_ctrl] Mark rom_ctrl as D2
    
    All checklist items are done.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
