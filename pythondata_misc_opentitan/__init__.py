import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11452"
version_tuple = (0, 0, 11452)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11452")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11326"
data_version_tuple = (0, 0, 11326)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11326")
except ImportError:
    pass
data_git_hash = "faa725270416aeb5a0de5f28dc2bb37397d443f0"
data_git_describe = "v0.0-11326-gfaa725270"
data_git_msg = """\
commit faa725270416aeb5a0de5f28dc2bb37397d443f0
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Apr 5 10:41:14 2022 -0400

    [sw/silicon_creator] Configure the bootstrap pin only if enabled in OTP
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
