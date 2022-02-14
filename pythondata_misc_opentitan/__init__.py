import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10283"
version_tuple = (0, 0, 10283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10157"
data_version_tuple = (0, 0, 10157)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10157")
except ImportError:
    pass
data_git_hash = "ed80fa070e410aeaba10d5858e4689baf9772534"
data_git_describe = "v0.0-10157-ged80fa070"
data_git_msg = """\
commit ed80fa070e410aeaba10d5858e4689baf9772534
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Sun Feb 13 16:46:34 2022 +0000

    [mask_rom] Add support for (but do not enable) hardened shadow stack
    
    This change allows the mask ROM to be built with the hardened shadow
    stack enabled. For the time being the feature needs to be enabled
    manually as only the ROM supports it and it requires a patched LLVM
    toolchain.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
