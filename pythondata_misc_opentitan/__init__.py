import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5228"
version_tuple = (0, 0, 5228)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5228")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5137"
data_version_tuple = (0, 0, 5137)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5137")
except ImportError:
    pass
data_git_hash = "a6833b1d7165b5543f6bce7d023f305b384cd48f"
data_git_describe = "v0.0-5137-ga6833b1d7"
data_git_msg = """\
commit a6833b1d7165b5543f6bce7d023f305b384cd48f
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 3 14:58:38 2021 -0800

    [top] Correct memory connection bit widths
    
    This solution is not complete, please see #5446
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
