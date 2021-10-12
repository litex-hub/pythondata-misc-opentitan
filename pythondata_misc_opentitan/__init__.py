import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8218"
version_tuple = (0, 0, 8218)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8218")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8106"
data_version_tuple = (0, 0, 8106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8106")
except ImportError:
    pass
data_git_hash = "6e4471149f57a94946b8d8412a49f90c76184b87"
data_git_describe = "v0.0-8106-g6e4471149"
data_git_msg = """\
commit 6e4471149f57a94946b8d8412a49f90c76184b87
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Mon Oct 11 12:07:33 2021 -0700

    [sw/rom] Remove generic otbn modexp subroutine.
    
    Leave only modexp_65537 to save on flash space.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
