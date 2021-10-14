import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8279"
version_tuple = (0, 0, 8279)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8279")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8167"
data_version_tuple = (0, 0, 8167)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8167")
except ImportError:
    pass
data_git_hash = "936db9a03080ca0a42ac56a094c1eb90e11bfd50"
data_git_describe = "v0.0-8167-g936db9a03"
data_git_msg = """\
commit 936db9a03080ca0a42ac56a094c1eb90e11bfd50
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 13 19:55:11 2021 +0000

    [dif/alert_handler] Remove need to pass in HW params.
    
    This partially addresses #8409, with respect to the Alert Handler.
    
    Templated IPs (which have the `templated` attribute in the `<toplevel>.hjson`
    file) **_may_** have DIFs that require extra bits of information related to
    the specific toplevel instantiation of said IP for DIF arg-checking purposes.
    This toplevel instantiation specific information was most recently
    encapsulated in the `dif_<ip>_params_t` struct, which was manually defined
    in the Alert Handler's DIF header file, and passed in as an argument to
    various DIFs. However, the information contained in this struct is
    already automatically generated in the `alert_handler_regs.h` header
    file. To reduce usage complexity, the `dif_alert_handler_params_t`
    struct was deprecated, and the required parameter information is used
    directly from the `alert_handler_regs.h` header file throughout the
    various Alert Handler DIFs that require this information.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
