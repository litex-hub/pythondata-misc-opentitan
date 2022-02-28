import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10593"
version_tuple = (0, 0, 10593)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10593")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10467"
data_version_tuple = (0, 0, 10467)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10467")
except ImportError:
    pass
data_git_hash = "9ea6c5e2ba297e113a221b4d7c0c7cbfd3c1a22f"
data_git_describe = "v0.0-10467-g9ea6c5e2b"
data_git_msg = """\
commit 9ea6c5e2ba297e113a221b4d7c0c7cbfd3c1a22f
Author: Michael Schaffner <msf@google.com>
Date:   Fri Feb 25 17:52:36 2022 +0000

    [tlul_sram_byte] Fix width mismatch
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
