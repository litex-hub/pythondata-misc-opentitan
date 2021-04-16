import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5913"
version_tuple = (0, 0, 5913)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5913")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5818"
data_version_tuple = (0, 0, 5818)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5818")
except ImportError:
    pass
data_git_hash = "35d771817d33442ab8ef32e22598f8998c26a06b"
data_git_describe = "v0.0-5818-g35d771817"
data_git_msg = """\
commit 35d771817d33442ab8ef32e22598f8998c26a06b
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Wed Apr 7 00:12:46 2021 -0700

    [sw/dif] CSRNG Updates
    
    Add implementations for the following functions
    
    *   `dif_csrng_instantiate()`
    *   `dif_csrng_reseed()`
    *   `dif_csrng_update()`
    *   `dif_csrng_generate()`
    *   `dif_csrng_read_output()`
    
    Update `dif_csrng_smoketest.cc` to run the CSRNG in software mode
    with a determistic seed.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
