import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12737"
version_tuple = (0, 0, 12737)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12737")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12595"
data_version_tuple = (0, 0, 12595)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12595")
except ImportError:
    pass
data_git_hash = "69f0bbe00785ccc409b51919205204ffc02b5113"
data_git_describe = "v0.0-12595-g69f0bbe007"
data_git_msg = """\
commit 69f0bbe00785ccc409b51919205204ffc02b5113
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 15 17:44:40 2022 -0700

    [rv_core_ibex] Update to latest crash dump
    
    Addresses some of the usability issues discovered in #12908
    dependent on lowRISC/ibex#1680
    
    The crash dump is now more representative of where the first and second exceptions occurred.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
