import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13150"
version_tuple = (0, 0, 13150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13008"
data_version_tuple = (0, 0, 13008)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13008")
except ImportError:
    pass
data_git_hash = "f0f9dbf27c79145850fbe4352b4682e4c6481b47"
data_git_describe = "v0.0-13008-gf0f9dbf27c"
data_git_msg = """\
commit f0f9dbf27c79145850fbe4352b4682e4c6481b47
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Jul 14 06:12:33 2022 -0400

    [bazel/test_rom] use the dif for the rstmgr in test_rom
    
    Some of the target specific sources are to do with bootstraps but some
    aren't specific anylonger so they were renamed target_test_rom_lib or
    with a specific platform substituted for "target"
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
