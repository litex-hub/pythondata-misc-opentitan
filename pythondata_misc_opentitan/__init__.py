import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11542"
version_tuple = (0, 0, 11542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11416"
data_version_tuple = (0, 0, 11416)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11416")
except ImportError:
    pass
data_git_hash = "c3279dce64edb3c2507ea992f1756055c5080b77"
data_git_describe = "v0.0-11416-gc3279dce6"
data_git_msg = """\
commit c3279dce64edb3c2507ea992f1756055c5080b77
Author: Alexander Williams <awill@google.com>
Date:   Tue Apr 12 16:11:39 2022 -0700

    [build] Fix up test_rom / flash_ctrl deps
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
