import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9787"
version_tuple = (0, 0, 9787)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9787")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9665"
data_version_tuple = (0, 0, 9665)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9665")
except ImportError:
    pass
data_git_hash = "e99015e644d03768a616d463f4f8c991f07f3bb3"
data_git_describe = "v0.0-9665-ge99015e64"
data_git_msg = """\
commit e99015e644d03768a616d463f4f8c991f07f3bb3
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Mon Jan 24 18:12:10 2022 -0800

    [sw/rom] Update bazel rules
    
    1. Remove abs and sec_mmio dependencies from their respective mock
       functions.
    2. Add OPENTITAN_CPU target to libraries that depend on target specific
       definitions.
    3. Fix build issues with sigverify OTBN rules.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
