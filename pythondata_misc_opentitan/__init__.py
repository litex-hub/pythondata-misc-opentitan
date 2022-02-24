import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10510"
version_tuple = (0, 0, 10510)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10510")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10384"
data_version_tuple = (0, 0, 10384)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10384")
except ImportError:
    pass
data_git_hash = "c34153e9f90e44bda2e8644a5242d219a0a0b6be"
data_git_describe = "v0.0-10384-gc34153e9f"
data_git_msg = """\
commit c34153e9f90e44bda2e8644a5242d219a0a0b6be
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Feb 21 14:46:00 2022 +0100

    [aes] Make IV register readable for software
    
    This is required to support IV save/restore flows in the software
    implementation of the crypto library.
    
    This is related to lowRISC/OpenTitan#10532.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
