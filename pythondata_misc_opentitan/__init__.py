import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10390"
version_tuple = (0, 0, 10390)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10390")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10264"
data_version_tuple = (0, 0, 10264)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10264")
except ImportError:
    pass
data_git_hash = "dfe2e4e635d3ec62cdcf811e40bcca892a03e161"
data_git_describe = "v0.0-10264-gdfe2e4e63"
data_git_msg = """\
commit dfe2e4e635d3ec62cdcf811e40bcca892a03e161
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Feb 14 15:45:38 2022 +0100

    [aes] Fix AscentLint errors
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
