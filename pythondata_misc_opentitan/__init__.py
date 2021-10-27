import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8485"
version_tuple = (0, 0, 8485)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8485")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8373"
data_version_tuple = (0, 0, 8373)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8373")
except ImportError:
    pass
data_git_hash = "d55b8c632ccb3a371ac05b5928de5f1f0b2e43b9"
data_git_describe = "v0.0-8373-gd55b8c632"
data_git_msg = """\
commit d55b8c632ccb3a371ac05b5928de5f1f0b2e43b9
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Mon Oct 4 13:16:23 2021 -0400

    [lib] Make hardened.h polyglot
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
