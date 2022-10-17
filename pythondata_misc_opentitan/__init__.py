import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14790"
version_tuple = (0, 0, 14790)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14790")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14648"
data_version_tuple = (0, 0, 14648)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14648")
except ImportError:
    pass
data_git_hash = "d698f0375c7d23919b20826f3cd269f8f7d9bf5d"
data_git_describe = "v0.0-14648-gd698f0375c"
data_git_msg = """\
commit d698f0375c7d23919b20826f3cd269f8f7d9bf5d
Author: Weicai Yang <weicai@google.com>
Date:   Fri Oct 14 17:09:40 2022 -0700

    [spi_device/dv] Update spi_device_driver to collect payload
    
    Updated spi_device_driver to collect payload so that vseq can have the completed
    payload to check.
    
    Thanks Alex for pointing this out.
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
