import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11319"
version_tuple = (0, 0, 11319)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11319")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11193"
data_version_tuple = (0, 0, 11193)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11193")
except ImportError:
    pass
data_git_hash = "0dc541c1eb0195818bbc1c1251778d74ffe01edf"
data_git_describe = "v0.0-11193-g0dc541c1e"
data_git_msg = """\
commit 0dc541c1eb0195818bbc1c1251778d74ffe01edf
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 1 11:37:27 2022 +0100

    [dvsim,xcelium] Avoid an OPTP2ND error if a plusarg isn't set
    
    This is needed to get e.g. the prim_present_test testbench working
    with Xcelium.
    
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
