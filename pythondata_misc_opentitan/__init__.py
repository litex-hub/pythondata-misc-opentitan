import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14194"
version_tuple = (0, 0, 14194)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14194")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14052"
data_version_tuple = (0, 0, 14052)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14052")
except ImportError:
    pass
data_git_hash = "d4641339ed703904120639d1504804fb725535ce"
data_git_describe = "v0.0-14052-gd4641339ed"
data_git_msg = """\
commit d4641339ed703904120639d1504804fb725535ce
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Wed Sep 14 05:46:30 2022 +0000

    [flash_ctrl/dv] Sign off V2
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
