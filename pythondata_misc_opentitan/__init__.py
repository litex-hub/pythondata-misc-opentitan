import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14424"
version_tuple = (0, 0, 14424)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14424")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14282"
data_version_tuple = (0, 0, 14282)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14282")
except ImportError:
    pass
data_git_hash = "9559b249c741b8e2302cf278c0d4efbd108d9d6e"
data_git_describe = "v0.0-14282-g9559b249c7"
data_git_msg = """\
commit 9559b249c741b8e2302cf278c0d4efbd108d9d6e
Author: Eli Kim <eli@opentitan.org>
Date:   Sat Sep 24 04:05:27 2022 +0000

    fix(bazel): Bazel airgapped environment
    
    PR #15044 did not update bazel airgap environment prep script.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
