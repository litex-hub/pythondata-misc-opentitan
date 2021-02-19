import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5059"
version_tuple = (0, 0, 5059)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5059")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4968"
data_version_tuple = (0, 0, 4968)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4968")
except ImportError:
    pass
data_git_hash = "1e7fa2eb509f864e3785c47a73b5d3bad5b2c471"
data_git_describe = "v0.0-4968-g1e7fa2eb5"
data_git_msg = """\
commit 1e7fa2eb509f864e3785c47a73b5d3bad5b2c471
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Thu Feb 18 08:41:37 2021 -0800

    [edn/rtl] added fatal alert signal
    
    Same as CSRNG, with less status bits.
    Re-ran regtool to get up to date.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
