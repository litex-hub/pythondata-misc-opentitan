import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5657"
version_tuple = (0, 0, 5657)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5657")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5562"
data_version_tuple = (0, 0, 5562)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5562")
except ImportError:
    pass
data_git_hash = "df7aa7163d1642f4d0029a6d3217259974c5c957"
data_git_describe = "v0.0-5562-gdf7aa7163"
data_git_msg = """\
commit df7aa7163d1642f4d0029a6d3217259974c5c957
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Sat Mar 27 17:25:14 2021 -0700

    [sw/dif] Entropy source implementation
    
    Implement the following function calls:
    
    *   `dif_entropy_init()`
    *   `dif_entropy_configure()`
    *   `dif_entropy_read()`
    
    Add the following test targets:
    
    *   `dif_entropy_unittest`
    *   `dif_entropy_smoketest`
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
