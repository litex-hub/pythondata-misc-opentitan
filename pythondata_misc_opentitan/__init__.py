import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12568"
version_tuple = (0, 0, 12568)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12568")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12426"
data_version_tuple = (0, 0, 12426)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12426")
except ImportError:
    pass
data_git_hash = "fdd3b8c5bae60cd9c998f79140632639c74e1dc1"
data_git_describe = "v0.0-12426-gfdd3b8c5b"
data_git_msg = """\
commit fdd3b8c5bae60cd9c998f79140632639c74e1dc1
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jun 7 15:18:48 2022 -0700

    fix(otp_ctrl): Keymgr Key valid glitch
    
    This PR fixes the CDC issue on otp_keymgr_key_t.valid signal. Also
    there's chance the key_share0, key_share1 can be changed during the
    operation but the chance is limited to the escalation stage, in which
    case the CDC is not meaningful anymore.
    
    So rather than latching the key_shares, this commit adds assertion to
    check the stability of the key_shares during the normal operation.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
