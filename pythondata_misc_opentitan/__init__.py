import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15256"
version_tuple = (0, 0, 15256)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15256")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15114"
data_version_tuple = (0, 0, 15114)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15114")
except ImportError:
    pass
data_git_hash = "e1d71da8ad4264c8a2ce329aebffaf855d7be139"
data_git_describe = "v0.0-15114-ge1d71da8ad"
data_git_msg = """\
commit e1d71da8ad4264c8a2ce329aebffaf855d7be139
Author: Jon Flatley <jflat@google.com>
Date:   Wed Nov 2 16:18:35 2022 -0400

    [opentitantool] Output OTP image overlays with hex values
    
    Signed-off-by: Jon Flatley <jflat@google.com>

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
