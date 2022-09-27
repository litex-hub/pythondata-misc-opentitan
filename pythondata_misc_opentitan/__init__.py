import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14448"
version_tuple = (0, 0, 14448)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14448")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14306"
data_version_tuple = (0, 0, 14306)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14306")
except ImportError:
    pass
data_git_hash = "f1b87a7786f602bf223cbb41a71e543e34205f93"
data_git_describe = "v0.0-14306-gf1b87a7786"
data_git_msg = """\
commit f1b87a7786f602bf223cbb41a71e543e34205f93
Author: Joshua Park <jeoong@google.com>
Date:   Wed Sep 21 17:15:19 2022 -0700

    [DV|CSR BIT BASH] Excluded two watermark RO registers
    
    - watermarks (RD CSR) is updated by internal HW when reg2hw.health_test_window.fips_window is updated multiple times like a sweep test. When it is written by 0, the watermark is also cleared to 0.
    
    Signed-off-by: Joshua Park <jeoong@google.com>

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
