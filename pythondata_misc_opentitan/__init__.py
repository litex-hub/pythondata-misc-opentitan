import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13263"
version_tuple = (0, 0, 13263)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13263")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13121"
data_version_tuple = (0, 0, 13121)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13121")
except ImportError:
    pass
data_git_hash = "b104a4f68768df102cc85cae3eff7bfc4921ddc5"
data_git_describe = "v0.0-13121-gb104a4f687"
data_git_msg = """\
commit b104a4f68768df102cc85cae3eff7bfc4921ddc5
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Jul 18 14:58:32 2022 +0100

    [sigverify] Update OTBN instruction count range.
    
    The original range was wrong because it missed a branch in the
    computation of R^2. This range has been confirmed locally both by a
    manual check and also a new automatic script. CI test to follow once the
    script is merged, which should prevent future errors.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
