import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10079"
version_tuple = (0, 0, 10079)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10079")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9955"
data_version_tuple = (0, 0, 9955)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9955")
except ImportError:
    pass
data_git_hash = "6d12a3861c6db1caea19277178200077569d3e69"
data_git_describe = "v0.0-9955-g6d12a3861"
data_git_msg = """\
commit 6d12a3861c6db1caea19277178200077569d3e69
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Feb 3 17:18:52 2022 -0800

    [entropy_src] related software updates
    
    - update disable register write
    - update expected values
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
