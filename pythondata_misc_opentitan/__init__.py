import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12485"
version_tuple = (0, 0, 12485)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12485")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12343"
data_version_tuple = (0, 0, 12343)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12343")
except ImportError:
    pass
data_git_hash = "c941279301af2774f8d64120e31466a55669ed25"
data_git_describe = "v0.0-12343-gc94127930"
data_git_msg = """\
commit c941279301af2774f8d64120e31466a55669ed25
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 1 14:19:15 2022 -0700

    [pwrmgr] Fix escalate request CDC
    
    - addresses #12981
    - If the escalate request is not permanent, it is possible
      for the pwrmgr to miss this request since it goes through
      an always-on clock synchronization.
    - capture and hold escalate request until the system resets.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
