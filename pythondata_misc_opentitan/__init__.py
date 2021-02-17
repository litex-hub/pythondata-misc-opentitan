import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5032"
version_tuple = (0, 0, 5032)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5032")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4941"
data_version_tuple = (0, 0, 4941)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4941")
except ImportError:
    pass
data_git_hash = "b826e4d7ab2b4adce37accb2221354c83ed1c1ba"
data_git_describe = "v0.0-4941-gb826e4d7a"
data_git_msg = """\
commit b826e4d7ab2b4adce37accb2221354c83ed1c1ba
Author: Weicai Yang <weicai@google.com>
Date:   Tue Feb 16 11:53:23 2021 -0800

    [top/dv] Fix backdoor override
    
    readelf may trancate the symbol name if long is over 85 chars
    Since we need to find the symbol name `exp_spi_device_rx_data` to
    replace the value, we can't trancate it
    
    Before the fix:
    >  1512: 20003698   128 OBJECT  LOCAL  DEFAULT    6 exp_spi_device_r[...]
    After:
    >  1512: 20003698   128 OBJECT  LOCAL  DEFAULT    6 exp_spi_device_rx_data
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
