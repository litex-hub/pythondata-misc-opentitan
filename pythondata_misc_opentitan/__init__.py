import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9659"
version_tuple = (0, 0, 9659)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9659")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9537"
data_version_tuple = (0, 0, 9537)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9537")
except ImportError:
    pass
data_git_hash = "954592a075a4a0fad158a8363715c4b6d12219db"
data_git_describe = "v0.0-9537-g954592a07"
data_git_msg = """\
commit 954592a075a4a0fad158a8363715c4b6d12219db
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Wed Jan 19 13:10:24 2022 +0000

    [adc_ctrl] Excluded adc_en_ctl.adc_enable field from CSR write tests
    
    - Updated adc_ctrl.hjson to disable writing to adc_en_ctl.adc_enable
    during CSR tests this is to prevent unpredictable side effects.
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

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
