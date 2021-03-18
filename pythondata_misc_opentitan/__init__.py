import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5479"
version_tuple = (0, 0, 5479)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5479")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5384"
data_version_tuple = (0, 0, 5384)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5384")
except ImportError:
    pass
data_git_hash = "540661ebb656caadb5d1e71d920f0e9e88e11451"
data_git_describe = "v0.0-5384-g540661ebb"
data_git_msg = """\
commit 540661ebb656caadb5d1e71d920f0e9e88e11451
Author: Weicai Yang <weicai@google.com>
Date:   Tue Mar 16 17:40:18 2021 -0700

    [chip/dv] Add chip_stub_cpu_base_vseq
    
    extract it from chip_common_vseq to use for other seq with stub mode
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
