import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8174"
version_tuple = (0, 0, 8174)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8174")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8062"
data_version_tuple = (0, 0, 8062)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8062")
except ImportError:
    pass
data_git_hash = "fc115292a65bd8a2f8bc60ea1efb6004c9b007a0"
data_git_describe = "v0.0-8062-gfc115292a"
data_git_msg = """\
commit fc115292a65bd8a2f8bc60ea1efb6004c9b007a0
Author: Michael Schaffner <msf@google.com>
Date:   Fri Oct 1 16:41:30 2021 -0700

    [ast] Ast lint fixes and waiver file update
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
