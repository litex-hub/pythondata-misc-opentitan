import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14924"
version_tuple = (0, 0, 14924)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14924")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14782"
data_version_tuple = (0, 0, 14782)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14782")
except ImportError:
    pass
data_git_hash = "d0f667d861f326466299fdcf7ce9e06b3bd0bba1"
data_git_describe = "v0.0-14782-gd0f667d861"
data_git_msg = """\
commit d0f667d861f326466299fdcf7ce9e06b3bd0bba1
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 24 13:04:54 2022 -0700

    [spi_device/dv] Fix some coverage issues
    
    1. fixed wrong variable type int -> bit
    2. fixed dummy_cycles cross, as write doesn't allow dummy_cycles
    3. reduced auto_bin to reduce cross coverage
    4. adjusted randomization to increase chance for swap data/addr
    
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
