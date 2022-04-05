import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11375"
version_tuple = (0, 0, 11375)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11375")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11249"
data_version_tuple = (0, 0, 11249)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11249")
except ImportError:
    pass
data_git_hash = "e8be89f08c47cbd2934bad19decdd0f75a4823b2"
data_git_describe = "v0.0-11249-ge8be89f08"
data_git_msg = """\
commit e8be89f08c47cbd2934bad19decdd0f75a4823b2
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Fri Apr 1 08:38:07 2022 +0200

    [otbn] Add FSM-related CM labels
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
