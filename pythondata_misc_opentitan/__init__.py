import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11503"
version_tuple = (0, 0, 11503)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11503")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11377"
data_version_tuple = (0, 0, 11377)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11377")
except ImportError:
    pass
data_git_hash = "aea5f3e011eb82013c6bbe6deafc5104448fe3ca"
data_git_describe = "v0.0-11377-gaea5f3e01"
data_git_msg = """\
commit aea5f3e011eb82013c6bbe6deafc5104448fe3ca
Author: Chris Frantz <cfrantz@google.com>
Date:   Fri Apr 8 17:49:30 2022 -0700

    [bazel, mask_rom] Fix build of mask_rom
    
    The mask_rom rule was missing a dependency on
    `//sw/device/silicon_creator/lib/base:static_critical_sec_mmio`.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
