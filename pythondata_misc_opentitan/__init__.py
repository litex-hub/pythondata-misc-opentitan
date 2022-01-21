import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9694"
version_tuple = (0, 0, 9694)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9694")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9572"
data_version_tuple = (0, 0, 9572)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9572")
except ImportError:
    pass
data_git_hash = "fe0aaec7f6129549cc4797def5bf519b6728a477"
data_git_describe = "v0.0-9572-gfe0aaec7f"
data_git_msg = """\
commit fe0aaec7f6129549cc4797def5bf519b6728a477
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jan 20 21:45:04 2022 -0800

    [dv/pwrmgr] Stimulate the rom inputs
    
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
