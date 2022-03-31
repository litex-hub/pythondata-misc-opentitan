import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11247"
version_tuple = (0, 0, 11247)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11247")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11121"
data_version_tuple = (0, 0, 11121)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11121")
except ImportError:
    pass
data_git_hash = "33ef10435f5c2b5edbf93a54b39a14365c5059ff"
data_git_describe = "v0.0-11121-g33ef10435"
data_git_msg = """\
commit 33ef10435f5c2b5edbf93a54b39a14365c5059ff
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Mar 29 10:57:03 2022 +0200

    [aes] Fix clearing of data input registers without inferring combo loop
    
    Previously, the write enable for the data input registers was set for
    two clock cycles when clearing the registers. This caused the
    data_in_qe_i signals used for status tracking to be high during the
    first clock cycle when back in IDLE. As a result, the AES unit would
    immediately start when running in automatic operation.
    
    This is a second version of the fix that doesn't infer a combo loop by
    splitting the clearing operation into two distinct states: First CLEAR_I
    clears input registers such as Initial Key, IV and input data registers.
    Then CLEAR_CO waits for the cipher core, clears the trigger bits and
    if selected also clear the output data registers.
    
    This is related to lowRISC/OpenTitan#11431 and lowRISC/OpenTitan#11758.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
