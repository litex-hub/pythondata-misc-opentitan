import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11412"
version_tuple = (0, 0, 11412)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11412")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11286"
data_version_tuple = (0, 0, 11286)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11286")
except ImportError:
    pass
data_git_hash = "b6a4941afece4e4bbde47e4ff688e5b61fc863df"
data_git_describe = "v0.0-11286-gb6a4941af"
data_git_msg = """\
commit b6a4941afece4e4bbde47e4ff688e5b61fc863df
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Mon Apr 4 14:21:46 2022 -0400

    [bazel] Bazelize the example BL0
    
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
