import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12582"
version_tuple = (0, 0, 12582)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12582")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12440"
data_version_tuple = (0, 0, 12440)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12440")
except ImportError:
    pass
data_git_hash = "e1cd49d563e1b26e5b431c4b0c075301d1099891"
data_git_describe = "v0.0-12440-ge1cd49d56"
data_git_msg = """\
commit e1cd49d563e1b26e5b431c4b0c075301d1099891
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue May 17 11:57:52 2022 +0100

    [otbn,rtl] Add predecode checking for control flow related signals
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
