// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

#include "sw/device/lib/arch/device.h"

/**
 * @file
 * @brief Device-specific symbol definitions for the ChipWhisperer CW310 device.
 */

const device_type_t kDeviceType = kDeviceFpgaCw310;

const uint64_t kClockFreqCpuHz = 10 * 1000 * 1000;  // 10MHz

const uint64_t kClockFreqPeripheralHz = 25 * 100 * 1000;  // 2.5MHz

const uint64_t kClockFreqUsbHz = 48 * 1000 * 1000;  // 48MHz

const uint64_t kClockFreqAonHz = 200 * 1000;  // 200kHz

const uint64_t kUartBaudrate = 115200;

const uint32_t kUartNCOValue =
    CALCULATE_UART_NCO(kUartBaudrate, kClockFreqPeripheralHz);

const uint32_t kUartTxFifoCpuCycles =
    CALCULATE_UART_TX_FIFO_CPU_CYCLES(kUartBaudrate, kClockFreqCpuHz);

const uintptr_t kDeviceTestStatusAddress = 0;

const uintptr_t kDeviceLogBypassUartAddress = 0;
