import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8975"
version_tuple = (0, 0, 8975)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8975")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8863"
data_version_tuple = (0, 0, 8863)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8863")
except ImportError:
    pass
data_git_hash = "caeb0b7ea2966dadbaa60357e045ff64d68e8c72"
data_git_describe = "v0.0-8863-gcaeb0b7ea"
data_git_msg = """\
commit caeb0b7ea2966dadbaa60357e045ff64d68e8c72
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 30 17:47:10 2021 -0800

    [flash_ctrl] Various documentation update
    
    - fixes #9205
    
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
