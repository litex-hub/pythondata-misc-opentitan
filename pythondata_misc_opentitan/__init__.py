import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10459"
version_tuple = (0, 0, 10459)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10459")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10333"
data_version_tuple = (0, 0, 10333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10333")
except ImportError:
    pass
data_git_hash = "3281bd3cf497853245a7d59678ae5ceeb4d411c7"
data_git_describe = "v0.0-10333-g3281bd3cf"
data_git_msg = """\
commit 3281bd3cf497853245a7d59678ae5ceeb4d411c7
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Feb 21 14:19:12 2022 +0100

    [aes] Allow de-asserting EDN request upon fatal alerts
    
    This fixes lowRISC/OpenTitan#10991.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
