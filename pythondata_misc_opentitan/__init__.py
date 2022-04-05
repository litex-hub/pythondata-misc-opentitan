import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11381"
version_tuple = (0, 0, 11381)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11381")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11255"
data_version_tuple = (0, 0, 11255)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11255")
except ImportError:
    pass
data_git_hash = "f78b283951fd2d5c18d40348ce4b12b23b17f2ae"
data_git_describe = "v0.0-11255-gf78b28395"
data_git_msg = """\
commit f78b283951fd2d5c18d40348ce4b12b23b17f2ae
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Fri Apr 1 18:05:34 2022 -0400

    [bazel] Merge mock targets in mask_rom
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
