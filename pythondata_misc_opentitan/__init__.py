import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10151"
version_tuple = (0, 0, 10151)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10151")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10027"
data_version_tuple = (0, 0, 10027)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10027")
except ImportError:
    pass
data_git_hash = "cdc4bd4c821fce7a32367ee7450358d0f9a7f0d2"
data_git_describe = "v0.0-10027-gcdc4bd4c8"
data_git_msg = """\
commit cdc4bd4c821fce7a32367ee7450358d0f9a7f0d2
Author: Timothy Trippel <ttrippel@google.com>
Date:   Sun Feb 6 22:33:21 2022 -0800

    [sw/test_rom] Add AST init to test ROM
    
    This commit adds the blind-data-copy initialization code to the test ROM
    to enable testing the AST in chip-level tests.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
