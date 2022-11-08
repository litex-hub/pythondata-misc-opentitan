import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15331"
version_tuple = (0, 0, 15331)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15331")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15189"
data_version_tuple = (0, 0, 15189)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15189")
except ImportError:
    pass
data_git_hash = "ce22188696373f4f1712624f08ced2b489b80b30"
data_git_describe = "v0.0-15189-gce22188696"
data_git_msg = """\
commit ce22188696373f4f1712624f08ced2b489b80b30
Author: James Wainwright <james.wainwright@lowrisc.org>
Date:   Mon Oct 31 17:31:51 2022 +0000

    [sw/silicon_creator] Add test cases for otbn_copy_data_{to,from}_otbn
    
    These functions are just wrappers around `otbn_{write,read}_data`, so
    these new tests were modified from those functions' tests.
    
    Signed-off-by: James Wainwright <james.wainwright@lowrisc.org>

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
