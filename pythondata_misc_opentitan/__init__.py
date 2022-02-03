import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10023"
version_tuple = (0, 0, 10023)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10023")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9899"
data_version_tuple = (0, 0, 9899)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9899")
except ImportError:
    pass
data_git_hash = "92a3f2450f305af825b2887bb7d64e4a14c9b1dd"
data_git_describe = "v0.0-9899-g92a3f2450"
data_git_msg = """\
commit 92a3f2450f305af825b2887bb7d64e4a14c9b1dd
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Thu Jan 13 14:30:20 2022 +0000

    [flash_ctrl] ADD TEST FOR READ BUFFER EVICTION
    
    Add test for read buffer eviction. All combination read/program/read and
    read/erase/read are exercised. read can be performed by SW or Host
    directly which gives in total 8 scenarios.
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
