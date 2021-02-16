import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5005"
version_tuple = (0, 0, 5005)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5005")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4914"
data_version_tuple = (0, 0, 4914)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4914")
except ImportError:
    pass
data_git_hash = "f6803cbe20ef438cbebe38d50cfa60a3e4348018"
data_git_describe = "v0.0-4914-gf6803cbe2"
data_git_msg = """\
commit f6803cbe20ef438cbebe38d50cfa60a3e4348018
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Feb 10 10:45:48 2021 +0000

    [otbn] Initial rewriting support in extracted documentation
    
    This generates a "pretty" version of GPR/WDR accesses. For example,
    the ADD instruction looked like this before:
    
        val1 = state.gprs.get_reg(self.grs1).read_unsigned()
        val2 = state.gprs.get_reg(self.grs2).read_unsigned()
        result = (val1 + val2) & ((1 << 32) - 1)
        state.gprs.get_reg(self.grd).write_unsigned(result)
    
    and now looks like this:
    
        val1 = GPRs[self.grs1]
        val2 = GPRs[self.grs2]
        result = (val1 + val2) & ((1 << 32) - 1)
        GPRs[self.grd] = result
    
    Signed (2's complement) conversions are shown explicitly. For example,
    here's SRA:
    
        val1 = from_2s_complement(GPRs[self.grs1])
        val2 = GPRs[self.grs2] & 0x1f
        result = val1 >> val2
        GPRs[self.grd] = to_2s_complement(result)
    
    WDRs are also converted. For example, BN.ADD looks like this:
    
        a = WDRs[self.wrs1]
        b = WDRs[self.wrs2]
        b_shifted = logical_byte_shift(b, self.shift_type, self.shift_bytes)
    
        (result, flags) = state.add_with_carry(a, b_shifted, 0)
        WDRs[self.wrd] = result
        state.set_flags(self.flag_group, flags)
    
    This is just an initial rewrite pass. If we go with this, we'll want
    to do things for flags, at least. This is easy enough with the same
    framework.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
