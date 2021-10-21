import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8379"
version_tuple = (0, 0, 8379)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8379")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8267"
data_version_tuple = (0, 0, 8267)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8267")
except ImportError:
    pass
data_git_hash = "d726f959ed37eadc2fc4a6a8747350a8c66157a6"
data_git_describe = "v0.0-8267-gd726f959e"
data_git_msg = """\
commit d726f959ed37eadc2fc4a6a8747350a8c66157a6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Oct 20 17:50:53 2021 +0100

    [otbn,dv] Add otbn_imem_err to the "core" regression
    
    These sequences are the intended to be the ones that run code and we
    forgot to add otbn_imem_err when defining it.
    
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
