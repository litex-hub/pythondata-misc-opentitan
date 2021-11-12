import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8706"
version_tuple = (0, 0, 8706)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8706")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8594"
data_version_tuple = (0, 0, 8594)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8594")
except ImportError:
    pass
data_git_hash = "0310540ed5e4e25c3b695db326027726ff5b434f"
data_git_describe = "v0.0-8594-g0310540ed"
data_git_msg = """\
commit 0310540ed5e4e25c3b695db326027726ff5b434f
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Nov 4 09:50:04 2021 +0000

    [sw] Add message encoding to RSA-3072 interface.
    
    This will allow us to implement a more typical verification interface,
    and easily run test vectors that haven't pre-encoded the message.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
