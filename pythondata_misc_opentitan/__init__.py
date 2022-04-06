import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11409"
version_tuple = (0, 0, 11409)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11409")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11283"
data_version_tuple = (0, 0, 11283)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11283")
except ImportError:
    pass
data_git_hash = "96e13fe342572922d0c64b382561792d6c9b5b05"
data_git_describe = "v0.0-11283-g96e13fe34"
data_git_msg = """\
commit 96e13fe342572922d0c64b382561792d6c9b5b05
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Oct 27 17:26:32 2021 -0400

    [lib] Add constant-power-hardened mem*() function equivalents
    
    These functions are carefully crafted to traverse buffers in random
    order to thwart traditional power-analysis attacks, making the aggregate
    behavior of calls to this function appear as if their power usage has
    minimal dependency on the input.
    
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
