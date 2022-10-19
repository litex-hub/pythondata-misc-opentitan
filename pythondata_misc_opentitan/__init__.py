import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14841"
version_tuple = (0, 0, 14841)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14841")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14699"
data_version_tuple = (0, 0, 14699)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14699")
except ImportError:
    pass
data_git_hash = "84835838da2d38b72e97d48949f36d54efdfa3e7"
data_git_describe = "v0.0-14699-g84835838da"
data_git_msg = """\
commit 84835838da2d38b72e97d48949f36d54efdfa3e7
Author: Fatih Balli <fatihballi@google.com>
Date:   Wed Oct 5 15:42:32 2022 +0200

    [chip_sw, kmac_entropy] Checking timeout of EDN inside KMAC
    
    Implements chip_sw_kmac_entropy test.
    
    This commit also updates necessary KMAC DIF functions used within this
    test. Respective KMAC unittests are also updated accordingly.
    
    Signed-off-by: Fatih Balli <fatihballi@google.com>

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
