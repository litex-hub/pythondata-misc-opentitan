import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9946"
version_tuple = (0, 0, 9946)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9946")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9822"
data_version_tuple = (0, 0, 9822)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9822")
except ImportError:
    pass
data_git_hash = "e1fe177e2a24d1abaf048c9808e0af9cfdcc8b11"
data_git_describe = "v0.0-9822-ge1fe177e2"
data_git_msg = """\
commit e1fe177e2a24d1abaf048c9808e0af9cfdcc8b11
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jan 31 15:38:22 2022 +0100

    [aes] Use separately buffered copies of lc_escalate_en
    
    This is related to lowRISC/OpenTitan#10422.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
