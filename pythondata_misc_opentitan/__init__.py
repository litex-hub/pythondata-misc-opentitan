import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8923"
version_tuple = (0, 0, 8923)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8923")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8811"
data_version_tuple = (0, 0, 8811)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8811")
except ImportError:
    pass
data_git_hash = "40b607b776d7b10cfc2899cc0d724d00dc0c91a2"
data_git_describe = "v0.0-8811-g40b607b77"
data_git_msg = """\
commit 40b607b776d7b10cfc2899cc0d724d00dc0c91a2
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Mon Nov 29 12:48:19 2021 +0000

    [dv] Fix for rom_ctrl_tl_intg_err regression failure
    
    Following fixes have been made in this commit:
    1. reset is done after run_tl_intg_err_vseq task finishes for both ral
    models. Earlier, reset was asserted after the shortest task ended.
    2. tl_access in issue_tl_access_w_intg_err is made to run on respective
    ral model's sequencer. Earlier it was running only on default sequencer
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
