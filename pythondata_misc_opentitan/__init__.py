import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14243"
version_tuple = (0, 0, 14243)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14243")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14101"
data_version_tuple = (0, 0, 14101)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14101")
except ImportError:
    pass
data_git_hash = "40ba9daefe8726641547990503142fcd752cd2f2"
data_git_describe = "v0.0-14101-g40ba9daefe"
data_git_msg = """\
commit 40ba9daefe8726641547990503142fcd752cd2f2
Author: Jes B. Klinke <jbk@chromium.org>
Date:   Mon Jun 13 04:52:52 2022 -0700

    [opentitantool] Add transport subcommand
    
    UltraDebug and the CW310 Atmel chip both have firmware that hard-codes
    the functionality of reset, uart, and all other pins, and are therefore
    ready for operation upon powering on.
    
    HyperDebug on the other hand, is not hard-coded for any OpenTitan pin
    assignments, and all its ports default to high-impedance.  Hence, it
    needs some initialization to be told among other things that the reset
    pin should be open-drain with pullup, defaulting high, and the boot0
    pins should be push-pull defaulting to a low level.  These pin
    configurations and defaults are generally declared in configuration
    files.  OpenTitan tool cannot blindly apply these defaults at every
    invocation, as it would override any previous pin manipulation in the
    session.
    
    This PR introduces a new command `transport init`, meant to explicitly
    tell the OpenTitan tool to configure all pins according to the
    configuration, and set their level to the default (discarding any
    previously set levels).
    
    I have create the `transport` top-level command with the intent that
    HyperDebug or other transports may have some special features that do
    not fit well into any generic trait, and we could add a channel for
    sending arbitrary instructions to the transport, without OpenTitan tool
    understanding those instructions.  HyperDebug for instance already has a
    textual command line interface, if it had a command for setting e.g. the
    slope control on I2C or SPI lines, then OpenTitan tool could be fitted
    with a `transport passthrough` command, allowing the sending of a text
    string verbatim to the transport for processing.
    
    Signed-off-by: Jes B. Klinke <jbk@chromium.org>
    Change-Id: Ifd004b024a087beb91ae57268a87d02063af8e85

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
