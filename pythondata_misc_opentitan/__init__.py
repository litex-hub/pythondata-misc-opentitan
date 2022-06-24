import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12832"
version_tuple = (0, 0, 12832)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12832")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12690"
data_version_tuple = (0, 0, 12690)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12690")
except ImportError:
    pass
data_git_hash = "2bd39248e4d9716740417886199c38a6138b01c5"
data_git_describe = "v0.0-12690-g2bd39248e4"
data_git_msg = """\
commit 2bd39248e4d9716740417886199c38a6138b01c5
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jun 24 14:32:38 2022 +0200

    [otbn/doc] Clarify the expected behavior around RND_REP/FIPS_CHK_FAIL
    
    These are both recoverable errors that are only triggered when OTBN
    uses the random numbers during program execution by reading RND
    register and not when the entropy is received from EDN.
    
    This resolves lowRISC/OpenTitan#13325.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
