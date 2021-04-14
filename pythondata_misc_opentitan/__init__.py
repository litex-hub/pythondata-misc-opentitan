import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5860"
version_tuple = (0, 0, 5860)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5860")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5765"
data_version_tuple = (0, 0, 5765)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5765")
except ImportError:
    pass
data_git_hash = "76caf9ac8c8b4a416422f75c3317e0fbf6cf1a7f"
data_git_describe = "v0.0-5765-g76caf9ac8"
data_git_msg = """\
commit 76caf9ac8c8b4a416422f75c3317e0fbf6cf1a7f
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Apr 8 14:04:15 2021 -0700

    [dv/dvsim] Adds failure bucketizer for triage.
    
    Changes _post_finish to take an ErrorMessage as second argument.
    Moves class SimCfg's Results to its own file and renames it to SimResults.
    The bucketizer is called when initializing SimResults.
    This will change when reruns are implemented, since we would want to
    rerun one test per bucket as soon as the failing test completes.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
