import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5524"
version_tuple = (0, 0, 5524)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5524")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5429"
data_version_tuple = (0, 0, 5429)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5429")
except ImportError:
    pass
data_git_hash = "306799d9eac2c356263106d284a7f21fff85ff48"
data_git_describe = "v0.0-5429-g306799d9e"
data_git_msg = """\
commit 306799d9eac2c356263106d284a7f21fff85ff48
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Mar 22 15:25:08 2021 +0100

    [aes] Replace register file related literals by existing parameters
    
    The register tool exports parameters in aes_reg_pkg.sv that we can use
    instead of literals.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
