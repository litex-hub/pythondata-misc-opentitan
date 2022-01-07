import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9370"
version_tuple = (0, 0, 9370)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9370")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9253"
data_version_tuple = (0, 0, 9253)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9253")
except ImportError:
    pass
data_git_hash = "26887cb975e0512920b9359e5ee41d887d1f5601"
data_git_describe = "v0.0-9253-g26887cb97"
data_git_msg = """\
commit 26887cb975e0512920b9359e5ee41d887d1f5601
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jan 6 15:37:09 2022 -0800

    [sram/dv] Fix intg_err test
    
    Shouldn't do sram_init for intg_err test. Only apply init for
    passthru_mem test
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
