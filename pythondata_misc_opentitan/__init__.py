import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8413"
version_tuple = (0, 0, 8413)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8413")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8301"
data_version_tuple = (0, 0, 8301)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8301")
except ImportError:
    pass
data_git_hash = "4a394963938cae7a7d6eecc33992c465d9c43cb1"
data_git_describe = "v0.0-8301-g4a3949639"
data_git_msg = """\
commit 4a394963938cae7a7d6eecc33992c465d9c43cb1
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Fri Oct 22 14:02:05 2021 +0100

    [mask_rom] Use named offsets when configuring entropy source
    
    Explicitly set the individual fields in the `entropy_src.CONF`
    register. This makes it easier to determine which fields are being
    set and makes the code more robust against future interface changes.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
