import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9305"
version_tuple = (0, 0, 9305)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9305")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9188"
data_version_tuple = (0, 0, 9188)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9188")
except ImportError:
    pass
data_git_hash = "5493d4bd15d51449b36bbfae37193d9c763665cc"
data_git_describe = "v0.0-9188-g5493d4bd1"
data_git_msg = """\
commit 5493d4bd15d51449b36bbfae37193d9c763665cc
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Dec 24 08:07:47 2021 -0800

    [entropy_src, dv] Restructuring of "rng" vseq
    
    - Implemented scoreboarding for CSRNG bus seeds
    - Added two new processings to RNG test
       - A csrng pull thread
       - A thread for sending CSR commands (which currently holds just some
         placeholder commands, but will hold alert handling in a future PR)
    - Added a new cfg variable "Duration" to control how long the test runs
       - Currently the test runs for 7.5ms
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
