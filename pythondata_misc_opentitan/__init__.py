import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12213"
version_tuple = (0, 0, 12213)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12213")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12085"
data_version_tuple = (0, 0, 12085)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12085")
except ImportError:
    pass
data_git_hash = "b9370006f49956571000ec34c7f7ae84a08badc2"
data_git_describe = "v0.0-12085-gb9370006f"
data_git_msg = """\
commit b9370006f49956571000ec34c7f7ae84a08badc2
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Thu May 12 13:34:36 2022 -0400

    [dif/edn] Add unit tests
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
