import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5853"
version_tuple = (0, 0, 5853)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5853")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5758"
data_version_tuple = (0, 0, 5758)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5758")
except ImportError:
    pass
data_git_hash = "fe1494799fbafaece75e0ea2d7e20d129e11bcfa"
data_git_describe = "v0.0-5758-gfe1494799"
data_git_msg = """\
commit fe1494799fbafaece75e0ea2d7e20d129e11bcfa
Author: Udi Jonnalagadda <udij@google.com>
Date:   Mon Apr 12 17:13:21 2021 -0700

    [dv/cip_lib] create `cip_tl_host_single_seq`
    
    this PR creates a custom extension of `tl_host_single_seq` to allow for
    full flexibility in creating cmd integrity related test sequences, and
    adds basic functionality to swap between TL access types (DataType or
    InstrType).
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
