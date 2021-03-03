import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5208"
version_tuple = (0, 0, 5208)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5208")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5117"
data_version_tuple = (0, 0, 5117)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5117")
except ImportError:
    pass
data_git_hash = "03bcc2f0975e0748ce46e6b21c85415dedb0c688"
data_git_describe = "v0.0-5117-g03bcc2f09"
data_git_msg = """\
commit 03bcc2f0975e0748ce46e6b21c85415dedb0c688
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 1 15:13:25 2021 -0800

    [dv/jtag] Fix two small jtag issue
    
    These PR fixes two small issues in jtag:
    1. Add a clock cycle delay in between clock_en and drive_tms.
       This is to make sure the clock is stable before driving any signals.
    2. Fix a port declaration from output to ref.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
