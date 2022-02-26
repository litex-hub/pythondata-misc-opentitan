import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10569"
version_tuple = (0, 0, 10569)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10569")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10443"
data_version_tuple = (0, 0, 10443)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10443")
except ImportError:
    pass
data_git_hash = "e151655e8b335f78051a73b7578715e7caba0e53"
data_git_describe = "v0.0-10443-ge151655e8"
data_git_msg = """\
commit e151655e8b335f78051a73b7578715e7caba0e53
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Feb 24 20:22:02 2022 -0800

    [sw, dv] Minor updates to allow rom copy of ast init
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
