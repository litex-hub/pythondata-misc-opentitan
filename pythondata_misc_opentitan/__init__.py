import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15021"
version_tuple = (0, 0, 15021)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15021")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14879"
data_version_tuple = (0, 0, 14879)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14879")
except ImportError:
    pass
data_git_hash = "f0c0618b6773655d0ebb32c07cd37d0ca587c14e"
data_git_describe = "v0.0-14879-gf0c0618b67"
data_git_msg = """\
commit f0c0618b6773655d0ebb32c07cd37d0ca587c14e
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Oct 27 18:39:35 2022 -0700

    [top-test] refactor otbn_randomness tests
    
    Move OTBN random test into a separate library so that it can be reused
    in other tests.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
