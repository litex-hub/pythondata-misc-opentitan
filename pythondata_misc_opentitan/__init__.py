import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11323"
version_tuple = (0, 0, 11323)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11323")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11197"
data_version_tuple = (0, 0, 11197)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11197")
except ImportError:
    pass
data_git_hash = "55dc90392e74ed7e1666bf07de32a094660f062e"
data_git_describe = "v0.0-11197-g55dc90392"
data_git_msg = """\
commit 55dc90392e74ed7e1666bf07de32a094660f062e
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Wed Mar 30 04:09:06 2022 -0700

    [aes/dv] added read check for IV
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
