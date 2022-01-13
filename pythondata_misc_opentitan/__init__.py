import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9492"
version_tuple = (0, 0, 9492)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9492")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9374"
data_version_tuple = (0, 0, 9374)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9374")
except ImportError:
    pass
data_git_hash = "4b74463b4dfc853ea5b4e0821bb216890ee53907"
data_git_describe = "v0.0-9374-g4b74463b4"
data_git_msg = """\
commit 4b74463b4dfc853ea5b4e0821bb216890ee53907
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sun Nov 7 15:56:49 2021 -0800

    [ spi_host, prj ] Update SPI_HOST checklist
    
    - Indicate all items as ready for D2
    - Mark items in D2S, V2S as N/A
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
