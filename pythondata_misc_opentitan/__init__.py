import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14301"
version_tuple = (0, 0, 14301)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14301")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14159"
data_version_tuple = (0, 0, 14159)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14159")
except ImportError:
    pass
data_git_hash = "b0ca56797ff459e1f74e010bbc6bc6019f38d772"
data_git_describe = "v0.0-14159-gb0ca56797f"
data_git_msg = """\
commit b0ca56797ff459e1f74e010bbc6bc6019f38d772
Author: Jade Philipoom <jadep@google.com>
Date:   Thu Sep 15 17:40:29 2022 +0200

    [otbn, util] Add start constants to information-flow analysis.
    
    Starting constants were previously added to `check_const_time.py`; this
    adds them to `analyze_information_flow.py` as well, since the two use
    the same backend.
    
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
