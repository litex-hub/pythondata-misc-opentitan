import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8941"
version_tuple = (0, 0, 8941)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8941")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8829"
data_version_tuple = (0, 0, 8829)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8829")
except ImportError:
    pass
data_git_hash = "c5f2c32f4a0841bbc013e9076534c6cbbd5fe037"
data_git_describe = "v0.0-8829-gc5f2c32f4"
data_git_msg = """\
commit c5f2c32f4a0841bbc013e9076534c6cbbd5fe037
Author: kosta-kojdic <kosta.kojdic@ensilica.com>
Date:   Tue Nov 30 11:10:36 2021 +0000

    End of lile lines
    
    Signed-off-by: kosta-kojdic <kosta.kojdic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
