import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9608"
version_tuple = (0, 0, 9608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9486"
data_version_tuple = (0, 0, 9486)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9486")
except ImportError:
    pass
data_git_hash = "bf6c7513e86976b6a6f36792300a173c6819daaa"
data_git_describe = "v0.0-9486-gbf6c7513e"
data_git_msg = """\
commit bf6c7513e86976b6a6f36792300a173c6819daaa
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jan 13 10:41:47 2022 -0800

    [flash_ctrl] prep work for flash exec value update
    
    - Address #10022 with a 32-bit constant value
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
