import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8723"
version_tuple = (0, 0, 8723)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8723")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8611"
data_version_tuple = (0, 0, 8611)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8611")
except ImportError:
    pass
data_git_hash = "2238c51f8fe92556213a061d19a8c233fe5c666e"
data_git_describe = "v0.0-8611-g2238c51f8"
data_git_msg = """\
commit 2238c51f8fe92556213a061d19a8c233fe5c666e
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Fri Nov 12 17:01:48 2021 +0000

    [sw, tests] Main SRAM exec minor refactor
    
    - Cosmetic changes (kRam..Bytes => kRam..Addr, function comments from
      `/* text */` => `/** text */`)
    - Minor bug fix (addresses are inclusive, so the check whether the
      instruction buffer resides within Main SRAM must include the
      `kRamStartAddr`)
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
