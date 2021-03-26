import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5600"
version_tuple = (0, 0, 5600)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5600")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5505"
data_version_tuple = (0, 0, 5505)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5505")
except ImportError:
    pass
data_git_hash = "b506aa33a6db353d73f2a98e24604c4ce6381558"
data_git_describe = "v0.0-5505-gb506aa33a"
data_git_msg = """\
commit b506aa33a6db353d73f2a98e24604c4ce6381558
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Mar 25 15:04:54 2021 -0700

    [csnrg/rtl] remove incorrect TODO
    
    The TODO says that the GEN command does not update working state, but it does.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
