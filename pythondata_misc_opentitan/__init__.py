import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9521"
version_tuple = (0, 0, 9521)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9521")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9399"
data_version_tuple = (0, 0, 9399)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9399")
except ImportError:
    pass
data_git_hash = "4a6f457f4306dec5149a8fa5c67f8d1faf5e5139"
data_git_describe = "v0.0-9399-g4a6f457f4"
data_git_msg = """\
commit 4a6f457f4306dec5149a8fa5c67f8d1faf5e5139
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jan 12 21:56:29 2022 -0800

    [dv/clkmgr] Add measurement saturation and fix timeout
    
    Add code to set the measurement cnt to a high value to test counter
    saturation.
    Fix measurement timeout test to stop the clock after the measurements
    start to make sure the CSRs are updated, and to expect all io derived
    clocks to timeout when the primary io clock is stopped.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
