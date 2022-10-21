import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14873"
version_tuple = (0, 0, 14873)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14873")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14731"
data_version_tuple = (0, 0, 14731)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14731")
except ImportError:
    pass
data_git_hash = "7d9b5775cb6c9de18e13a9b6b2be73051f25d658"
data_git_describe = "v0.0-14731-g7d9b5775cb"
data_git_msg = """\
commit 7d9b5775cb6c9de18e13a9b6b2be73051f25d658
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Oct 20 12:01:17 2022 +0100

    [otbn,rtl] Latch various internal state errors
    
    FPV has revealed it was possible for some internal state errors to be
    ignored, so no alert was triggered, if they occurred the same cycle or
    the cycle before a start command was issues to OTBN. This was due to
    some errors only appearing for a single cycle and others getting reset
    by the start command.
    
    This adds latching behaviour to various internal errors, so once seen
    they will remain asserted until reset.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
