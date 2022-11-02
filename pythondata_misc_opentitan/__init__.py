import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15120"
version_tuple = (0, 0, 15120)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15120")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14978"
data_version_tuple = (0, 0, 14978)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14978")
except ImportError:
    pass
data_git_hash = "e1671fddf58976e5e11db41cd51fa17de54dea14"
data_git_describe = "v0.0-14978-ge1671fddf5"
data_git_msg = """\
commit e1671fddf58976e5e11db41cd51fa17de54dea14
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Nov 1 16:01:20 2022 -0700

    [dv/csrng_agent] Add csrng_agent cov
    
    This PR adds some coverage for CSRNG agent.
    It includes coverage for cmd and genbits.
    
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
