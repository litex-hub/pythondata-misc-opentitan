import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10919"
version_tuple = (0, 0, 10919)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10919")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10793"
data_version_tuple = (0, 0, 10793)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10793")
except ImportError:
    pass
data_git_hash = "2d9bfa749da6e11ef64bc95173906654d2cd2b36"
data_git_describe = "v0.0-10793-g2d9bfa749"
data_git_msg = """\
commit 2d9bfa749da6e11ef64bc95173906654d2cd2b36
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Tue Mar 15 11:51:39 2022 -0400

    [lib] Don't make anything in lib depend on the base:base rule
    
    This excludes a couple of deprecated targets that aren't worth fixing.
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
