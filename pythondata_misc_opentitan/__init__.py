import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14603"
version_tuple = (0, 0, 14603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14461"
data_version_tuple = (0, 0, 14461)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14461")
except ImportError:
    pass
data_git_hash = "a3f6f6bceae186b732a07ceec350f54af85ffda1"
data_git_describe = "v0.0-14461-ga3f6f6bcea"
data_git_msg = """\
commit a3f6f6bceae186b732a07ceec350f54af85ffda1
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Oct 6 12:52:24 2022 -0700

    [top-test] entropy_src_csrng adjust timeout
    
    Adjust test timeout to fix nightly regression failure.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
