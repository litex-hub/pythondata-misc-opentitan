import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11245"
version_tuple = (0, 0, 11245)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11245")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11119"
data_version_tuple = (0, 0, 11119)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11119")
except ImportError:
    pass
data_git_hash = "0fb66204ea9e5c7b058763f88ac402d71783788d"
data_git_describe = "v0.0-11119-g0fb66204e"
data_git_msg = """\
commit 0fb66204ea9e5c7b058763f88ac402d71783788d
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Mar 22 16:23:13 2022 +0000

    [doc, aes] Update the AES checklist status to S2
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
