import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10340"
version_tuple = (0, 0, 10340)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10340")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10214"
data_version_tuple = (0, 0, 10214)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10214")
except ImportError:
    pass
data_git_hash = "87d485a80468a6e64a3267a50cbbf2a4a3d8c259"
data_git_describe = "v0.0-10214-g87d485a80"
data_git_msg = """\
commit 87d485a80468a6e64a3267a50cbbf2a4a3d8c259
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Feb 11 15:18:16 2022 -0800

    [dif/csrng] Update DIF milestones and move to S1
    
    This commit updates the DIF milestones for the CSRNG DIF library to
    reflect the current state of the SW.
    
    This addresses a task in #10504.
    
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
