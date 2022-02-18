import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10439"
version_tuple = (0, 0, 10439)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10439")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10313"
data_version_tuple = (0, 0, 10313)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10313")
except ImportError:
    pass
data_git_hash = "b1855ecc53e3be62f3153219dee2d0cb9a592618"
data_git_describe = "v0.0-10313-gb1855ecc5"
data_git_msg = """\
commit b1855ecc53e3be62f3153219dee2d0cb9a592618
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Fri Feb 18 17:31:30 2022 +0000

    [COMMITTERS] Update committers list
    
    Add Jade Philipoom to the committers list as agreed by the
    technical committee.
    
    Thanks for all your contributions Jade!
    
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
