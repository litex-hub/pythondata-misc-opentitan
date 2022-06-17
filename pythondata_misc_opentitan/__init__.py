import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12730"
version_tuple = (0, 0, 12730)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12730")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12588"
data_version_tuple = (0, 0, 12588)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12588")
except ImportError:
    pass
data_git_hash = "7de3ae517a990d6e1714779c5cb38e1b0dc35388"
data_git_describe = "v0.0-12588-g7de3ae517"
data_git_msg = """\
commit 7de3ae517a990d6e1714779c5cb38e1b0dc35388
Author: Hugo McNally <hugo.mcnally@gmail.com>
Date:   Fri Jun 17 12:46:28 2022 +0100

    [dif, hmac] add unit test dif_hmac_get_message_length
    
    Signed-off-by: Hugo McNally <hugo.mcnally@gmail.com>

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
