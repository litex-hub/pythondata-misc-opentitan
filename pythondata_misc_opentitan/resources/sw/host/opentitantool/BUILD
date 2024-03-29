# Copyright lowRISC contributors.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

load("@rules_rust//rust:defs.bzl", "rust_binary")
load("@rules_pkg//pkg:mappings.bzl", "pkg_filegroup", "pkg_files")

package(default_visibility = ["//visibility:public"])

rust_binary(
    name = "opentitantool",
    srcs = [
        "src/command/bootstrap.rs",
        "src/command/console.rs",
        "src/command/emulator.rs",
        "src/command/fpga.rs",
        "src/command/fpga_reset.rs",
        "src/command/gpio.rs",
        "src/command/hello.rs",
        "src/command/i2c.rs",
        "src/command/image.rs",
        "src/command/load_bitstream.rs",
        "src/command/mod.rs",
        "src/command/otp.rs",
        "src/command/rsa.rs",
        "src/command/set_pll.rs",
        "src/command/spi.rs",
        "src/command/transport.rs",
        "src/command/update_usr_access.rs",
        "src/command/version.rs",
        "src/main.rs",
    ],
    proc_macro_deps = [
        "//sw/host/opentitanlib/opentitantool_derive",
    ],
    stamp = 1,
    tags = [
        # Only until we figure out how to deal with version.rs including
        # the bazel voltatile-status.txt file.
        "no-clippy",
    ],
    deps = [
        "//sw/host/opentitanlib",
        "//third_party/rust/crates:anyhow",
        "//third_party/rust/crates:atty",
        "//third_party/rust/crates:directories",
        "//third_party/rust/crates:env_logger",
        "//third_party/rust/crates:erased_serde",
        "//third_party/rust/crates:hex",
        "//third_party/rust/crates:humantime",
        "//third_party/rust/crates:log",
        "//third_party/rust/crates:nix",
        "//third_party/rust/crates:raw_tty",
        "//third_party/rust/crates:regex",
        "//third_party/rust/crates:serde",
        "//third_party/rust/crates:serde_bytes",
        "//third_party/rust/crates:serde_json",
        "//third_party/rust/crates:shellwords",
        "//third_party/rust/crates:structopt",
        "//third_party/rust/crates:thiserror",
        "@serde_annotate",
    ],
)

pkg_files(
    name = "binary",
    srcs = [":opentitantool"],
)

pkg_filegroup(
    name = "package",
    srcs = [
        ":binary",
    ],
    prefix = "opentitantool",
)
