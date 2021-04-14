import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5866"
version_tuple = (0, 0, 5866)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5866")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5771"
data_version_tuple = (0, 0, 5771)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5771")
except ImportError:
    pass
data_git_hash = "cc5e3e02b6321423daa5c578aa3cd77ff6fce57b"
data_git_describe = "v0.0-5771-gcc5e3e02b"
data_git_msg = """\
commit cc5e3e02b6321423daa5c578aa3cd77ff6fce57b
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Apr 8 16:07:29 2021 -0700

    [dv/sram] check sram initialization in scb
    
    this PR adds support for checking `CTRL.init`in the scoreboard,
    using a simple timing model to do so.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
