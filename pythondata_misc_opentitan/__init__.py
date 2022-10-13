import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14722"
version_tuple = (0, 0, 14722)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14722")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14580"
data_version_tuple = (0, 0, 14580)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14580")
except ImportError:
    pass
data_git_hash = "bc758e2cd2b1624a22370dbe1acdff701ad9fc91"
data_git_describe = "v0.0-14580-gbc758e2cd2"
data_git_msg = """\
commit bc758e2cd2b1624a22370dbe1acdff701ad9fc91
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Oct 12 16:18:41 2022 -0700

    [top-test] xref csrng_lc_hw_debug_en to test point
    
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
