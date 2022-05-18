import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12216"
version_tuple = (0, 0, 12216)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12216")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12088"
data_version_tuple = (0, 0, 12088)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12088")
except ImportError:
    pass
data_git_hash = "88c679896c52e81e50c21acae287eba6cc5a9851"
data_git_describe = "v0.0-12088-g88c679896"
data_git_msg = """\
commit 88c679896c52e81e50c21acae287eba6cc5a9851
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed May 18 12:46:01 2022 -0400

    [sw/silicon_creator] Change RESET opcode to 0x99
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
