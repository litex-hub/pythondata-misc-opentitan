import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12553"
version_tuple = (0, 0, 12553)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12553")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12411"
data_version_tuple = (0, 0, 12411)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12411")
except ImportError:
    pass
data_git_hash = "de0e5b0a507dc10cf712bdb0bbbf7cd0e0c1bfbf"
data_git_describe = "v0.0-12411-gde0e5b0a5"
data_git_msg = """\
commit de0e5b0a507dc10cf712bdb0bbbf7cd0e0c1bfbf
Author: Miles Dai <milesdai@google.com>
Date:   Mon Jun 6 17:33:08 2022 -0400

    [ci] Fixup to #13046 to include the full set of fpga systemtests.
    
    PR #13046 missed some tests that were originally included in systemtest.
    This commit adds them back. Note that some tests were included in
    systemtest but are failing when run on Bazel. These were not included.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
