import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8611"
version_tuple = (0, 0, 8611)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8611")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8499"
data_version_tuple = (0, 0, 8499)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8499")
except ImportError:
    pass
data_git_hash = "ae4a31f9fa20ee80875cb9582678c93f449d5102"
data_git_describe = "v0.0-8499-gae4a31f9f"
data_git_msg = """\
commit ae4a31f9fa20ee80875cb9582678c93f449d5102
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Nov 3 15:13:48 2021 -0700

    [edn/rtl] prim counter replacing standard counter
    
    A counter used to track long generate commands has been replaced with the hardened version.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
