import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14500"
version_tuple = (0, 0, 14500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14358"
data_version_tuple = (0, 0, 14358)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14358")
except ImportError:
    pass
data_git_hash = "a0241d1446c5de6b99eef5cbc5081c22ca63af24"
data_git_describe = "v0.0-14358-ga0241d1446"
data_git_msg = """\
commit a0241d1446c5de6b99eef5cbc5081c22ca63af24
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Sep 28 16:57:24 2022 -0400

    [sw/silicon_creator] Use asm to avoid SP usage in ROM exception handler
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
