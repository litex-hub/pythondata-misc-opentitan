import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5124"
version_tuple = (0, 0, 5124)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5124")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5033"
data_version_tuple = (0, 0, 5033)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5033")
except ImportError:
    pass
data_git_hash = "b3ed613aeede8d52444ac6a2dbf067d16a922bcf"
data_git_describe = "v0.0-5033-gb3ed613ae"
data_git_msg = """\
commit b3ed613aeede8d52444ac6a2dbf067d16a922bcf
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Feb 23 10:37:13 2021 -0800

    [top] Convert fetch_enable to lc ctrl based
    
    Blocked by #5356 for completion
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
