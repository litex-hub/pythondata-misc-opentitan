import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14458"
version_tuple = (0, 0, 14458)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14458")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14316"
data_version_tuple = (0, 0, 14316)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14316")
except ImportError:
    pass
data_git_hash = "81dec1a1c64a8048560c501c4dfd184c9872bd4b"
data_git_describe = "v0.0-14316-g81dec1a1c6"
data_git_msg = """\
commit 81dec1a1c64a8048560c501c4dfd184c9872bd4b
Author: Cindy <chencindy@google.com>
Date:   Tue Sep 27 18:10:11 2022 +0000

    [dv/kmac] Enhance lc_escalation test
    
    FSM coverage is low for kmac due to the transaction to lc_escalation
    stage.
    This PR adds more possibility for DUT to issue lc_escalation during kmac
    busy.
    
    Signed-off-by: Cindy <chencindy@google.com>

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
