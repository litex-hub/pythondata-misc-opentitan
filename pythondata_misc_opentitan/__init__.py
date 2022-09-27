import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14457"
version_tuple = (0, 0, 14457)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14457")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14315"
data_version_tuple = (0, 0, 14315)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14315")
except ImportError:
    pass
data_git_hash = "e424b2567b62e8a7b9b16dfb251456da3433fd31"
data_git_describe = "v0.0-14315-ge424b2567b"
data_git_msg = """\
commit e424b2567b62e8a7b9b16dfb251456da3433fd31
Author: Dan McArdle <dmcardle@google.com>
Date:   Tue Sep 27 12:52:20 2022 -0400

    [doc] s/Understaning/Understanding/ in _index.md
    
    lowRISC/opentitan#14805
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
