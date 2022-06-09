import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12580"
version_tuple = (0, 0, 12580)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12580")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12438"
data_version_tuple = (0, 0, 12438)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12438")
except ImportError:
    pass
data_git_hash = "ebb94aba30facd52fa9bd34241ca77a2f41fe4a2"
data_git_describe = "v0.0-12438-gebb94aba3"
data_git_msg = """\
commit ebb94aba30facd52fa9bd34241ca77a2f41fe4a2
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Sat Jun 4 23:38:33 2022 +0000

    [top,dv] rv_dm agent update
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
