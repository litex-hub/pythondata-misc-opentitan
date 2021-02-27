import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5166"
version_tuple = (0, 0, 5166)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5166")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5075"
data_version_tuple = (0, 0, 5075)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5075")
except ImportError:
    pass
data_git_hash = "363f5c1967786a96c59d5c9aa797c7a027f9a306"
data_git_describe = "v0.0-5075-g363f5c196"
data_git_msg = """\
commit 363f5c1967786a96c59d5c9aa797c7a027f9a306
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Feb 25 12:26:52 2021 -0800

    [dv/shadow_reg] Fix aes shadow reg error
    
    This PR support aes shadow reg with the new feature reported in
    PR #4895 :
    AES shadow reg fatal error will lock this register's write access.
    
    This PR updates the testbench regarding this feature:
    1. Add a `shadow_fatal_lock` local variable to indicate if the shadow
    reg is locked due to fatal error.
    2. Temp unlock the `shadow_fatal_lock` if a backdoor write is issued.
    Because tesbench can still update the shadow reg value.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
