import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8669"
version_tuple = (0, 0, 8669)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8669")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8557"
data_version_tuple = (0, 0, 8557)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8557")
except ImportError:
    pass
data_git_hash = "759917d35e9a9be5f00542613846a8d94b98f14a"
data_git_describe = "v0.0-8557-g759917d35"
data_git_msg = """\
commit 759917d35e9a9be5f00542613846a8d94b98f14a
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Wed Nov 3 11:10:15 2021 -0700

    [edn/dv] Added genbits test/sequence, randomized genbits
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
