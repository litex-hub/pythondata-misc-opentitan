import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10137"
version_tuple = (0, 0, 10137)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10137")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10013"
data_version_tuple = (0, 0, 10013)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10013")
except ImportError:
    pass
data_git_hash = "9ba75ebe576524fcf1cf0228947db70bdddd0df1"
data_git_describe = "v0.0-10013-g9ba75ebe5"
data_git_msg = """\
commit 9ba75ebe576524fcf1cf0228947db70bdddd0df1
Author: Alphan Ulusoy <alphan@google.com>
Date:   Fri Feb 4 13:07:52 2022 -0500

    [sw/silicon_creator] Harden boot_data read functions
    
    This change slightly simplifies and hardens
    `boot_data_page_info_update_impl()` along with other functions in the
    boot_data read path by adding hardened checks for `rom_error_t` and
    `hardened_bool_t` values and loop counters.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
