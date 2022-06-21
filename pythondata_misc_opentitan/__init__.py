import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12758"
version_tuple = (0, 0, 12758)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12758")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12616"
data_version_tuple = (0, 0, 12616)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12616")
except ImportError:
    pass
data_git_hash = "6cb41fe6d2d4cdcc941ca54c2f5e478e6a111869"
data_git_describe = "v0.0-12616-g6cb41fe6d2"
data_git_msg = """\
commit 6cb41fe6d2d4cdcc941ca54c2f5e478e6a111869
Author: Guillermo Maturana <maturana@google.com>
Date:   Sat Jun 18 05:40:30 2022 -0700

    [dv,chip] Format time in microseconds
    
    Format time in microseconds losing no precision. The added "." makes it
    easier to  determine the order of magnitude without counting digits, as
    is needed if it was formatted as ps or ns.
    
    For example, time would be represented as "  333.333333 us" instead of
    "   333333333 ps".
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
