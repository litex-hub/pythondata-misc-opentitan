import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11526"
version_tuple = (0, 0, 11526)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11526")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11400"
data_version_tuple = (0, 0, 11400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11400")
except ImportError:
    pass
data_git_hash = "5a50bfe4e2267ba1656cb18470b12f18b136c6ee"
data_git_describe = "v0.0-11400-g5a50bfe4e"
data_git_msg = """\
commit 5a50bfe4e2267ba1656cb18470b12f18b136c6ee
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri Apr 8 13:20:25 2022 +0100

    [otbn, dv] Added a test to escalate software error to fatal errors
    
    This commit adds a new testcase called otbn_sw_errs_fatal_chk. This test
    sets the software_errs_fatal bit in ctrl register to escalate software
    errors to fatal errors.
    
    This commit also adds required functions to set software_errs_fatal flag
    in ISS model and if this bit is set in the model, the model goes to
    locked state.
    
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
