import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5248"
version_tuple = (0, 0, 5248)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5248")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5157"
data_version_tuple = (0, 0, 5157)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5157")
except ImportError:
    pass
data_git_hash = "caa0d898407ecb4ea345fd00469936b9feece7e3"
data_git_describe = "v0.0-5157-gcaa0d8984"
data_git_msg = """\
commit caa0d898407ecb4ea345fd00469936b9feece7e3
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Mar 1 13:15:52 2021 -0800

    [dvsim] Move clean_odirs to `util.py`
    
    Output directory cleaner does not need to be tied to a Launcher instance
    - moving it to a generic utils module.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
