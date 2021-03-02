import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5195"
version_tuple = (0, 0, 5195)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5195")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5104"
data_version_tuple = (0, 0, 5104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5104")
except ImportError:
    pass
data_git_hash = "1db6fcd8f909543a08a67bf6c354898be258612d"
data_git_describe = "v0.0-5104-g1db6fcd8f"
data_git_msg = """\
commit 1db6fcd8f909543a08a67bf6c354898be258612d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 11 14:56:20 2021 +0000

    [reggen] Define a class to represent the registers in a block
    
    This is used to represent obj['registers'], which was previously a
    list of registers, multiregs, windows, reserved and skipto entries.
    The commit doesn't replace the top-level object (obj).
    
    Other than removing genwennames and gennextoffset from (h)json export,
    the only other change is that we no longer distinguish between
    reserved and skipto, which means we have to pick one format or the
    other on export. This commit picks reserved (because it is more
    "relocatable"), but skipto could work instead.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
