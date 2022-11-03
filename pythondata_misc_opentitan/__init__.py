import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15165"
version_tuple = (0, 0, 15165)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15165")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15023"
data_version_tuple = (0, 0, 15023)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15023")
except ImportError:
    pass
data_git_hash = "d3ed1298de886116adcab66f0c3609fd0dcd9f82"
data_git_describe = "v0.0-15023-gd3ed1298de"
data_git_msg = """\
commit d3ed1298de886116adcab66f0c3609fd0dcd9f82
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Nov 2 19:05:31 2022 -0700

    [top-test] Update flash_ctrl_test buffer sizes
    
    Update buffer sizes to cover the entire page based on
    `flash_info.bytes_per_page`.
    
    Fixes #10848.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
