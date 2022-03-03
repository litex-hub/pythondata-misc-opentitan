import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10688"
version_tuple = (0, 0, 10688)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10688")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10562"
data_version_tuple = (0, 0, 10562)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10562")
except ImportError:
    pass
data_git_hash = "2c374e07cb5af04dc16ae8cb0fc0ad56eade4949"
data_git_describe = "v0.0-10562-g2c374e07c"
data_git_msg = """\
commit 2c374e07cb5af04dc16ae8cb0fc0ad56eade4949
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Mar 2 23:46:05 2022 -0800

    [sw/runtime] Fix ibex_timeout_check
    
    The return value should match the function documentation.
    Fix the IBEX_SPIN_FOR macro to match.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
