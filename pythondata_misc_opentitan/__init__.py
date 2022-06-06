import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12519"
version_tuple = (0, 0, 12519)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12519")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12377"
data_version_tuple = (0, 0, 12377)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12377")
except ImportError:
    pass
data_git_hash = "84089a286e5a599103642002d6e5bb9748e5c2b6"
data_git_describe = "v0.0-12377-g84089a286"
data_git_msg = """\
commit 84089a286e5a599103642002d6e5bb9748e5c2b6
Author: Miles Dai <milesdai@google.com>
Date:   Mon Jun 6 11:52:45 2022 -0400

    [ci,sw/silicon_creator] Temporarily disable keymgr_functest on fpga
    
    Merging #12912 broke
    //sw/device/silicon_creator/lib/drivers:keymgr_functest_fpga_cw310. This
    commit temporarily disables that test until #13045 can fix it.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
