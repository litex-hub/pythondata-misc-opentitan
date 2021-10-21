import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8369"
version_tuple = (0, 0, 8369)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8369")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8257"
data_version_tuple = (0, 0, 8257)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8257")
except ImportError:
    pass
data_git_hash = "bf7faa427a5adf377a4245ad4689be831021934a"
data_git_describe = "v0.0-8257-gbf7faa427"
data_git_msg = """\
commit bf7faa427a5adf377a4245ad4689be831021934a
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Oct 19 22:22:19 2021 -0700

    [dvsim] Enabling glob-style patterns for -i switch
    
    This commit enables the user to pass glob-style patterns instead of
    fully resolved test/regression names to `-i|--items` switch.
    
    The following are some examples:
    - Run all CSR tests: `-i *csr*`
    - Run all sleep tests: `-i chip_sw_sleep*`
    
    As before, it matches the input patterns with the list of available
    regrssions first. For example, `-i *smoke*` will add all tests enabled
    for the smoke regressions AND then, it will add all tests containing the
    pattern `*smoke*` in the name that are not added to the smoke
    regression. If multiple regressions match the input patterns, and there
    is an overlap of tests, then the subsequent regressions are dropped with
    a warning message. If an input pattern does not match any available
    regression or test name, then a warning is thrown.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
