import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12397"
version_tuple = (0, 0, 12397)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12397")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12257"
data_version_tuple = (0, 0, 12257)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12257")
except ImportError:
    pass
data_git_hash = "439ddcf9450545673e7d9e4b1ec977491676f8aa"
data_git_describe = "v0.0-12257-g439ddcf94"
data_git_msg = """\
commit 439ddcf9450545673e7d9e4b1ec977491676f8aa
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Apr 16 15:38:01 2022 -0700

    [entropy_src/dv] Implement CGs for seed output
    
     -Implements seed_output_hw_cg and fw_ov_output_cg
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
