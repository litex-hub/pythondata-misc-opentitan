import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10605"
version_tuple = (0, 0, 10605)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10605")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10479"
data_version_tuple = (0, 0, 10479)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10479")
except ImportError:
    pass
data_git_hash = "c36d777512db6e70c5f230e4c84cea473acd5f73"
data_git_describe = "v0.0-10479-gc36d77751"
data_git_msg = """\
commit c36d777512db6e70c5f230e4c84cea473acd5f73
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 3 12:49:59 2022 +0000

    [otbn,dv] Make sure we're writing bad data in otbn_*mem_err_vseq
    
    This sometimes caused a problem when chaining dmem/imem error
    sequences in a stress sequence. It seems that we were managing to undo
    a previous corruption, leaving some words correct again. Oops!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
