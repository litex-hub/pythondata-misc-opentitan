import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5901"
version_tuple = (0, 0, 5901)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5901")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5806"
data_version_tuple = (0, 0, 5806)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5806")
except ImportError:
    pass
data_git_hash = "0828ce5b7c6b5d32bc33a0e26c1f3c0591bab3d8"
data_git_describe = "v0.0-5806-g0828ce5b7"
data_git_msg = """\
commit 0828ce5b7c6b5d32bc33a0e26c1f3c0591bab3d8
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Apr 15 21:49:44 2021 -0700

    [sw/test] Remove sha256_test
    
    This is now covered by dif_hmac_smoketest.c
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
