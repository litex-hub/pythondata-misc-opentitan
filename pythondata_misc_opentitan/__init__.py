import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5739"
version_tuple = (0, 0, 5739)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5739")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5644"
data_version_tuple = (0, 0, 5644)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5644")
except ImportError:
    pass
data_git_hash = "12841fcca27cdfa68c62eeee834793ad4a120795"
data_git_describe = "v0.0-5644-g12841fcca"
data_git_msg = """\
commit 12841fcca27cdfa68c62eeee834793ad4a120795
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 22 10:25:15 2021 +0000

    [flash_ctrl,lint] Fix width errors for parameters in flash_ctrl_pkg
    
    Most of these changes are pretty mechanical, silencing Verilator
    warnings by making casts explicit.
    
    The only non-trivial change is in flash_ctrl_info_cfg.sv, where a
    page_addr_t structure (normally used for addressing pages within a
    data partition) is used to address pages in an info partition. This
    means that the "CurPage" index needs expanding from InfoPageW to
    PageW. In practice, Info partitions are no bigger than data
    partitions, so this should be fine, but we also add a comment and an
    ASSERT_INIT to make sure this holds.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
