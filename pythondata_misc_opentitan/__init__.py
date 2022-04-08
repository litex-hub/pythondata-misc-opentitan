import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11468"
version_tuple = (0, 0, 11468)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11468")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11342"
data_version_tuple = (0, 0, 11342)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11342")
except ImportError:
    pass
data_git_hash = "b77fb9ff902a70c7e7856ddaf31084ccdaf85e0f"
data_git_describe = "v0.0-11342-gb77fb9ff9"
data_git_msg = """\
commit b77fb9ff902a70c7e7856ddaf31084ccdaf85e0f
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri Mar 25 10:37:34 2022 +0000

    [otbn, dv] Added otbn_illegal_mem_acc testcase and related checkers
    
    This commit adds a new testcase called otbn_illegal_mem_acc and changes
    / additions required to run the test. It also adds a checker to check
    that whenever a mem access is made while the OTBN is busy,
    *mem_rdata_bus pins should be de-asserted.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
