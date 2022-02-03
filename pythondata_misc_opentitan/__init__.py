import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10054"
version_tuple = (0, 0, 10054)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10054")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9930"
data_version_tuple = (0, 0, 9930)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9930")
except ImportError:
    pass
data_git_hash = "cc8ad6a1db0afdbbe3cd147bc63fda7e9e26ef6e"
data_git_describe = "v0.0-9930-gcc8ad6a1d"
data_git_msg = """\
commit cc8ad6a1db0afdbbe3cd147bc63fda7e9e26ef6e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 3 17:07:49 2022 +0000

    [otbn,dv] Wait to come out of reset in the stress_all vseq
    
    This sequence is used by otbn_stress_all_with_rand_reset. The
    sequences that otbn_stress_all_vseq calls all exit immediately when
    the device goes into reset. We need to make sure we don't immediately
    start another sequence (when we're still in reset) because that would,
    in turn exit immediately.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
