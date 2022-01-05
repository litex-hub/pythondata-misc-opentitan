import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9335"
version_tuple = (0, 0, 9335)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9335")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9218"
data_version_tuple = (0, 0, 9218)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9218")
except ImportError:
    pass
data_git_hash = "f6e5618114efb763ed63870bc5946c12631d2ec7"
data_git_describe = "v0.0-9218-gf6e561811"
data_git_msg = """\
commit f6e5618114efb763ed63870bc5946c12631d2ec7
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Dec 21 01:40:14 2021 -0800

    [spi_host/dv] created env for spi_host
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
