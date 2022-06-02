import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12475"
version_tuple = (0, 0, 12475)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12475")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12333"
data_version_tuple = (0, 0, 12333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12333")
except ImportError:
    pass
data_git_hash = "0eae0e92ad47b62739a82a7b184356d00a99eaeb"
data_git_describe = "v0.0-12333-g0eae0e92a"
data_git_msg = """\
commit 0eae0e92ad47b62739a82a7b184356d00a99eaeb
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jun 1 22:35:54 2022 -0700

    [dv] Update tl_intg sequence
    
    1. Changed to only trigger one intg_error at a time, rather than
       triggering intg_error at all TL interfaces at a time. One intg_error
       should lead to a fatal alert.
    2. added `check_no_fatal_alerts` after testing passthru_mem_tl_intg_err
       since no fata alert should occur
    3. small cleanup - moved `num_times` to the main task
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
