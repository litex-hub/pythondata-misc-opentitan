import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11433"
version_tuple = (0, 0, 11433)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11433")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11307"
data_version_tuple = (0, 0, 11307)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11307")
except ImportError:
    pass
data_git_hash = "944fb14cbe71149448dbb58a6d3e2f0cf43d6b00"
data_git_describe = "v0.0-11307-g944fb14cb"
data_git_msg = """\
commit 944fb14cbe71149448dbb58a6d3e2f0cf43d6b00
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Thu Apr 7 11:22:51 2022 +0100

    [otbn, dv] Fixed regression issue in otbn_stress_all_with_rand_reset
    
    If a reset is asserted when elf file is getting loaded, the sequence
    waits for reset to get de-asserted before executing run_otbn task.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
