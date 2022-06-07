import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12562"
version_tuple = (0, 0, 12562)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12562")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12420"
data_version_tuple = (0, 0, 12420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12420")
except ImportError:
    pass
data_git_hash = "2f48edc13fec8fd3787988100028f2ee107e766d"
data_git_describe = "v0.0-12420-g2f48edc13"
data_git_msg = """\
commit 2f48edc13fec8fd3787988100028f2ee107e766d
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jun 7 11:50:00 2022 -0700

    chore(ci): Skip FPGA , SW test for CDC changes
    
    This commit let CI skip FPGA tests, SW tests when only CDC related
    changes are made.
    
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
