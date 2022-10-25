import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14931"
version_tuple = (0, 0, 14931)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14931")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14789"
data_version_tuple = (0, 0, 14789)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14789")
except ImportError:
    pass
data_git_hash = "7a7139c8af345f423ac27a0186febdda027f7127"
data_git_describe = "v0.0-14789-g7a7139c8af"
data_git_msg = """\
commit 7a7139c8af345f423ac27a0186febdda027f7127
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 24 15:38:17 2022 -0700

    [spi_device/dv] Add connectivity test for ram_cfg
    
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
