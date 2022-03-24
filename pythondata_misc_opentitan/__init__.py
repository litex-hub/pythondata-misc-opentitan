import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11052"
version_tuple = (0, 0, 11052)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11052")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10926"
data_version_tuple = (0, 0, 10926)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10926")
except ImportError:
    pass
data_git_hash = "f3da340e3abcee2b8dab253fa9698be488cdc45d"
data_git_describe = "v0.0-10926-gf3da340e3"
data_git_msg = """\
commit f3da340e3abcee2b8dab253fa9698be488cdc45d
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 23 14:26:34 2022 -0700

    [spi_device] Update BUSY section in the spec.
    
    As BUSY clearing and STATUS update behaviors are changed in this PR, I
    update the spec to reflect the current design.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
