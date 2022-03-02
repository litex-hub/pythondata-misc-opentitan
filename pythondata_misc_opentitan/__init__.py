import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10633"
version_tuple = (0, 0, 10633)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10633")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10507"
data_version_tuple = (0, 0, 10507)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10507")
except ImportError:
    pass
data_git_hash = "36fe734974502c11b8cbcdbd43d8da9a489f800d"
data_git_describe = "v0.0-10507-g36fe73497"
data_git_msg = """\
commit 36fe734974502c11b8cbcdbd43d8da9a489f800d
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Feb 17 12:24:17 2022 -0800

    [adc_ctrl] Various fixes to better conform to spec
    
    - fixes #10779
    - fixes #10843
    
    - filter status updates and filterinterrupt generation are done only on a match change
    - de-couple interrupt generation from filter status
    - update interrupt control to only latch interrupt status when enabled
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
