import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5686"
version_tuple = (0, 0, 5686)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5686")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5591"
data_version_tuple = (0, 0, 5591)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5591")
except ImportError:
    pass
data_git_hash = "5bf75e9351e9eef509a967f80eb3e37015cc9ca0"
data_git_describe = "v0.0-5591-g5bf75e935"
data_git_msg = """\
commit 5bf75e9351e9eef509a967f80eb3e37015cc9ca0
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Mar 31 11:33:08 2021 -0700

    [sw/dif] CSRNG Initial Implementation
    
    This commits adds the following dif_csrng functions:
    
    *   `dif_csrng_init()`
    *   `dif_csrng_configure()`
    *   `dif_csrng_get_cmd_interface()`
    *   `dif_csrng_get_output_status()`
    
    Added unittest and smoketest boilerplate.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
