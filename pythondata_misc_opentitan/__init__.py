import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14863"
version_tuple = (0, 0, 14863)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14863")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14721"
data_version_tuple = (0, 0, 14721)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14721")
except ImportError:
    pass
data_git_hash = "dd9e2b7d9b12ac6c1e79cb613f73bd74cb15334e"
data_git_describe = "v0.0-14721-gdd9e2b7d9b"
data_git_msg = """\
commit dd9e2b7d9b12ac6c1e79cb613f73bd74cb15334e
Author: Weicai Yang <weicai@google.com>
Date:   Wed Oct 19 22:00:24 2022 -0700

    [spi_device/dv] Change to SW only update addr_4b after reset
    
    Due to #15543
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
