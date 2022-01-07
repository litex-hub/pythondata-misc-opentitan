import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9388"
version_tuple = (0, 0, 9388)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9388")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9271"
data_version_tuple = (0, 0, 9271)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9271")
except ImportError:
    pass
data_git_hash = "a8f89ad1ed328fde67c0e67d8bb0ca4748033974"
data_git_describe = "v0.0-9271-ga8f89ad1e"
data_git_msg = """\
commit a8f89ad1ed328fde67c0e67d8bb0ca4748033974
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jan 6 22:47:04 2022 -0800

    [sram/dv] add sram_ctrl_regwen_vseq
    
    `ctrl` CSR is excluded in csr tests and it's gated by ctrl_regwen.
    Add this test to verify it
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
