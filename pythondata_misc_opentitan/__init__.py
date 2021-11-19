import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8779"
version_tuple = (0, 0, 8779)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8779")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8667"
data_version_tuple = (0, 0, 8667)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8667")
except ImportError:
    pass
data_git_hash = "b1a874a946c157442ab010ae42abdfe5ef6d6ad4"
data_git_describe = "v0.0-8667-gb1a874a94"
data_git_msg = """\
commit b1a874a946c157442ab010ae42abdfe5ef6d6ad4
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Nov 17 15:13:53 2021 +0000

    [sw,crypto] Use Mako template for test vectors.
    
    Switch to using a Mako template for generating RSA test vector C header.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
