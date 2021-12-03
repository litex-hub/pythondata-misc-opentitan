import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8987"
version_tuple = (0, 0, 8987)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8987")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8875"
data_version_tuple = (0, 0, 8875)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8875")
except ImportError:
    pass
data_git_hash = "3fdc7395d36a3c3b07614b5ea6e1a54794b4952e"
data_git_describe = "v0.0-8875-g3fdc7395d"
data_git_msg = """\
commit 3fdc7395d36a3c3b07614b5ea6e1a54794b4952e
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Dec 3 06:46:24 2021 -0800

    [entropy_src/doc] uninstantiate command update
    
    The documentation has been updated to restrict the clen of an uninstantiate command to be zero.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
