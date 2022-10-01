import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14530"
version_tuple = (0, 0, 14530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14388"
data_version_tuple = (0, 0, 14388)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14388")
except ImportError:
    pass
data_git_hash = "723b8b0d0ac2d5adfc1b352c232487fb1a668f1e"
data_git_describe = "v0.0-14388-g723b8b0d0a"
data_git_msg = """\
commit 723b8b0d0ac2d5adfc1b352c232487fb1a668f1e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Sep 30 18:49:04 2022 +0000

    [dv/kmac] Update masked version exclusion file
    
    This PR updates the masked kmac exclusion file:
    1). Removed previous UNR exclusions because they are based on old RTL
      file.
    2). Add a kmac_masked_terminal_st_excl.el file to exclude transitions
      from some states to terminal states.
      Because these are hard to hit in DV due to sensetive timing, and FPV
      has fully covered it.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
