import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10710"
version_tuple = (0, 0, 10710)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10710")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10584"
data_version_tuple = (0, 0, 10584)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10584")
except ImportError:
    pass
data_git_hash = "75d648378a9d274fe6ef45e172cebc8b0577f15f"
data_git_describe = "v0.0-10584-g75d648378"
data_git_msg = """\
commit 75d648378a9d274fe6ef45e172cebc8b0577f15f
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Mar 2 16:58:47 2022 -0800

    [entropy_src/dv] Properly predict fips_mode signal
    
    RNG single bit mode is not considered FIPS compliant by the DUT.
    
    This commit reflects that in the scoreboard.
    It also includes scoreboard diagnostics to help detect similar errors.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
