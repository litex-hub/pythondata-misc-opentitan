import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5575"
version_tuple = (0, 0, 5575)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5575")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5480"
data_version_tuple = (0, 0, 5480)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5480")
except ImportError:
    pass
data_git_hash = "abd74ca59e5387d905fc60501dd905647d1bbc12"
data_git_describe = "v0.0-5480-gabd74ca59"
data_git_msg = """\
commit abd74ca59e5387d905fc60501dd905647d1bbc12
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 23 18:36:11 2021 -0700

    [spi] Remove a few lint errors to clean-up output
    
    - tie off unused from spi host
    - temporarily remove combo loop in spi device
    - changes to case inside usage
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
