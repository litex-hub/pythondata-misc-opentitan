import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14129"
version_tuple = (0, 0, 14129)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14129")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13987"
data_version_tuple = (0, 0, 13987)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13987")
except ImportError:
    pass
data_git_hash = "28d4235ed758eb8edc988e96a68f82fd0c68bb5f"
data_git_describe = "v0.0-13987-g28d4235ed7"
data_git_msg = """\
commit 28d4235ed758eb8edc988e96a68f82fd0c68bb5f
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Sep 7 11:56:53 2022 -0700

    [dv/kmac] Fix err_code regression error
    
    This PR fixes err_code regression error because we removed the cycle
    accurate model. Now we do not know which sha3 state from design so I
    masked these bits when checking the readout value.
    However, I will create some direct sequence test to make sure design
    reflects the correct error bits regarding the sha3 states.
    
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
