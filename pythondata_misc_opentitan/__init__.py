import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10303"
version_tuple = (0, 0, 10303)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10303")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10177"
data_version_tuple = (0, 0, 10177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10177")
except ImportError:
    pass
data_git_hash = "166d7afd7b8744c72e6d6da7a4456c8574ddfd84"
data_git_describe = "v0.0-10177-g166d7afd7"
data_git_msg = """\
commit 166d7afd7b8744c72e6d6da7a4456c8574ddfd84
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Feb 11 14:48:44 2022 -0800

    [dv/kmac] Add lc_escalation seq
    
    This PR adds lc_escalation seq in DV:
    It randomly issue lc_escalate_en in the middle of a Kmac operation,
    Then check if Kmac is in terminal state.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
