import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11428"
version_tuple = (0, 0, 11428)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11428")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11302"
data_version_tuple = (0, 0, 11302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11302")
except ImportError:
    pass
data_git_hash = "7c3843df31022bcbc11c53f5dbed9002276899a0"
data_git_describe = "v0.0-11302-g7c3843df3"
data_git_msg = """\
commit 7c3843df31022bcbc11c53f5dbed9002276899a0
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Apr 5 17:07:32 2022 +0100

    [host,test] Fix broken test in host tools.
    
    When trying to test out a new change I found that this test was actually
    broken on master; it's a pretty straightforward fix. The test was
    assuming the identifier field is at the start of the manifest; filling
    in the identifier field's actual offset fixed the test.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
