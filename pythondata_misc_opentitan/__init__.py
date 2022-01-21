import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9698"
version_tuple = (0, 0, 9698)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9698")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9576"
data_version_tuple = (0, 0, 9576)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9576")
except ImportError:
    pass
data_git_hash = "8eac7c0264862cc4f9a92ee522fe753d9b543cbf"
data_git_describe = "v0.0-9576-g8eac7c026"
data_git_msg = """\
commit 8eac7c0264862cc4f9a92ee522fe753d9b543cbf
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Thu Jan 20 16:41:23 2022 -0500

    [sw/silicon_creator] Add hardened assembly routine for redundant checks
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
