import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9800"
version_tuple = (0, 0, 9800)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9800")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9678"
data_version_tuple = (0, 0, 9678)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9678")
except ImportError:
    pass
data_git_hash = "4d7a648fcc5a51a4c89dc8df1fb8ce22a7fae728"
data_git_describe = "v0.0-9678-g4d7a648fc"
data_git_msg = """\
commit 4d7a648fcc5a51a4c89dc8df1fb8ce22a7fae728
Author: Drew Macrae <drewmacrae@google.com>
Date:   Tue Jan 25 14:15:57 2022 -0800

    [bazel] sigverify_dynamic_functest has more deps
    
    This part of https://github.com/lowRISC/opentitan/pull/10041 was
    necessary to correct the building and testing of the
    sigverify_dynamic_functest. Due to some recent changes it's no longer
    sufficient.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
