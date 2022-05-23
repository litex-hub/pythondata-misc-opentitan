import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12283"
version_tuple = (0, 0, 12283)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12283")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12155"
data_version_tuple = (0, 0, 12155)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12155")
except ImportError:
    pass
data_git_hash = "114e7fc41855b27bba91d966dfedf300afc8470a"
data_git_describe = "v0.0-12155-g114e7fc41"
data_git_msg = """\
commit 114e7fc41855b27bba91d966dfedf300afc8470a
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri May 20 16:32:35 2022 -0700

    [fpv/rstmgr] Fix FPV compile error
    
    This PR fixes rstmgr FPV sec_cm compile error.
    The sva core file cannot include any UVM components, so we moved the
    mubi coverage bind to rstmgr/dv/cov/ folder.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
