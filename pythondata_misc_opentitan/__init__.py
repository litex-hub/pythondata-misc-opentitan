import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9339"
version_tuple = (0, 0, 9339)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9339")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9222"
data_version_tuple = (0, 0, 9222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9222")
except ImportError:
    pass
data_git_hash = "c1cf4a8a3d62af1070ecd8777129816bfa604d4a"
data_git_describe = "v0.0-9222-gc1cf4a8a3"
data_git_msg = """\
commit c1cf4a8a3d62af1070ecd8777129816bfa604d4a
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Thu Dec 16 17:47:48 2021 +0000

    [sw,tests] ROM Integrity check in PROD and non-PROD LC States
    
    Checks that the ROM will successfully boot when there is a mismatch of the computed and expected digests in non-production LC state.
    Checks that it will NOT boot when the same mismatch occurs when in production LC state.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
