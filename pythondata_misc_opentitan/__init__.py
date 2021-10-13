import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8255"
version_tuple = (0, 0, 8255)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8255")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8143"
data_version_tuple = (0, 0, 8143)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8143")
except ImportError:
    pass
data_git_hash = "937d707e7b1a666bf2a06bbc2c774553d140497a"
data_git_describe = "v0.0-8143-g937d707e7"
data_git_msg = """\
commit 937d707e7b1a666bf2a06bbc2c774553d140497a
Author: Weicai Yang <weicai@google.com>
Date:   Tue Oct 12 16:19:13 2021 -0700

    [dv] Fix shadow reg backdoor path and enable csr_reset sequence
    
    Thanks Tim Chen for finding the backdoor path issue that we deposit
    backdoor value into a net rather a storage
    
    1. This PR removed committed path as we only need the default path and
    shadow path
    2. Fixed default path to a real storage register
    3. Enhance csr_wr seq to backdoor write all the paths for csr_reset seq
    4. Enhance csr_reset seq to also do backdoor read check to ensure we
    don't deposit value to a net
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
