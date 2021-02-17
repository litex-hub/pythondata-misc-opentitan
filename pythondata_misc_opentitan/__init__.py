import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5029"
version_tuple = (0, 0, 5029)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5029")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4938"
data_version_tuple = (0, 0, 4938)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4938")
except ImportError:
    pass
data_git_hash = "729130d2bda4d1153bff81b1abe5091b6cd9f152"
data_git_describe = "v0.0-4938-g729130d2b"
data_git_msg = """\
commit 729130d2bda4d1153bff81b1abe5091b6cd9f152
Author: Dan Nussbaum <dansn@google.com>
Date:   Wed Feb 10 11:25:17 2021 -0500

    [doc] Fix typos in rust_for_c.md.
    
    Signed-off-by: Dan Nussbaum <dansn@google.com>

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
