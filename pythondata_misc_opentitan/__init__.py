import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10332"
version_tuple = (0, 0, 10332)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10332")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10206"
data_version_tuple = (0, 0, 10206)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10206")
except ImportError:
    pass
data_git_hash = "48a9fb73f951577cd69421cb1c6ff4c6f53f532b"
data_git_describe = "v0.0-10206-g48a9fb73f"
data_git_msg = """\
commit 48a9fb73f951577cd69421cb1c6ff4c6f53f532b
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Feb 10 22:36:40 2022 -0800

    [dif] Update DIF milestones and descriptions
    
    The DIF milestones were out of date. This commit addresses (and a task
    in #10504).
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
