import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11256"
version_tuple = (0, 0, 11256)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11256")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11130"
data_version_tuple = (0, 0, 11130)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11130")
except ImportError:
    pass
data_git_hash = "3219d9c63bcd0040b49e664d789efe8021d287df"
data_git_describe = "v0.0-11130-g3219d9c63"
data_git_msg = """\
commit 3219d9c63bcd0040b49e664d789efe8021d287df
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 31 07:49:30 2022 -0700

    [lc_ctrl] change the assert construction for clarity
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
