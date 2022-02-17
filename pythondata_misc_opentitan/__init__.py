import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10403"
version_tuple = (0, 0, 10403)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10403")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10277"
data_version_tuple = (0, 0, 10277)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10277")
except ImportError:
    pass
data_git_hash = "dcf148872e2ce013d33b8fba51a8c33dedd1fca9"
data_git_describe = "v0.0-10277-gdcf148872"
data_git_msg = """\
commit dcf148872e2ce013d33b8fba51a8c33dedd1fca9
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Feb 10 12:31:53 2022 -0800

    [top] Update relevant core files to use alternate pmp reset values
    
    - add alternate pmp reset file
    
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
