import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12466"
version_tuple = (0, 0, 12466)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12466")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12324"
data_version_tuple = (0, 0, 12324)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12324")
except ImportError:
    pass
data_git_hash = "5c1a7171c43ee59120e5b3896f2ca95282056bf3"
data_git_describe = "v0.0-12324-g5c1a7171c"
data_git_msg = """\
commit 5c1a7171c43ee59120e5b3896f2ca95282056bf3
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Jun 1 14:33:24 2022 -0700

    chore(cdc): Waive JTAG EN strap
    
    JTAG en strap can be waived in CDC review
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
