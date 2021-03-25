import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5579"
version_tuple = (0, 0, 5579)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5579")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5484"
data_version_tuple = (0, 0, 5484)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5484")
except ImportError:
    pass
data_git_hash = "da490e7b187050ddad51bd093a3df9fc63abf8af"
data_git_describe = "v0.0-5484-gda490e7b1"
data_git_msg = """\
commit da490e7b187050ddad51bd093a3df9fc63abf8af
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 25 08:29:42 2021 +0000

    [otbn] Document the idle_o signal
    
    As Sri pointed out, I've just added some DV code that checks the
    idle_o signal does what I think it should do, but this isn't actually
    specced anywhere. Fix that!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
