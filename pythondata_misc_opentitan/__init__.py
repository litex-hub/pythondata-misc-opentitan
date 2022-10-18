import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14799"
version_tuple = (0, 0, 14799)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14799")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14657"
data_version_tuple = (0, 0, 14657)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14657")
except ImportError:
    pass
data_git_hash = "202b67e8eb8de3ae5d24e191bbcf903f96918c89"
data_git_describe = "v0.0-14657-g202b67e8eb"
data_git_msg = """\
commit 202b67e8eb8de3ae5d24e191bbcf903f96918c89
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Sat Oct 15 16:19:49 2022 +0000

    [flash_ctrl,dv] filesystem_support test fix
    
    - Add address redundency check to guarantee singgle bit error injection
    - Assert error to tb ref mem when singble error is asserted to rtl.
    
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
