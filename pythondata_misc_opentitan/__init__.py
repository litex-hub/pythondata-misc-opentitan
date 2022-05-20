import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12260"
version_tuple = (0, 0, 12260)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12260")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12132"
data_version_tuple = (0, 0, 12132)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12132")
except ImportError:
    pass
data_git_hash = "dad98a7b6e7ad69a815442402c4e15206c689fad"
data_git_describe = "v0.0-12132-gdad98a7b6"
data_git_msg = """\
commit dad98a7b6e7ad69a815442402c4e15206c689fad
Author: Jade Philipoom <jadep@google.com>
Date:   Fri May 20 10:43:52 2022 +0100

    [silicon_creator] Update sigverify test vector header template.
    
    This template is used for testing alternate test vector sets such as
    Wycheproof. I recently ran the large test set for the first time in a
    while to check some recent changes and noticed the template had gotten
    slightly out of sync with the surrounding code.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
