import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5907"
version_tuple = (0, 0, 5907)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5907")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5812"
data_version_tuple = (0, 0, 5812)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5812")
except ImportError:
    pass
data_git_hash = "e489c4a7ee47909576f8840f75ae490ff69f996e"
data_git_describe = "v0.0-5812-ge489c4a7e"
data_git_msg = """\
commit e489c4a7ee47909576f8840f75ae490ff69f996e
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Apr 15 12:08:01 2021 -0700

    [tools] simple instructions for interactive synth
    
    - The steps are still pretty manual and not ideal, but at least we can do it for now.
    - Long term it may be good to have this built directly into dvsim with some kind of -interactive command.
    
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
