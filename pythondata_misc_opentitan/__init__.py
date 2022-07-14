import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13089"
version_tuple = (0, 0, 13089)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13089")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12947"
data_version_tuple = (0, 0, 12947)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12947")
except ImportError:
    pass
data_git_hash = "87b269981fbbbc3041cdee21184ba97e6b094184"
data_git_describe = "v0.0-12947-g87b269981f"
data_git_msg = """\
commit 87b269981fbbbc3041cdee21184ba97e6b094184
Author: Stefan Lippuner <lstefan@iis.ee.ethz.ch>
Date:   Wed Jun 29 09:00:03 2022 -0700

    [usbdev] Fix control bug on clear_rdybit
    
    The clear of the ready bit when a SETUP transaction completed would get
    overridden by a later conditional block, which had the effect of
    rewriting the logic function to never set clear_rdybit in response to
    SETUP transactions.
    
    Make the conditional blocks exclusive instead of sequential.
    
    Signed-off-by: Stefan Lippuner <lstefan@iis.ee.ethz.ch>
    Signed-off-by: Alexander Williams <awill@google.com>

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
