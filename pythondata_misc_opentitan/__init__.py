import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12943"
version_tuple = (0, 0, 12943)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12943")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12801"
data_version_tuple = (0, 0, 12801)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12801")
except ImportError:
    pass
data_git_hash = "168cc3161d3232403592ef6370d0993874d0a346"
data_git_describe = "v0.0-12801-g168cc3161d"
data_git_msg = """\
commit 168cc3161d3232403592ef6370d0993874d0a346
Author: Michał Mazurek <maz@semihalf.com>
Date:   Wed Jun 15 10:55:07 2022 +0200

    [opentitanlib] Add I2C for Ti50Emulator transport
    
    The implementation of the I2C bus for the Ti50Emulator is based on the following assumptions.
    Connections between DUT and the Host are made directly (point-to-point).
    There are no other devices on the bus, only DUT and Host are connected.
    In order to perform the tests, the connections do not need to be simulated at the level of transmitted bits.
    The implementation does not simulate the ACK / NACK mechanism.
    
    The emulated I2C BUS is implemented as a Unix Stream socket with a request/respons
    based protocol to describe read and write transactions.
    
    Signed-off-by: Michał Mazurek <maz@semihalf.com>

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
