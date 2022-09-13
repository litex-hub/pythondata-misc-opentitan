import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14171"
version_tuple = (0, 0, 14171)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14171")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14029"
data_version_tuple = (0, 0, 14029)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14029")
except ImportError:
    pass
data_git_hash = "e954fe0aacaef634327bed411e42a224e8093633"
data_git_describe = "v0.0-14029-ge954fe0aac"
data_git_msg = """\
commit e954fe0aacaef634327bed411e42a224e8093633
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Jul 20 11:13:29 2022 +0100

    [crypto, test] Test timing properties of AES-GCM decryption.
    
    Add a test that checks if AES-GCM decryption is constant-time relative
    to different invalid tags. This helps ensure that an attacker cannot get
    information about how much of the tag they've guessed correctly.
    
    As part of this change, refactor AES-GCM testing so that utilities can
    be imported by multiple files.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
