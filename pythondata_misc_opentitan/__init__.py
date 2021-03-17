import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5442"
version_tuple = (0, 0, 5442)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5442")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5347"
data_version_tuple = (0, 0, 5347)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5347")
except ImportError:
    pass
data_git_hash = "4829d28a852c38fe8db7726b6f5343de1556e6e9"
data_git_describe = "v0.0-5347-g4829d28a8"
data_git_msg = """\
commit 4829d28a852c38fe8db7726b6f5343de1556e6e9
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 17 00:18:26 2021 -0700

    [dvsim] Cosmetic updates to launcher methods
    
    - Rearranged APIs to make them uniform
    - Updated `_has_passed()`
      - Renamed to `_check_status()`
      - Returns a tuple as opposed to bool
        - Tuple returned is status, err_msg, where status is "P" or "F"
        - Makes it easy to pick the 'right' error message to report
        especially when there are multiple points of failure in more complex
        launcher system such as LSF
    - _post_finish() now takes err_msg as additional arg to reuse more code
    - LsfLauncher:
      - Renamed some vars / methods
      - Removed the bsub output file existence check since it adds runtime
        overhead and is not needed.
      - Some more cosmetic changes
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
