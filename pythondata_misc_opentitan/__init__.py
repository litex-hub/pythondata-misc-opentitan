import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11268"
version_tuple = (0, 0, 11268)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11268")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11142"
data_version_tuple = (0, 0, 11142)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11142")
except ImportError:
    pass
data_git_hash = "51d9ddd8188fa4ce8d66543d28ca5dda1b7dde56"
data_git_describe = "v0.0-11142-g51d9ddd81"
data_git_msg = """\
commit 51d9ddd8188fa4ce8d66543d28ca5dda1b7dde56
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Mar 28 11:51:47 2022 +0200

    [kmac/pre_syn] Enable Yosys synthesis of full SHA3 core or entire KMAC
    
    Previously, we were only able to synthesize keccak_2share or
    keccak_round, i.e., the core modules to formally analyze the masking
    using Alma.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
