import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14461"
version_tuple = (0, 0, 14461)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14461")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14319"
data_version_tuple = (0, 0, 14319)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14319")
except ImportError:
    pass
data_git_hash = "b40e28862c7f82b149d7f233bedb211366a58fa8"
data_git_describe = "v0.0-14319-gb40e28862c"
data_git_msg = """\
commit b40e28862c7f82b149d7f233bedb211366a58fa8
Author: Weicai Yang <weicai@google.com>
Date:   Mon Sep 26 16:54:29 2022 -0700

    [spi_device/dv] Update monitor for TPM mode
    
    1. small refactor to reuse the part that kills threads after CSR drops
    2. Completed `collect_tpm_trans` task
    3. Renamed a few task as they can be reused for TPM mode
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
