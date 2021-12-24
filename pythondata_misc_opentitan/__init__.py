import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9291"
version_tuple = (0, 0, 9291)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9291")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9174"
data_version_tuple = (0, 0, 9174)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9174")
except ImportError:
    pass
data_git_hash = "da5559c67ae4b0bf1671b33090f82d8bf357c78b"
data_git_describe = "v0.0-9174-gda5559c67"
data_git_msg = """\
commit da5559c67ae4b0bf1671b33090f82d8bf357c78b
Author: Weicai Yang <weicai@google.com>
Date:   Wed Dec 22 17:50:34 2021 -0800

    [sram/dv] clean up scb to remove old backdoor checking
    
    The new backdoor checking was added in #9573, which is pretty stable.
    Now removed the old backdoor checks. No other function change in this
    update.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
