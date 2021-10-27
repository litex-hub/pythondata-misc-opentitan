import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8479"
version_tuple = (0, 0, 8479)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8479")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8367"
data_version_tuple = (0, 0, 8367)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8367")
except ImportError:
    pass
data_git_hash = "5adfa4eea91d66503220e29dd3b4e92faba83871"
data_git_describe = "v0.0-8367-g5adfa4eea"
data_git_msg = """\
commit 5adfa4eea91d66503220e29dd3b4e92faba83871
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Oct 20 12:57:50 2021 -0700

    [util, top] Correct top level ast reset mapping
    
    - Also fix a minor issue in `merge.py` that added
      unnecessary domains to resets.
    
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
