import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14188"
version_tuple = (0, 0, 14188)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14188")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14046"
data_version_tuple = (0, 0, 14046)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14046")
except ImportError:
    pass
data_git_hash = "1b4bb0e07f0304747a3014471170a1ca83ed9a58"
data_git_describe = "v0.0-14046-g1b4bb0e07f"
data_git_msg = """\
commit 1b4bb0e07f0304747a3014471170a1ca83ed9a58
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Aug 30 13:46:07 2022 +0200

    [sw,otbn] Add Bazel targets for the OTBN simulator.
    
    Create Bazel targets for the OTBN simulator and its dependencies and use
    the new targets in the OTBN simulator test rule.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
