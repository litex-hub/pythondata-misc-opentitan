import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9578"
version_tuple = (0, 0, 9578)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9578")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9456"
data_version_tuple = (0, 0, 9456)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9456")
except ImportError:
    pass
data_git_hash = "2b53c16ad1e3836da28898a2bf9347d7a11ad190"
data_git_describe = "v0.0-9456-g2b53c16ad"
data_git_msg = """\
commit 2b53c16ad1e3836da28898a2bf9347d7a11ad190
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Jan 17 14:59:44 2022 +0000

    [dv,spi] Remove some unnecessary "unique"s
    
    In these two statements, a unique case doesn't give any extra
    information (the cases are obviously distinct!) and it also doesn't
    actually work. VCS warns with:
    
        Warning-[UFCNP] Unique/priority final check ignored
        ../src/lowrisc_dv_spi_agent_0.1/spi_device_driver.sv, 67
          Unique/priority final check will not be performed for this statement.
          Unique/priority statement is not in always block or not in simple for-loop.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
