import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12860"
version_tuple = (0, 0, 12860)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12860")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12718"
data_version_tuple = (0, 0, 12718)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12718")
except ImportError:
    pass
data_git_hash = "c3f9c7423f0d25e075b81f0fab3c3faf2d827965"
data_git_describe = "v0.0-12718-gc3f9c7423f"
data_git_msg = """\
commit c3f9c7423f0d25e075b81f0fab3c3faf2d827965
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Jun 23 20:27:16 2022 -0700

    [chip-test] Add chip_sw_entropy_src_kat_test.
    
    Adds known answer test for the entropy_src SHA3 conditioner block using
    a SHA3 CAVP test vector. The test employs the entropy_src firmware
    override mode.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
