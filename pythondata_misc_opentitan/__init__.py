import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5800"
version_tuple = (0, 0, 5800)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5800")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5705"
data_version_tuple = (0, 0, 5705)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5705")
except ImportError:
    pass
data_git_hash = "e1bc36198309dcbe9a993d7cc4067a1011deb455"
data_git_describe = "v0.0-5705-ge1bc36198"
data_git_msg = """\
commit e1bc36198309dcbe9a993d7cc4067a1011deb455
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Apr 8 13:00:14 2021 +0100

    [edn,lint] Fix width mismatch in the definition of cmd_sent
    
    cmd_fifo_cnt_q is actually 4 bits wide in the current design. The
    mismatch between that and 13'h01 causes Verilator width warnings.
    
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
