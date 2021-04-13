import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5845"
version_tuple = (0, 0, 5845)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5845")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5750"
data_version_tuple = (0, 0, 5750)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5750")
except ImportError:
    pass
data_git_hash = "f8b33d6e46fbc8024c37e64f02ecb6d08be5b192"
data_git_describe = "v0.0-5750-gf8b33d6e4"
data_git_msg = """\
commit f8b33d6e46fbc8024c37e64f02ecb6d08be5b192
Author: Felix Miller <felix.miller@gi-de.com>
Date:   Thu Apr 8 13:53:04 2021 +0200

    [otbn] add coordinate transformation for P-384
    
    Adds a routine for coordinate transformation from
    projective space to affine space for P-384 curve
    points.
    Enables back transformation of coordinates at
    the end of the scalar multiplication routine.
    
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
