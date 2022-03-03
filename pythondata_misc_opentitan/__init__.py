import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10692"
version_tuple = (0, 0, 10692)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10692")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10566"
data_version_tuple = (0, 0, 10566)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10566")
except ImportError:
    pass
data_git_hash = "c50edd875c6d1e8de623a6029ca3d0b11af770a1"
data_git_describe = "v0.0-10566-gc50edd875"
data_git_msg = """\
commit c50edd875c6d1e8de623a6029ca3d0b11af770a1
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 3 17:05:34 2022 +0000

    [keymgr] OR together signals differently to avoid Xcelium warnings
    
    The previous syntax triggered the "DUPBWO" warning ("error prone
    bit-wise OR sequence detected"). Using |{a, b} instead of "|a | |b"
    silences the warning and is maybe a bit easier to understand anyway.
    
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
