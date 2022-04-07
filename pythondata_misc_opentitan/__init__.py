import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11431"
version_tuple = (0, 0, 11431)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11431")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11305"
data_version_tuple = (0, 0, 11305)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11305")
except ImportError:
    pass
data_git_hash = "b352f3d54d2133fcd02f5bb2b5e16d77c522dafd"
data_git_describe = "v0.0-11305-gb352f3d54"
data_git_msg = """\
commit b352f3d54d2133fcd02f5bb2b5e16d77c522dafd
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Apr 6 16:51:47 2022 +0100

    [otbn,rtl] Use err_bits, not err_bits_q for alerts[AlertFatal]
    
    This fixes a bug introduced by 75885e6 where we'd only generate fatal
    alerts when an operation finished. One problem with this is that
    secure wipe takes ~100 cycles, so delays the alert. Another (more
    serious) problem is that it means alerts are squashed altogether when
    OTBN isn't running.
    
    Note that the timing of alerts[AlertFatal] now matches that of the
    FATAL_ALERT_CAUSE register, which should make a bit more sense.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
