import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10931"
version_tuple = (0, 0, 10931)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10931")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10805"
data_version_tuple = (0, 0, 10805)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10805")
except ImportError:
    pass
data_git_hash = "0f337102132a1bb0209f93414d1a3cd0b2734c85"
data_git_describe = "v0.0-10805-g0f3371021"
data_git_msg = """\
commit 0f337102132a1bb0209f93414d1a3cd0b2734c85
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Wed Mar 16 14:55:09 2022 -0400

    Add #include clarifications in freestading/README.md
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
