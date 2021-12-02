import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8953"
version_tuple = (0, 0, 8953)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8953")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8841"
data_version_tuple = (0, 0, 8841)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8841")
except ImportError:
    pass
data_git_hash = "e3370ba2a7720aba763040013856c374d8395b4b"
data_git_describe = "v0.0-8841-ge3370ba2a"
data_git_msg = """\
commit e3370ba2a7720aba763040013856c374d8395b4b
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Nov 24 10:09:52 2021 +0000

    [rom_ctrl, dv] Fix for rom_ctrl_tl_errors regression failures
    
    Following changes are made in this commit:
    1. cip_base_vseq__tl_errors: Dafault sequencer has been removed in
    create_tl_access_error_case as it introduced unwanted bugs by running on
    default sequencer.
    tl_write_ro_mem_err is made to run on corresponding RAL model's
    sequencer
    2. rom_ctrl_scoreboard: If an invalid address is picked, the scoreboard
    is taught not to generate errors.
    
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
