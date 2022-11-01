import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15079"
version_tuple = (0, 0, 15079)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15079")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14937"
data_version_tuple = (0, 0, 14937)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14937")
except ImportError:
    pass
data_git_hash = "53874025b840788d5e66ffddae8fe7840a9cf4df"
data_git_describe = "v0.0-14937-g53874025b8"
data_git_msg = """\
commit 53874025b840788d5e66ffddae8fe7840a9cf4df
Author: Weicai Yang <weicai@google.com>
Date:   Sun Oct 30 23:41:38 2022 -0700

    [dv] Update dv_base_reg_field to handle status interrupts
    
    Related to #15580
    Use CSR access (RO/W1C) to distinguish status interrupt or regular interrupt
    It determines how intr_test affects the corresponding intr_state value.
    
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
