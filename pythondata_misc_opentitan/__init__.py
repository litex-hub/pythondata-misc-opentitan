import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5473"
version_tuple = (0, 0, 5473)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5473")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5378"
data_version_tuple = (0, 0, 5378)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5378")
except ImportError:
    pass
data_git_hash = "4769007560230561c3575147d4c3cbbc59aa3626"
data_git_describe = "v0.0-5378-g476900756"
data_git_msg = """\
commit 4769007560230561c3575147d4c3cbbc59aa3626
Author: Udi Jonnalagadda <udij@google.com>
Date:   Mon Mar 15 16:07:06 2021 -0700

    [dv/kmac] add mem_tests to nightly regression
    
    this PR adds the mem_tests to the nightly KMAC regression,
    and temporarily removes stress_tests as it is not ready.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
