import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9520"
version_tuple = (0, 0, 9520)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9520")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9398"
data_version_tuple = (0, 0, 9398)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9398")
except ImportError:
    pass
data_git_hash = "2745275cae4897ed59a9e4e2bcd534590b3352a9"
data_git_describe = "v0.0-9398-g2745275ca"
data_git_msg = """\
commit 2745275cae4897ed59a9e4e2bcd534590b3352a9
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sun Jan 9 13:07:15 2022 -0800

    [fpv/pinmux] Update pinmux doc for V1 requirements
    
    This PR updates the pinmux doc for V1.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
