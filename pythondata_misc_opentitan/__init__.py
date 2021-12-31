import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9308"
version_tuple = (0, 0, 9308)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9308")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9191"
data_version_tuple = (0, 0, 9191)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9191")
except ImportError:
    pass
data_git_hash = "bf6f6d15ba147ea7b0d95ff5b7cbca0789172e7c"
data_git_describe = "v0.0-9191-gbf6f6d15b"
data_git_msg = """\
commit bf6f6d15ba147ea7b0d95ff5b7cbca0789172e7c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Dec 30 11:50:02 2021 -0800

    [fpv/pinmux] Sleep mode and dio related assertions
    
    This PR adds sleep mode assertions and DIO assertions.
    A few failures filed an issue #9850 to clarify.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
