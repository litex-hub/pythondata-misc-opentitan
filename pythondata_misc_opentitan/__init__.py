import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10852"
version_tuple = (0, 0, 10852)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10852")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10726"
data_version_tuple = (0, 0, 10726)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10726")
except ImportError:
    pass
data_git_hash = "9b93f1bfe4340757eb7a6fb3f2a8e646e64f196f"
data_git_describe = "v0.0-10726-g9b93f1bfe"
data_git_msg = """\
commit 9b93f1bfe4340757eb7a6fb3f2a8e646e64f196f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Mar 11 10:23:02 2022 +0000

    [fpv] Don't import uvm_pkg at global scope
    
    This was causing warnings in the VCS build.
    
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
