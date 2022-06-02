import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12457"
version_tuple = (0, 0, 12457)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12457")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12315"
data_version_tuple = (0, 0, 12315)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12315")
except ImportError:
    pass
data_git_hash = "1b4293480568f9bb6ac97836fff952f1e6c63fba"
data_git_describe = "v0.0-12315-g1b4293480"
data_git_msg = """\
commit 1b4293480568f9bb6ac97836fff952f1e6c63fba
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jun 1 13:44:54 2022 -0700

    [dv/pattgen] Remove memory testplan entry
    
    This PR removes testplan entries regarding memory. Pattgen does not
    contain any memory so this test is not needed.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
