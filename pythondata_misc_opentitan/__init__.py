import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5583"
version_tuple = (0, 0, 5583)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5583")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5488"
data_version_tuple = (0, 0, 5488)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5488")
except ImportError:
    pass
data_git_hash = "8f4d13d6b387c0aa5610ede6312dc21385dea265"
data_git_describe = "v0.0-5488-g8f4d13d6b"
data_git_msg = """\
commit 8f4d13d6b387c0aa5610ede6312dc21385dea265
Author: Michael Schaffner <msf@google.com>
Date:   Wed Mar 24 20:17:56 2021 -0700

    [primgen] Minor fix to enable types with underscores
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
