import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15047"
version_tuple = (0, 0, 15047)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15047")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14905"
data_version_tuple = (0, 0, 14905)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14905")
except ImportError:
    pass
data_git_hash = "3f88b0938fc839b6c3d4b153b04072b6d1d9029b"
data_git_describe = "v0.0-14905-g3f88b0938f"
data_git_msg = """\
commit 3f88b0938fc839b6c3d4b153b04072b6d1d9029b
Author: Weicai Yang <weicai@google.com>
Date:   Sun Oct 30 21:50:54 2022 -0700

    [spi_device/dv] Fix a constraint error
    
    Recent constraint update affected the direct test - read_buffer_direct
    Changed to call a uvm_reg_field randomize instead of vseq randomize,
    since this direct test doesn't need to the complex constraint in base_vseq.
    
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
