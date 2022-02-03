import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10021"
version_tuple = (0, 0, 10021)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10021")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9897"
data_version_tuple = (0, 0, 9897)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9897")
except ImportError:
    pass
data_git_hash = "b1f413bf2d4424925cb18116749bb5d1f37562a1"
data_git_describe = "v0.0-9897-gb1f413bf2"
data_git_msg = """\
commit b1f413bf2d4424925cb18116749bb5d1f37562a1
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 1 14:53:03 2022 -0800

    [rstmgr] Prepare D2S counetermeasure items
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    [rstmgr] Prepare d2s countermeasures
    
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
