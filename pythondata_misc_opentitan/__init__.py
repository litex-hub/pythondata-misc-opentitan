import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14434"
version_tuple = (0, 0, 14434)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14434")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14292"
data_version_tuple = (0, 0, 14292)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14292")
except ImportError:
    pass
data_git_hash = "955d57a70b66373c08cbe575de83c4754315bc8a"
data_git_describe = "v0.0-14292-g955d57a70b"
data_git_msg = """\
commit 955d57a70b66373c08cbe575de83c4754315bc8a
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Sep 16 14:27:24 2022 +0200

    [otbn, util] Modify otbn_sim_test rule to use new wrapper.
    
    Use the new OTBN simulator test wrapper in the otbn_sim_test Bazel rule.
    For compatibility with existing tests, this version simply always sets
    the expected values to "w0=0"; future updates will create specific
    expected-values files for each test.
    
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
