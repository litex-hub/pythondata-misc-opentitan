import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5024"
version_tuple = (0, 0, 5024)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5024")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4933"
data_version_tuple = (0, 0, 4933)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4933")
except ImportError:
    pass
data_git_hash = "9dffa1b320ff70f1fd724a0cfb67f418c6caf437"
data_git_describe = "v0.0-4933-g9dffa1b32"
data_git_msg = """\
commit 9dffa1b320ff70f1fd724a0cfb67f418c6caf437
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Wed Feb 17 11:45:30 2021 +0000

    [reggen] Minor fix to REGWEN error message
    
    Relates to #5267
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
