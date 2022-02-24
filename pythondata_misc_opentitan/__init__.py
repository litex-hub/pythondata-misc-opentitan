import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10513"
version_tuple = (0, 0, 10513)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10513")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10387"
data_version_tuple = (0, 0, 10387)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10387")
except ImportError:
    pass
data_git_hash = "4efcabef8b88e2eec9560e5700fbfb322100c97e"
data_git_describe = "v0.0-10387-g4efcabef8"
data_git_msg = """\
commit 4efcabef8b88e2eec9560e5700fbfb322100c97e
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Feb 22 09:08:35 2022 -0800

    [aes/dv] enable masking
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
