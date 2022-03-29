import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11169"
version_tuple = (0, 0, 11169)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11169")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11043"
data_version_tuple = (0, 0, 11043)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11043")
except ImportError:
    pass
data_git_hash = "cdcb6967f9ff49f3e6b932734303695a7c51dab7"
data_git_describe = "v0.0-11043-gcdcb6967f"
data_git_msg = """\
commit cdcb6967f9ff49f3e6b932734303695a7c51dab7
Author: Jade Philipoom <jadep@google.com>
Date:   Tue Mar 22 13:46:33 2022 +0000

    [sw,otbn] Remove outdated Makefile/rules.mk from code-snippets.
    
    Found these files when making Bazel rules and they seem to be from two
    build systems ago; they say to remove once the Meson system is working.
    Seems like it should definitely be safe to remove them now.
    
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
