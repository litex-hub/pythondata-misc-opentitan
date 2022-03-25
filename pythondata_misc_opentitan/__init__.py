import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11128"
version_tuple = (0, 0, 11128)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11128")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11002"
data_version_tuple = (0, 0, 11002)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11002")
except ImportError:
    pass
data_git_hash = "e9c6fcce94aa3fae40ecd5388710abd1720c7fc5"
data_git_describe = "v0.0-11002-ge9c6fcce9"
data_git_msg = """\
commit e9c6fcce94aa3fae40ecd5388710abd1720c7fc5
Author: Timothy Trippel <ttrippel@google.com>
Date:   Thu Mar 24 15:54:17 2022 -0700

    [bazel] add python rules and register python toolchain
    
    Currently, Python scripts are referenced across our repository as bazel
    files/filegroups, rather than using actualy Python bazel rules.
    Moreover, our current bazel configuration did not enforce hermiticity
    w.r.t. a python toolchain or packages. By adding Python rules and
    registering a toolchain, makes hermetic Python builds possible.
    
    This fixes #11683.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
