import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9819"
version_tuple = (0, 0, 9819)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9819")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9697"
data_version_tuple = (0, 0, 9697)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9697")
except ImportError:
    pass
data_git_hash = "e9c6841f99407e7d844d013cef3e0c12b3828439"
data_git_describe = "v0.0-9697-ge9c6841f9"
data_git_msg = """\
commit e9c6841f99407e7d844d013cef3e0c12b3828439
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Jan 21 12:12:40 2022 +0000

    [sw,crypto] Fix cryptolib tests.
    
    Remaining fixups so that code not only builds but also passes tests and
    format checks.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
