import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12738"
version_tuple = (0, 0, 12738)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12738")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12596"
data_version_tuple = (0, 0, 12596)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12596")
except ImportError:
    pass
data_git_hash = "a3562f8e2fbdecda849bb8a2d29f150ec3b21472"
data_git_describe = "v0.0-12596-ga3562f8e2f"
data_git_msg = """\
commit a3562f8e2fbdecda849bb8a2d29f150ec3b21472
Author: Drew Macrae <drewmacrae@google.com>
Date:   Fri Jun 17 16:08:09 2022 -0400

    [bazel/ci] mark e2e mask rom test flaky for better ci runs
    
    also rerun the test when it stochastically fails.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
