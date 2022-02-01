import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9967"
version_tuple = (0, 0, 9967)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9967")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9843"
data_version_tuple = (0, 0, 9843)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9843")
except ImportError:
    pass
data_git_hash = "c02272adbfb16b67e53b93082b4fb8dec5e29858"
data_git_describe = "v0.0-9843-gc02272adb"
data_git_msg = """\
commit c02272adbfb16b67e53b93082b4fb8dec5e29858
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jan 31 14:35:00 2022 -0800

    [dv/kmac] fifo empty interrupt behavior
    
    This PR aligns a fifo empty interrupt related behavior:
    If the read and write pointers are equal, and next clock cycle a write
    is issued and accepted, the fifo empty interrupt won't fire.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
