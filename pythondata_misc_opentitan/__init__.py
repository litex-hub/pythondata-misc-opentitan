import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10500"
version_tuple = (0, 0, 10500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10374"
data_version_tuple = (0, 0, 10374)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10374")
except ImportError:
    pass
data_git_hash = "e940d67869c5b8386154010f47c3ad70655d3722"
data_git_describe = "v0.0-10374-ge940d6786"
data_git_msg = """\
commit e940d67869c5b8386154010f47c3ad70655d3722
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Tue Feb 22 14:00:41 2022 -0800

    [opentitantool] Remove unused conf structs, and compiler fixes
    
    Fix compiler warning about semicolons in macros, and remove some
    unused declarations from configuration file format.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: I67252086410731d847ef1048084c240939d93a99

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
