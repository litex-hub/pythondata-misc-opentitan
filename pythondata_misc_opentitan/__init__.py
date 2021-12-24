import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9289"
version_tuple = (0, 0, 9289)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9289")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9172"
data_version_tuple = (0, 0, 9172)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9172")
except ImportError:
    pass
data_git_hash = "94308f5e5e4bc44b419463ec65ed91a577820790"
data_git_describe = "v0.0-9172-g94308f5e5"
data_git_msg = """\
commit 94308f5e5e4bc44b419463ec65ed91a577820790
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Dec 22 17:14:43 2021 -0800

    [dv/pwrmgr] Add more checking into scoreboard
    
    Predict the interrupt.
    Add interrupt coverage.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
