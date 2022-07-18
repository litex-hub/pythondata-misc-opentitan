import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13143"
version_tuple = (0, 0, 13143)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13143")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13001"
data_version_tuple = (0, 0, 13001)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13001")
except ImportError:
    pass
data_git_hash = "1445e264f27eb6b8eef3925a4411ae0f157cdd6d"
data_git_describe = "v0.0-13001-g1445e264f2"
data_git_msg = """\
commit 1445e264f27eb6b8eef3925a4411ae0f157cdd6d
Author: Sven Bauer <sven.bauer@gi-de.com>
Date:   Fri Jul 15 11:40:38 2022 +0200

    [otbn] otbn_build.py: Improve readability.
    
    Signed-off-by: Sven Bauer <sven.bauer@gi-de.com>

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
