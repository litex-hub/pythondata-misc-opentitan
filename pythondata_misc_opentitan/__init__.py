import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11528"
version_tuple = (0, 0, 11528)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11528")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11402"
data_version_tuple = (0, 0, 11402)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11402")
except ImportError:
    pass
data_git_hash = "569feb9b692c4e25d1448588b664ab061b04eb83"
data_git_describe = "v0.0-11402-g569feb9b6"
data_git_msg = """\
commit 569feb9b692c4e25d1448588b664ab061b04eb83
Author: Kosta Kojdic <kosta.kojdic@ensilica.com>
Date:   Mon Apr 11 14:13:19 2022 +0100

    Functional coverage flash and pass
    
    Signed-off-by: Kosta Kojdic <kosta.kojdic@ensilica.com>

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
