import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13164"
version_tuple = (0, 0, 13164)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13164")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13022"
data_version_tuple = (0, 0, 13022)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13022")
except ImportError:
    pass
data_git_hash = "a62799f93409c31ed91e8af9475bae555bb7aa16"
data_git_describe = "v0.0-13022-ga62799f934"
data_git_msg = """\
commit a62799f93409c31ed91e8af9475bae555bb7aa16
Author: Weicai Yang <weicai@google.com>
Date:   Mon Jul 18 15:28:51 2022 -0700

    [spi] Fix an assertion
    
    payload swap constraint should be applied to read command, which is
    `PayloadIn` instead of `PayloadOut`
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
