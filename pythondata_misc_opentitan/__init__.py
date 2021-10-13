import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8238"
version_tuple = (0, 0, 8238)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8238")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8126"
data_version_tuple = (0, 0, 8126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8126")
except ImportError:
    pass
data_git_hash = "2428d66c0c389435b31bf06e190931454efb00dd"
data_git_describe = "v0.0-8126-g2428d66c0"
data_git_msg = """\
commit 2428d66c0c389435b31bf06e190931454efb00dd
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Oct 13 14:02:50 2021 +0100

    [otbn,dv] Remove unused static set_rnd_data in otbn_model.cc
    
    This has been unused since 5480504 (which switched to passing 32 bits
    at a time).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
