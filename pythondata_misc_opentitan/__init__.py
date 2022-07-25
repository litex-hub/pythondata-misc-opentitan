import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13256"
version_tuple = (0, 0, 13256)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13256")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13114"
data_version_tuple = (0, 0, 13114)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13114")
except ImportError:
    pass
data_git_hash = "6da1e2589ddcc636c3aaef3743daa5e2f2ed44cd"
data_git_describe = "v0.0-13114-g6da1e2589d"
data_git_msg = """\
commit 6da1e2589ddcc636c3aaef3743daa5e2f2ed44cd
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Jul 22 16:28:23 2022 -0400

    [doc] Add caching/splicing info to FPGA ref manual
    
    Add some documentation on bitstream caching and splicing. The FPGA
    reference manual now touches on (a) how CI uploads to the GCS bucket and
    (b) how Bazel generates @bitstreams// targets.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
