import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9004"
version_tuple = (0, 0, 9004)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9004")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8892"
data_version_tuple = (0, 0, 8892)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8892")
except ImportError:
    pass
data_git_hash = "af8e8d99f5241befe1ee1d3c6e173218e3fa81a5"
data_git_describe = "v0.0-8892-gaf8e8d99f"
data_git_msg = """\
commit af8e8d99f5241befe1ee1d3c6e173218e3fa81a5
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Dec 2 21:11:58 2021 -0800

    [flash_ctrl] Correctly handle over-write / over-read scenarios.
    
    - Partially addresses #9496
    - The fix at the moment is incomplete.  On software over-reads
      we should really error back.  However, our DV does not currently
      support excluding windows from automated tests.  Until that happens
      make the failure a silent failure, but at least ensure the system
      does not hang.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
