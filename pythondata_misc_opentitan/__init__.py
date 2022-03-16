import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10908"
version_tuple = (0, 0, 10908)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10908")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10782"
data_version_tuple = (0, 0, 10782)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10782")
except ImportError:
    pass
data_git_hash = "9dddbb0e1a2724578954a30762c18450ef0d4fca"
data_git_describe = "v0.0-10782-g9dddbb0e1"
data_git_msg = """\
commit 9dddbb0e1a2724578954a30762c18450ef0d4fca
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Mar 9 16:20:30 2022 -0800

    [dif/pattgen] Add implementations of all DIFs
    
    This adds implementations (and unittests) of all DIFs for the PATTGEN
    IP.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
