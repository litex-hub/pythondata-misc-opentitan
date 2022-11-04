import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15220"
version_tuple = (0, 0, 15220)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15220")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15078"
data_version_tuple = (0, 0, 15078)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15078")
except ImportError:
    pass
data_git_hash = "4ba05ff98f96030f3f4497127942e264c3aae102"
data_git_describe = "v0.0-15078-g4ba05ff98f"
data_git_msg = """\
commit 4ba05ff98f96030f3f4497127942e264c3aae102
Author: Dan McArdle <dmcardle@google.com>
Date:   Thu Nov 3 10:39:15 2022 -0400

    [doc] Add udev instructions for ARM-USB-TINY-H JTAG adapter
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
