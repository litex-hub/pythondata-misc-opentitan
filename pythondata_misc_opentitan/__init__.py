import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12239"
version_tuple = (0, 0, 12239)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12239")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12111"
data_version_tuple = (0, 0, 12111)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12111")
except ImportError:
    pass
data_git_hash = "b13d59e4203de523a11e07865b08b018eb0e2e11"
data_git_describe = "v0.0-12111-gb13d59e42"
data_git_msg = """\
commit b13d59e4203de523a11e07865b08b018eb0e2e11
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed May 18 14:52:05 2022 -0400

    [sw/silicon_creator] Store reset reason in ret ram and clear register
    
    Fixes #7887
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
