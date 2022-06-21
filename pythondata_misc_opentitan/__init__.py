import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12742"
version_tuple = (0, 0, 12742)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12742")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12600"
data_version_tuple = (0, 0, 12600)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12600")
except ImportError:
    pass
data_git_hash = "9cc70b8f98fbac0ae61254463ab4d19cff982d70"
data_git_describe = "v0.0-12600-g9cc70b8f98"
data_git_msg = """\
commit 9cc70b8f98fbac0ae61254463ab4d19cff982d70
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Fri May 27 15:37:24 2022 +0100

    [otbn, dv] Fixed regression issue in otbn_illegal_mem_acc
    
    This commit disables compare check that happens in the memory model
    whenever an illegal access is done to the imem / dmem while the otbn is
    busy executing instructions.
    
    it also disables end address check inside run_otbn task.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
