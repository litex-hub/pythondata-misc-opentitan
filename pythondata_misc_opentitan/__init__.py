import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8398"
version_tuple = (0, 0, 8398)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8398")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8286"
data_version_tuple = (0, 0, 8286)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8286")
except ImportError:
    pass
data_git_hash = "d88e2dd0bcff264e3c7c42f2939efcb62d15577b"
data_git_describe = "v0.0-8286-gd88e2dd0b"
data_git_msg = """\
commit d88e2dd0bcff264e3c7c42f2939efcb62d15577b
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Oct 8 13:35:39 2021 -0700

    [dv/full chip] Update chip testplan
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
