import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15168"
version_tuple = (0, 0, 15168)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15168")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15026"
data_version_tuple = (0, 0, 15026)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15026")
except ImportError:
    pass
data_git_hash = "78fdfa23c9de6a01c20cf9ee81509eeb20ce4faf"
data_git_describe = "v0.0-15026-g78fdfa23c9"
data_git_msg = """\
commit 78fdfa23c9de6a01c20cf9ee81509eeb20ce4faf
Author: Miles Dai <milesdai@google.com>
Date:   Wed Nov 2 13:58:45 2022 -0400

    [ci] Split FPGA tests into two batches
    
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
