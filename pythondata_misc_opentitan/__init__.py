import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5746"
version_tuple = (0, 0, 5746)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5746")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5651"
data_version_tuple = (0, 0, 5651)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5651")
except ImportError:
    pass
data_git_hash = "8e68433118aa8b335b9a92eb8e9a1e9ff44e49da"
data_git_describe = "v0.0-5651-g8e6843311"
data_git_msg = """\
commit 8e68433118aa8b335b9a92eb8e9a1e9ff44e49da
Author: Felix Miller <felix.miller@gi-de.com>
Date:   Mon Apr 5 12:31:05 2021 +0200

    [otbn] add scalar multiplication for P-384 points
    
    Adds routine and test for scalar multiplication in
    projective space.
    This does not yet contain conversion to affine space
    of the resulting point.
    
    Signed-off-by: Felix Miller <felix.miller@gi-de.com>

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
