import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8375"
version_tuple = (0, 0, 8375)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8375")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8263"
data_version_tuple = (0, 0, 8263)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8263")
except ImportError:
    pass
data_git_hash = "ca82314d866d4f0e41243081d30c958ed6a4dad8"
data_git_describe = "v0.0-8263-gca82314d8"
data_git_msg = """\
commit ca82314d866d4f0e41243081d30c958ed6a4dad8
Author: Tomasz Gorochowik <tgorochowik@antmicro.com>
Date:   Tue Oct 19 13:54:46 2021 +0200

    Setup verible-linter github action
    
    Signed-off-by: Tomasz Gorochowik <tgorochowik@antmicro.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
