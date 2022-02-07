import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10115"
version_tuple = (0, 0, 10115)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10115")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9991"
data_version_tuple = (0, 0, 9991)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9991")
except ImportError:
    pass
data_git_hash = "99263a63f3eec22e1d34ebeef039a74c1ea7ec2b"
data_git_describe = "v0.0-9991-g99263a63f"
data_git_msg = """\
commit 99263a63f3eec22e1d34ebeef039a74c1ea7ec2b
Author: Weicai Yang <weicai@google.com>
Date:   Mon Feb 7 13:39:25 2022 -0800

    [dv] Enable xcelium to include X for toggle coverage
    
    Address #10332
    Signed-off-by: Weicai Yang <weicai@google.com>

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
