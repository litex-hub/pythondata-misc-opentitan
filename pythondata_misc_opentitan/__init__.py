import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12429"
version_tuple = (0, 0, 12429)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12429")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12287"
data_version_tuple = (0, 0, 12287)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12287")
except ImportError:
    pass
data_git_hash = "33ea5821037a0ee96f4b034c9758819b6d8b1fd8"
data_git_describe = "v0.0-12287-g33ea58210"
data_git_msg = """\
commit 33ea5821037a0ee96f4b034c9758819b6d8b1fd8
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue May 31 12:50:52 2022 -0700

    fix(spi_device)!: Default to Flash Mode
    
    As discussed in #12808, SPI_DEVICE default mode is changed to Flash mode
    in this commit. It removes three register writes in the Boot ROM.
    
    As Generic feature still lives in the SPI_DEVICE IP, SW can always
    change back to Generic mode.
    
    Justification:
    
        BootROM has been switched to SPI Flash mode to download the ROM
        Extension images. The usage of SPI_DEVICE is focused on Flash mode
        and Passthrough mode. Changing between Generic mode and
        (Flash/Passthrough) mode is not easy due to the clock change. SW
        shall follow the steps in the doc. This change eliminates the
        unnecessary steps in most cases.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
