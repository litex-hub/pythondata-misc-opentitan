import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15050"
version_tuple = (0, 0, 15050)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15050")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14908"
data_version_tuple = (0, 0, 14908)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14908")
except ImportError:
    pass
data_git_hash = "d3cdb0dd5ebe4e5addb53b2e12c34a4695228a14"
data_git_describe = "v0.0-14908-gd3cdb0dd5e"
data_git_msg = """\
commit d3cdb0dd5ebe4e5addb53b2e12c34a4695228a14
Author: Felix Miller <felix@opentitan.org>
Date:   Thu Jul 21 03:18:18 2022 +0200

    [sw,crypto] add SHA-512 implementation for OTBN
    
    Adds a OTBN SHA-512 implementation based on FIPS 180-4. This
    implementation is partially unrolled and favors performance over
    code size.
    
    Signed-off-by: Felix Miller <felix@opentitan.org>

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
