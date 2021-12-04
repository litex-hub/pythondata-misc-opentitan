import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8996"
version_tuple = (0, 0, 8996)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8996")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8884"
data_version_tuple = (0, 0, 8884)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8884")
except ImportError:
    pass
data_git_hash = "778cad7e1e6c248ff21f0301ec30253c00d62196"
data_git_describe = "v0.0-8884-g778cad7e1"
data_git_msg = """\
commit 778cad7e1e6c248ff21f0301ec30253c00d62196
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Dec 1 12:55:06 2021 -0800

    [dv/lc_tx_t] Simplify mubi4 and lc_tx_t randomization
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
