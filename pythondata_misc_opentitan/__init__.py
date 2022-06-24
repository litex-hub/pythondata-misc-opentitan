import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12835"
version_tuple = (0, 0, 12835)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12835")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12693"
data_version_tuple = (0, 0, 12693)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12693")
except ImportError:
    pass
data_git_hash = "aac02b4e727be002c40c4b7c07f04e3cd1ee43a8"
data_git_describe = "v0.0-12693-gaac02b4e72"
data_git_msg = """\
commit aac02b4e727be002c40c4b7c07f04e3cd1ee43a8
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 22 23:27:31 2022 -0700

    [top] Correct xbar reset connections
    
    - fixes #13354
    - isolate the xbar reset from the individual end-point resets
    - scripting updates required to allow for different resets
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
