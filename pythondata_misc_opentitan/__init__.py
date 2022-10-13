import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14735"
version_tuple = (0, 0, 14735)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14735")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14593"
data_version_tuple = (0, 0, 14593)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14593")
except ImportError:
    pass
data_git_hash = "8eb15e17d709a074df24fe91ae2a3ee7c79f6ca3"
data_git_describe = "v0.0-14593-g8eb15e17d7"
data_git_msg = """\
commit 8eb15e17d709a074df24fe91ae2a3ee7c79f6ca3
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Wed Oct 12 17:38:42 2022 +0000

    [flash_ctrl,dv] std_fault covergroup
    
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
