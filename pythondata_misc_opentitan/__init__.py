import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5653"
version_tuple = (0, 0, 5653)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5653")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5558"
data_version_tuple = (0, 0, 5558)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5558")
except ImportError:
    pass
data_git_hash = "34f334fb211b04e7fabce1ae7b42f5ef1cf6ad58"
data_git_describe = "v0.0-5558-g34f334fb2"
data_git_msg = """\
commit 34f334fb211b04e7fabce1ae7b42f5ef1cf6ad58
Author: Udi Jonnalagadda <udij@google.com>
Date:   Thu Mar 25 17:01:55 2021 -0700

    [dv/kmac] rework prefix calculation to fix #5755
    
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
