# Awesome RT-Thread [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> RT-Thread is an open source, neutral, and community-based real-time operating system (RTOS) for embedded systems and Internet of things (IoT). It is developed by the RT-Thread Development Team based in China. 

## Contents

- [Official Resources](#official-resources)
- [Tools](#tools)
  - [Build \& Config](#build--config)
  - [Editors \& IDEs](#editors--ides)
- [Hardwares](#hardwares)
- [Projects](#projects)
- [Packages](#packages)
  - [IoT](#iot)
  - [Misc](#misc)
  - [Peripherals](#peripherals)
  - [Multimedia](#multimedia)
  - [AI](#ai)
  - [Security](#security)
  - [System](#system)
  - [Language](#language)
  - [Signal process](#signal-process)
  - [Tools](#tools-1)


## Official Resources

- [rt-thread.org](https://www.rt-thread.org) - Official website (China).
- [rt-thread.com](https://www.rt-thread.com) - Official website (Commercial).
- [rt-thread.io](https://www.rt-thread.io) - Official website (Global).
- [rt-thread.org/document/site](https://www.rt-thread.org/document/site/) - Project documentation (Chinese).
- [rt-thread.io/document/site](https://www.rt-thread.io/document/site/) - Project documentation (English).
- [Community](https://club.rt-thread.org) - RT-Thread community.
- [GitHub](https://github.com/RT-Thread) - RT-Thread GitHub organization.
  - [rt-thread](https://github.com/RT-Thread/rt-thread) - RT-Thread GitHub repository.
  - [rtthread-nano](https://github.com/RT-Thread/rtthread-nano) - RT-Thread Nano repository.
  - [packages](https://github.com/RT-Thread/packages) - RT-Thread packages index repository.
  - [env](https://github.com/RT-Thread/env) - RT-Thread Env tool.
- [RT-Thread packages GitHub](https://github.com/RT-Thread-packages) - RT-Thread packages GitHub organization.
- [RT-Thread-Studio GitHub](https://github.com/RT-Thread-Studio) - RT-Thread-Studio GitHub organization.
  - [sdk-bsp-stm32l475-atk-pandora](https://github.com/RT-Thread-Studio/sdk-bsp-stm32l475-atk-pandora) - SDK for the Pandora development board (IoT Board).
  - [sdk-bsp-stm32h750-realthread-artpi](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h750-realthread-artpi) - SDK for the ART-Pi development board.
  - [sdk-bsp-ra6m3-hmi-board](https://github.com/RT-Thread-Studio/sdk-bsp-ra6m3-hmi-board) - SDK for the HMI-Board development board.
  - [sdk-bsp-ra8d1-vision-board](https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board) - SDK for the Vision-Board development board.
- [Gitee](https://gitee.com/rtthread) - RT-Thread Gitee organization.
  - [rt-thread](https://gitee.com/rtthread/rt-thread) - RT-Thread Gitee repository.
  - [docs-online](https://gitee.com/rtthread/docs-online) - RT-Thread documentation repository.
- [RT-Thread-Mirror](https://gitee.com/RT-Thread-Mirror) - RT-Thread packages mirror in gitee.com.
- [YouTube](https://www.youtube.com/@rt-thread) | [Bilibili](https://space.bilibili.com/423462075/) - Tutorial videos and conference videos.
- [Medium](https://rt-thread.medium.com) | [Linkedin](https://www.linkedin.com/company/rt-thread-iot-os/) | [Twitter](https://twitter.com/rt_thread) | [Facebook](https://www.facebook.com/profile.php?id=100066719216600) - Various social feeds.



## Tools

### Build & Config

- [RT-Thread Env Tool](https://www.rt-thread.io/download.html?download=Env)
- [KConfig](https://www.kernel.org/doc/Documentation/kbuild/kconfig-language.txt)
- [Scons](https://scons.org)


### Editors & IDEs

- RT-Thread Studio IDE
- MDK KEIL
- IAR
- VS Code Extension
  - [RT-Thread Studio](https://marketplace.visualstudio.com/items?itemName=RT-Thread.rt-thread-studio) - RT-Thread Studio for vscode.
  - [RT-Thread Smart](https://marketplace.visualstudio.com/items?itemName=RT-Thread.rt-thread-smart) - An integrated development environment for RT-Thread Smart.
  - [RT-Thread MicroPython](https://marketplace.visualstudio.com/items?itemName=RT-Thread.rt-thread-micropython) - The best MicroPython plug-in of vscode.
  - [RT-Thread Assistant](https://marketplace.visualstudio.com/items?itemName=rtthreadfans.rtthread-assistant) - RT-Thread Assistant for vscode.



## Hardwares

- [Pandora IoT Board](https://github.com/RT-Thread/IoT_Board) - An IoT development board based on STM32L4 (Cortex-M4).
- [ART-Pi](https://art-pi.github.io/website/) - A DIY open source hardware based on STM32H750 designed by the RT-Thread team.
- [Spark (星火1号)](https://github.com/RT-Thread-Studio/sdk-bsp-stm32f407-spark) - An RTOS development learning board based on STM32F407 specially designed for engineers and college students.
- [HMI Board](https://club.rt-thread.org/ask/tag/1a7377d47be92f4e.html) - A high-cost-performance graphic evaluation kit brought to you by RT-Thread in collaboration with Renesas and LVGL.
- [Vision Board](https://club.rt-thread.org/ask/tag/75c03d50eabf688a.html) - A development board with camera based on the Renesas RA8D1 (Cortex-M85).



## Projects

- [Firmament (FMT)](https://github.com/Firmament-Autopilot/FMT-Firmware) - Firmament Autopilot Embedded System.
- [RTduino](https://github.com/RTduino/RTduino) - The Arduino ecosystem compatibility layer for RT-Thread.



## Packages


### IoT

- [protobuf-c](https://github.com/wuhanstudio/protobuf-c) - Protobuf-c library for rt-thread.
- [EmbeddedProto](https://github.com/wuhanstudio/EmbeddedProto) - A C++ Protocol Buffers implementation specifically suitable for ARM Cortex-M MCUs.
- [agile_ftp](https://github.com/loogg/agile_ftp) - Lightweight ftp server.
- [mavlink](https://github.com/sogwms/mavlink) - A very lightweight messaging protocol for communicating.
- [zFTP](https://github.com/longtengmcu/zFTP.git) - Please add description of zFTP in English.
- [ipmsg](https://github.com/heyuanjie87/ipmsg) - A LAN instant messaging implement in RT-Thread.
- [dlt645](https://github.com/WKJay/DLT645) - Dlt645 master package.
- [net_server](https://github.com/WKJay/net-server) - Net server supports TCP/TLS.
- [small_modbus](https://github.com/cazure/small_modbus.git) - Small modbus.
- [atsrv_socket](https://github.com/RT-Thread-packages/atsrv_socket) - AT server with socket commands.
- [bc28_mqtt](https://github.com/luhuadong/rtt-bc28-mqtt) - Connect to Aliyun with Quectel BC28 model.
- [mongoose](https://github.com/armink-rtt-pkgs/mongoose) - Embedded Web Server Library for RT-Thread package.
- [lora_pkt_fwd](https://github.com/Forest-Rain/lora-pkt-fwd) - A LoRa(wan) packet forward based on Semtech GWMP.
- [agile_modbus](https://github.com/loogg/agile_modbus) - Lightweight modbus protocol stack.
- [ota_downloader](https://github.com/RT-Thread-packages/ota_downloader) - The firmware downloader bases on RT-Thread OTA component.
- [matter-adaptation-layer](https://github.com/kurisaW/MATTER-Adaptation_Layer) - Matter protocol stack porting on RT-Thread based on guidance from Connectivity Standards Alliance (CSA) Working Group.
- [wlan_cyw43012](https://github.com/Guozhanxin/cyw43012-RTT) - Wlan driver from CYW43012.
- [wlanmarvell](https://github.com/JianRuiqian/marvellwifi) - Marvell WiFi driver for rt-thread.
- [rw007](https://github.com/RT-Thread-packages/rw007) - RW007 (SPI Wi-Fi module) driver for RT-Thread.
- [wlan_wiced](https://github.com/RT-Thread-packages/wlan-wiced) - Wlan driver from WICED.
- [wlan_bl808](https://github.com/flyingcys/wlan_bl808_rtthread) - Wlan driver from BL808.
- [wlan_cyw43439](https://github.com/Z8MAN8/cyw43439-RTT) - Wlan driver from CYW43439.
- [abup_fota](https://github.com/RayShen1018/Abup) - The firmware downloader bases on abup FOTA component.
- [bt_cyw43012](https://github.com/Guozhanxin/cyw43012-ble-RTT) - Bt driver from CYW43012.
- [bsal](https://github.com/RT-Thread-packages/bsal) - The Bluetooth Stack Layer.
- [lssdp](https://github.com/RT-Thread-packages/lssdp.git) - Lssdp protocol implemented on rt-thread.
- [hm](https://github.com/Jackistang/HCI-Middleware) - A generic Bluetooth HCI transport layer.
- [GAgent](https://github.com/RT-Thread-packages/GAgent) - GAgent of Gizwits on RT-Thread.
- [ali-iotkit](https://github.com/RT-Thread-packages/ali-iotkit) - Ali Cloud SDK for IoT platform.
- [joylink](https://github.com/RT-Thread-packages/joylink) - Joylink Cloud SDK for IoT platform.
- [onenet](https://github.com/RT-Thread-packages/onenet) - China Mobile OneNet cloud SDK for RT-Thread.
- [ucloud_iot_sdk](https://github.com/ucloud/ucloud-iot-rtthread-package.git) - Ucloud iot sdk for uiot-core platform.
- [azure-iot-sdk](https://github.com/RT-Thread-packages/azure-iot-sdk) - Microsoft azure cloud SDK for RT-Thread.
- [tencent-iot-sdk](https://github.com/tencentyun/tencent-cloud-iot-package-for-rtthread) - Tencent Cloud IOT SDK for iot_explorer platform.
- [iotsharp-c-sdk](https://github.com/IoTSharp/iotsharp-rtthread-package) - IoTSharp client sdk for RT-Thread.
- [jiot-c-sdk](https://github.com/jpush/JIoT-rtthread-package.git) - JIGUANG IoT cloud client sdk for RT-Thread.
- [nmealib](https://github.com/ShineRoyal/nmealib) - A nmelib library porting on RT thread.
- [lhc_modbus](https://github.com/LHC324/lhc_modbus) - Lightweight and high-performance C language modbus protocol stack.
- [lorawan_driver](https://github.com/zyk6271/LoRaWAN_Driver) - Support for LoRaWAN Network with RT-Thread.
- [nopoll](https://github.com/RT-Thread-packages/nopoll) - A OpenSource WebSocket implementation (RFC 6455) in ansi C.
- [cmux](https://github.com/RT-Thread-packages/cmux) - Connection multiplexing protocol for RT-Thread, support GSM0710 .etc.
- [rt-link_hw](https://github.com/RT-Thread-packages/rt-link_hw) - The underlying communication port adaptation layer of the rt-link component.
- [RyanW5500](https://github.com/Ryan-CW-Code/RyanW5500) - W5500 BSD socket implementation.
- [lora_pkt_sniffer](https://github.com/Forest-Rain/lora-pkt-sniffer) - A sniffer tool of LoRa(wan) packet.
- [WebTerminal](https://github.com/armink-rtt-pkgs/WebTerminal) - Terminal runs in a Web browser.
- [mymqtt](https://github.com/hichard/mymqtt) - Eclipse Paho MQTT C/C++ client for Embedded platforms.A new efficient and stable way to realize for rt-thread.
- [capnp](https://github.com/wuhanstudio/capnp) - Cap'n Proto serialization/RPC system which is faster than protobuf.
- [qxwz](https://github.com/RT-Thread-packages/qianxun.git) - High precision location library for RT-Thread.
- [librws](https://github.com/RT-Thread-packages/librws) - Tiny, cross platform websocket client C library.
- [RyanMqtt](https://github.com/Ryan-CW-Code/RyanMqtt) - RyanMqtt client library provides an implementation of the MQTT 3.1.1 specification. It is optimized for resource constrained devices.
- [pahomqtt](https://github.com/RT-Thread-packages/paho-mqtt) - Eclipse Paho MQTT C/C++ client for Embedded platforms.
- [freemodbus](https://github.com/RT-Thread-packages/freemodbus) - Modbus master and slave stack.
- [wol](https://github.com/WKJay/wol) - Wake on lan package for rt-thread.
- [lwip](https://github.com/RT-Thread-packages/lwip) - LwIP for RT-Thread (upstream).
- [netutils](https://github.com/RT-Thread-packages/netutils) - Networking utilities for RT-Thread.
- [wiznet](https://github.com/RT-Thread-packages/wiznet) - WIZnet TCP/IP chips (such as W5500/W5100) SAL framework implement.
- [zephyr_polling](https://github.com/bobwenstudy/RTT_PACKAGE_zephyr_polling) - Bluetooth BLE Stack.
- [kawaii-mqtt](https://github.com/jiejieTop/kawaii-mqtt) - A kawaii mqtt client based on the socket API, has a very simple api interface, support QoS2、mbedtls.
- [libcurl2rtt](https://github.com/liu2guang/libcurl2rtt) - The curl library ported on the RT-Thread platform.
- [nanopb](https://github.com/RT-Thread-packages/nanopb) - Protocol Buffers for Embedded Systems.
- [tcpserver](https://github.com/Guozhanxin/tcpserver.git) - A TCP server that supports multiple clients.
- [ppp_device](https://github.com/RT-Thread-packages/ppp_device.git) - LwIP PPP porting for Cellular Module( 2G/3G/4G ).
- [at_device](https://github.com/RT-Thread-packages/at_device) - AT component porting or samples for different devices.
- [lorawan_ed_stack](https://github.com/Forest-Rain/lorawan-ed-stack) - Lorawan end-device stack.
- [cyw43xx](https://github.com/RT-Thread-packages/CYW43xx) - CYW43xx WiFi/BT SoC driver.
- [umqtt](https://github.com/RT-Thread-packages/umqtt.git) - A light weight, powerful, customizable, easy-to-use and embeddable mqtt client for RT-Thread!.
- [agile_telnet](https://github.com/loogg/agile_telnet) - TCP debug for Ethernet.
- [pdulib](https://github.com/ShineRoyal/pdulib) - A TEXT parsing library for short messages in PDU format.
- [webclient](https://github.com/RT-Thread-packages/webclient) - Http client library by RT-Thread.
- [wayz_iotkit](https://github.com/wayz-iot/wayz_iotkit) - Wayz iot location software package.
- [btstack](https://github.com/supperthomas/RTT_PACKAGE_BTSTACK.git) - Please add description of btstack in English.
- [NimBLE](https://github.com/RT-Thread-packages/nimble) - An Apache open-source Bluetooth 5.0 stack porting on RT-Thread.
- [smtp_client](https://github.com/WKJay/SMTP_CLIENT) - Smtp client package for rt-thread.
- [llsync_sdk_adapter](https://github.com/supperthomas/LLSync_sdk_adapter) - Please add description of llsync_sdk_adapter in English.
- [zb_coordinator](https://github.com/TaoYang0907/ZB_COORDINATOR_PACKAGE) - Application of AT Command on ZigBee Coordinator.
- [coap](https://github.com/RT-Thread-packages/coap) - A C implementation of the Constrained Application Protocol.
- [webnet](https://github.com/RT-Thread-packages/webnet) - A lightweight, customizable embedded Web Server by RT-Thread.
- [airkissOpen](https://github.com/heyuanjie87/airkissOpen) - Tencent Airkiss Protocol parse library.
- [qmodbus](https://github.com/qiyongzhong0/qmodbus) - A quick and easy to use modbus communication protocol stack.

### Misc

- [kendryte-demo](https://github.com/BernardXiong/kendryte-demo) - Kendryte k210 demo.
- [optparse](https://github.com/RT-Thread-packages/optparse) - Getopt command-line parameter parser bases on RT-Thread.
- [crclib](https://github.com/qiyongzhong0/crclib) - A library of functions with 8-bit ,16-bit ,32-bit crc check calculations.
- [CorevMCU_CLI](https://github.com/Yaochenger/CorevMCU_CLI) - CLI components of Core-V-MCU.
- [fastlz](https://github.com/RT-Thread-packages/fastlz) - Lightning-fast compression library.
- [lwgps](https://github.com/orange2348/lwgps2rtt) - Lightweight GPS NMEA parser.
- [MultiButton](https://github.com/RT-Thread-packages/MultiButton) - A compact and easy to use event-driven button driver.
- [dstr](https://github.com/RT-Thread-packages/dstr) - Dynamic string in C.
- [phase-locked-loop](https://github.com/haodongnj/PLL) - Phase locked loop and frequency locked loop algorithm.
- [state_machine](https://github.com/redoccheng/state_machine) - A feature-rich, yet simple finite state machine (FSM) implementation in C.
- [libcsv](https://github.com/liu2guang/libcsv) - Libcsv is a small, simple and fast CSV library written in pure ANSI C89 that can read and write CSV data.
- [uparam](https://github.com/aeo123/uparam.git) - Manage system parameters with FLASH.
- [hello](https://github.com/RT-Thread-packages/hello) - Package sample for rt-thread.
- [vi](https://github.com/RT-Thread-packages/vi) - The screen-oriented text editor for RT-Thread.
- [armv7m_dwt](https://github.com/sogwms/armv7m_dwt) - Armv7m_dwt High precision timing and delay.
- [FlexibleButton](https://github.com/murphyzhao/FlexibleButton) - Small and flexible button driver.
- [Controller](https://github.com/haodongnj/Controller) - PI, PR and RC controller library.
- [heatshrink](https://github.com/liukangcc/heatshrink.git) - A data compression/decompression library for embedded/real-time systems.
- [filesystem_samples](https://github.com/RT-Thread-packages/filesystem-sample) - RT-Thread filesystem samples.
- [network_samples](https://github.com/RT-Thread-packages/network-sample) - RT-Thread network samples.
- [kernel_samples](https://github.com/RT-Thread-packages/kernel-sample) - A kernel_samples package for rt-thread.
- [peripheral_samples](https://github.com/RT-Thread-packages/peripheral-sample) - RT-Thread peripheral samples.
- [ki](https://github.com/mysterywolf/ki) - Ki is a small text editor in less than 1K lines of code.
- [soem](https://github.com/lg28870983/soem) - SOEM (Source Open EtherCAT master) port to RT-Thread.
- [miniLZO](https://github.com/RT-Thread-packages/miniLZO) - A mini subset of the LZO real-time data compression library.
- [slcan2rtt](https://github.com/cazure/slcan2rtt.git) - Serial / USB serial CAN Adapter (slcan) on RT-Thread.
- [lzma](https://github.com/RiceChen0/lzma) - A compression library with high compression ratio.
- [MFBD](https://github.com/smartmx/MFBD) - Multi-Function Button Detection for MCU.
- [qparam](https://github.com/qiyongzhong0/rt-thread-qparam) - A quick and easy-to-use parameter management component, parameter saving recovery modification and quick access functions are implemented.
- [design_pattern](https://github.com/chenyingchun0312/design_pattern) - Design pattern implementation in C language.
- [minizip](https://github.com/mysterywolf/minizip) - Zip manipulation library.
- [upacker](https://github.com/aeo123/upacker.git) - Building and parsing data frames to be sent over a serial interface.
- [zlib](https://github.com/RT-Thread-packages/zlib) - General purpose data compression library.
- [TinyFrame](https://github.com/XXXXzzzz000/TinyFrame) - A simple library for building and parsing data frames for serial interfaces (like UART / RS232).
- [CanFestival](https://github.com/gbcwbz/canfestival-rtt) - A CanFestival port to RT-Thread operating system.
- [get_irq_priority](https://github.com/wdfk-prog/rt-thread-get_irq_priority) - Get irq priority for Cortex®-M.
- [ralarm](https://github.com/RiceChen0/ralarm) - An alarm clock component that does not rely on hardware and can be infinitely expanded.
- [cal](https://github.com/mysterywolf/cal) - A terminal calendar.
- [cmatrix](https://github.com/wuhanstudio/cmatrix) - Character Rain from the movie "The Matrix".
- [snake](https://github.com/mysterywolf/snake) - A remake of the old nokia game.
- [TinySquare](https://github.com/AlgoOy/TinySquare) - A lightweight square game engine running on Cortex-M.
- [sl](https://github.com/wuhanstudio/sl) - Steam locomotive runs across your terminal when you type 'sl' as you meant to type 'ls'.
- [c2048](https://github.com/mysterywolf/c2048) - An indie puzzle video game run on RT-Thread console.
- [donut](https://github.com/mysterywolf/donut) - A 3D spinning donut.
- [cowsay](https://github.com/wuhanstudio/cowsay) - Cowsay is a program that generates ASCII pictures of a cow with a message.
- [threes](https://github.com/mysterywolf/threes) - An indie puzzle video game which was very popular in the year of 2014.
- [aclock](https://github.com/mysterywolf/aclock) - A terminal clock.
- [morse](https://github.com/zhkag/morse) - Morse code.
- [tetris](https://github.com/volatile-static/rtt_tetris) - Tetris port to RT-Thread console.
- [quicklz](https://github.com/RT-Thread-packages/quicklz) - The world's fastest compression library.

### Peripherals

- [rosserial](https://github.com/wuhanstudio/rt-rosserial) - Robots Operating System (ROS1) on rt-thread.
- [easyblink](https://github.com/Sunwancn/rtt-pkgs-easyblink) - Blink the LED easily and use a little RAM for RT-Thread or RT-Thread Nano.
- [multi_infrared](https://github.com/jsrdczy/rt_thread_multi_infrared_frame) - Multi infrared channels based on rt thread pin and hwtimer.
- [SignalLed](https://github.com/WKJay/SignalLed) - A signal led package for rt-thread.
- [rx8900](https://github.com/Prry/rtt-rx8900) - Extern RTC driver for rx8900.
- [ds3231](https://github.com/Prry/rtt-ds3231) - Extern RTC driver for ds3231.
- [qkey](https://github.com/qiyongzhong0/rt-thread-qkey) - A quick and easy-to-use key driver package.
- [rs485](https://github.com/qiyongzhong0/rt-thread-rs485) - Rs485 driver package.
- [rda58xx](https://github.com/apeng2012/rda58xx) - RDA5820 single-chip broadcase FM transceiver driver.
- [bluetrum_sdk](https://github.com/BLUETRUM/bluetrum_sdk) - Bluetrum sdk.
- [nrfx](https://github.com/xckhmf/nrfx) - Standalone set of drivers for peripherals present in Nordic Semiconductor's SoCs.
- [embARC_bsp](https://github.com/foss-for-synopsys-dwc-arc-processors/embarc_bsp) - Synopsys ARC Processer Board Support Package (BSP) software package.
- [nuclei_sdk](https://github.com/Nuclei-Software/nuclei-sdk) - Nuclei RISC-V Software Development Kit.
- [raspberrypi-pico-sdk](https://github.com/RT-Thread-packages/raspberrypi-pico-sdk) - Raspberry Pi Pico SDK.
- [nrf5x_sdk](https://github.com/supperthomas/nrf5x_sdk) - Software development kit for the nRF52 Series and nRF51 Series SoCs.
- [K210-SDK](https://github.com/RT-Thread-packages/kendryte-k210-sdk) - Kendryte K210 SDK.
- [kendryte-sdk](https://github.com/RT-Thread-packages/kendryte_sdk) - Kendryte K210 SDK.
- [ESP-IDF](https://github.com/RT-Thread-packages/esp-idf) - Espressif IoT Development Framework.
- [stm32l4_cmsis_driver](https://github.com/RT-Thread-packages/stm32l4_cmsis_driver) - STM32 L4 CMSIS driver package.
- [stm32_sdio](https://github.com/RT-Thread-packages/stm32_sdio) - STM32 SDIO controller drivers library.
- [stm32l4_hal_driver](https://github.com/RT-Thread-packages/stm32l4_hal_driver) - STM32 L4 HAL driver package.
- [stm32wb55_sdk](https://github.com/xupenghu/stm32wb55_sdk.git) - Stm32wb55_sdk software package.
- [lrf-nv7lidar](https://github.com/RT-Thread-packages/nv7lidar) - LRF-NV7 laser ranging module.
- [LedBlink](https://github.com/aeo123/LedBlink.git) - Easy led blink support;.
- [io_input_filter](https://github.com/lizdDong/io_input_filter) - IO Input Filter.
- [mcp23008](https://github.com/XiaojieFan/mcp23008.git) - Remote 8-bit I/O expander for I2C-bus.
- [quick_led](https://github.com/qiyongzhong0/rt-thread-qled) - A quick and easy-to-use led driver package.
- [i2c-tools](https://github.com/wuhanstudio/rt-i2c-tools) - A collection of i2c tools including scan/read/write.
- [mfoc](https://github.com/wuhanstudio/mfoc) - Mifare Classic Offline Cracker.
- [agile_button](https://github.com/loogg/agile_button) - A agile button package.
- [dm9051](https://github.com/aozima/dm9051) - DM9051 SPI ethernet driver.
- [max7219](https://github.com/redocCheng/max7219) - A MAX7219 package for the digital tube.
- [nrf24l01](https://github.com/sogwms/nrf24l01) - Single-chip 2.4GHz wireless transceiver.
- [lkdGui](https://github.com/guoweilkd/lkdGui) - LkdGui is a graphical interface for monochrome displays.
- [spi-tools](https://github.com/vandoul/rt-spi-tools) - A collection of spi tools including init/config/trans.
- [aip650](https://github.com/Maihuanyi/aip650) - A quick and easy-to-use digit led and key driver package for aip650 and tm1650.
- [x9555](https://github.com/WennianYan/x9555) - 16-bit 1.65- to 5.5-V I2C/SMBus I/O expander with interrupt, weak pull-up & config registers.
- [ssd1306](https://github.com/luhuadong/rtt-ssd1306) - Drive OLEDs based on SSD1306, SH1106, SH1107 and SSD1309, supports I2C and SPI.
- [agile_console](https://github.com/loogg/agile_console) - Simple debugging device Middleware.
- [Misaka_AT24CXX](https://github.com/xqyjlj/Miaska_AT24CXX) - Misaka-Network for AT24CXX EEPROM.
- [rfm300](https://github.com/kylepengchn/rfm300.git) - ISM Transceiver Module With +20dBm(100mW) Output Power.
- [tca9534](https://github.com/Prry/rtt-tca9534) - A 8-bit I/O expander for i2c-bus.
- [lora_radio_driver](https://github.com/Forest-Rain/lora-radio-driver) - Lora chipset(SX126x\SX127x) driver.
- [pms_series](https://github.com/MrpYoung/pms_series) - Digital universal particle concentration sensor driver library.
- [as608](https://github.com/greedyhao/as608.git) - AS608 fingerprint module driver.
- [tmp1075](https://github.com/Prry/rtt-tmp1075) - Digital temperature sensor driver package for TMP1075.
- [mpu6xxx](https://github.com/RT-Thread-packages/mpu-6xxx) - A package of mpu6xxx driver library, compatible with mpu6000, mpu6050, mpu6500, mpu9250 and other chips.
- [dht11](https://github.com/murphyzhao/dht11_rtt) - Digital temperature and humidity sensor(Single bus).
- [bmp280](https://github.com/nfsq246/RTT_BMP280) - Bmp280 iic drive.
- [sths34pf80](https://github.com/zyk6271/STHS34PF80) - This is the STHS34PF80 sensor driver package.
- [ap3216c](https://github.com/RT-Thread-packages/ap3216c) - A digital ambient light and a proximity sensor ap3216c driver library.
- [bmp180](https://github.com/Prry/rtt-bmp180) - Barometric, temperature.
- [ds18b20](https://github.com/willianchanlovegithub/ds18b20) - A package of digital temperature sensor ds18b20.
- [hs300x](https://github.com/Guozhanxin/hs300x) - Digital humidity and temperature sensor hs300x driver library.
- [bme680](https://github.com/luhuadong/rtt-bme680) - Digital 4-in-1 sensor with gas, humidity, pressure and temperature.
- [qmp6989](https://github.com/kylepengchn/qmp6989.git) - High accuracy and small size barometric pressure sensor,support: barometer, temperature.
- [PAJ7620](https://github.com/orange2348/paj7620) - Gesture sensor PAJ7620 driver package.
- [hmc5883](https://github.com/gmyFighting/hmc5883) - Bmi088 software package.
- [mlx90397](https://github.com/lgnq/mlx90397) - The MLX90397 is the newest addition to the Melexis position sensing portfolio, bringing the highest flexibility in the portfolio's smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%.
- [bme280](https://github.com/RT-Thread-packages/bme280) - Barometric, humidity.
- [hts221](https://github.com/RT-Thread-packages/hts221) - Temperature, humidity.
- [ina226](https://github.com/xupenghu/ina226.git) - Ina226 software package.
- [gp2y10](https://github.com/luhuadong/rtt-gp2y10) - Dust sensor by Sharp for detect air quality.
- [gy271](https://github.com/jch12138/gy271) - A package of gy271 driver library.
- [mlx90393](https://github.com/lgnq/mlx90393) - The MLX90393 is the newest addition to the Melexis position sensing portfolio, bringing the highest fl exibility in the portfolio's smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%.
- [hdc1000](https://github.com/Forest-Rain/hdc1000) - Hdc1000 sensor driver base on RT-Thread sensor frame.
- [bmi160_bmx160](https://github.com/RT-Thread-packages/bmi160_bmx160) - The device driver package for BMX160 and BMI160.
- [max30102](https://github.com/Jackistang/max30102_rtt) - Heart rate and oxygen saturation measure.
- [max31865](https://github.com/SimpleInit/max31865) - A package of digital temperature sensor.
- [sht3x](https://github.com/donghao2nanjing/sht3x) - Digital humidity and temperature sensor sht3x driver library.
- [aht10](https://github.com/RT-Thread-packages/aht10) - Digital humidity and temperature sensor aht10 driver library.
- [bh1750](https://github.com/sanjaywu/bh1750_sensor) - Temperature, humidity.
- [dhtxx](https://github.com/luhuadong/rtt-dhtxx) - DHTxx one-wire digital temperature and humidity sensor.
- [cw2015](https://github.com/qingehao/CW2015) - Fuel gauging system IC for Lithium-ion(Li+) Battery.
- [sht4x](https://github.com/flyingcys/sht4x) - Digital humidity and temperature sensor sht4x driver library.
- [ad7746](https://github.com/wuhanstudio/rt-ad7746) - AD7746  a high resolution, capacitance-to-digital converter (CDC).
- [adt74xx](https://github.com/IoTSharp/ADT74XX) - Digital  temperature sensor adt74xx driver library.
- [ina260](https://github.com/xupenghu/ina260.git) - Ina260 software package.
- [ccs811](https://github.com/luhuadong/rtt-ccs811) - Digital Gas Sensor for Monitoring Indoor Air Quality.
- [isl29035](https://github.com/ShermanShao/isl29035) - Driver library for Renesas Ambient light sensor ISL29035.
- [vl53l0x](https://github.com/Prry/rtt-vl53l0x) - Time of flight sensor driver package for vl53l0x.
- [pmsxx](https://github.com/luhuadong/rtt-pmsxx) - Plantower pms serial PM2.5 sensor driver.
- [da270](https://github.com/MiraMEMS-Wonderful/da270-RT-Thread) - This is the driver package of MiraMEMS DA270 accelerometer for RT-Thread.
- [spl0601](https://github.com/RT-Thread-packages/spl0601) - The Digital Air Pressure Sensor SPL06-01 driver package.
- [max6675](https://github.com/JonasWen/max6675) - A package of digital temperature sensor max6675.
- [balance](https://github.com/xiaogeminghai/balance) - Use hx71xx and weighing pressure sensor to measure weight.
- [lis2dh12](https://github.com/StackRyan/lis2dh12.git) - Accelerometer, tempature.
- [lsm6dsm](https://github.com/my-RT-packages/lsm6dsm.git) - STMicroelectronics's LSM6DSM driver,support Accelerometer/gyro/step count/temperature.
- [sht2x](https://github.com/RT-Thread-packages/sht2x) - Digital humidity and temperature sensor sht2x driver library.
- [lsm303agr](https://github.com/RT-Thread-packages/lsm303agr) - Accelerometer, magnetometer.
- [df220](https://github.com/MiraMEMS-Wonderful/df220-RT-Thread.git) - This is the driver package of MiraMEMS df220 force sensor for RT-Thread.
- [lsm6dsl](https://github.com/RT-Thread-packages/lsm6dsl) - Accelerometer, gyroscope, step.
- [ms5611](https://github.com/sogwms/ms5611) - The Digital Air Pressure Sensor MS5611 driver package.
- [icm20608](https://github.com/RT-Thread-packages/icm20608) - A 3-axis gyroscope and a 3-axis accelerometer driver library.
- [as7341](https://github.com/RiceChen0/as7341) - AS7341 visible light sensor, can measure 8 wavelengths of visible light.
- [rt3020](https://github.com/RichtekTechnology/RT3020) - This is the driver package of RT3020 accelerometer.
- [ms5805](https://github.com/schuck-wang/RTThread-MS5805) - The Digital Air Pressure Sensor MS5805 driver package.
- [mmc3680kj](https://github.com/mumuge1/mmc3680kj) - Mmc3680kj drive.
- [mlx90632](https://github.com/xupenghu/mlx90632.git) - Mlx90632 software package.
- [zmod4410](https://github.com/ShermanShao/zmod4410) - The ZMOD4410 Gas Sensor Module is designed for detecting total volatile organic compounds (TVOC) and monitoring indoor air quality (IAQ).
- [max17048](https://github.com/aeo123/MAX17048.git) - Bat monitor.
- [bmi088](https://github.com/gmyFighting/bmi088) - Bmi088 software.
- [shtc1](https://github.com/nfsq246/RTT_SHTC1) - Temperature, humidity.
- [sr04](https://github.com/alec-shan/hc-sr04) - Driver package for hc-sr04 using rt-thread sensor package.
- [hshcal001](https://github.com/lucaslsh/hshcal001.git) - Temperature, humidity.
- [bma400](https://github.com/RT-Thread-packages/bma400) - Accelerometer, step.
- [tsl4531](https://github.com/JellyYe/tsl4531pkgs.git) - TSL4531 sensor driver package ,support lux.
- [mlx90392](https://github.com/lgnq/mlx90392) - The MLX90392 is the newest addition to the Melexis position sensing portfolio, bringing the highest fl exibility in the portfolio's smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%.
- [sgp30](https://github.com/luhuadong/rtt-sgp30) - Air sensor by Sensirion for detect TVOC and CO2.
- [lps22hb](https://github.com/RT-Thread-packages/lps22hb) - This is the LPS22HB sensor driver package.
- [vsensor](https://github.com/RT-Thread-packages/vsensor) - Virtual sensor device.
- [ws2812b](https://github.com/maplerian/rt_ws2812b) - Ws2812b software driver package for RT-Thread is driven by SPI+DMA.
- [beep](https://github.com/Sunwancn/rtt-pkgs-beep) - Control the buzzer to make beeps at different intervals.
- [libnfc](https://github.com/wuhanstudio/libnfc) - Platform independent Near Field Communication (NFC) library.
- [realtek_ameba](https://github.com/flyingcys/realtek_ameba) - Realtek ameba package on RT-Thread.
- [kobuki](https://github.com/wuhanstudio/kobuki) - Kobuki Robot serial communication driver.
- [infrared](https://github.com/RT-Thread-packages/infrared_framework) - Infrared framework based on rt-thread's pin,pwm and hwtimer driver.
- [pca9685](https://github.com/greedyhao/pca9685) - I2C-bus controlled 16-channel PWM controller.
- [ly68l6400](https://github.com/Ghazigq/ly68l6400) - Device drive for ly68l6400.
- [System_Run_LED](https://github.com/WennianYan/System_Run_LED) - Super simple and practical system running indicator light control thread.
- [nes](https://github.com/Ghazigq/nes) - Nes simulator c Library.
- [micro_ros](https://github.com/wuhanstudio/micro_ros) - ROS 2 on microcontrollers.
- [ili9341](https://github.com/Rbb666/ILI9341.git) - TFT-LCD ILI9341 SPI screen driver software package.
- [lora_gw_driver_lib](https://github.com/Forest-Rain/lora-gw-driver-lib) - Lora-gw-driver-lib is lora gateway chip(SX130x) driver binary libraries.
- [wm_libraries](https://github.com/WinnerMicro/rtpkg-wm_libraries) - A library package for WinnerMicro devices.
- [lora_modem_driver](https://github.com/Forest-Rain/lora-modem-driver) - A serial driver of LoRa(wan) modem.
- [xpt2046](https://github.com/LeeChunHei/xpt2046_touch_rtt) - Xpt2046 touch driver package.
- [ft6236](https://github.com/RT-Thread-packages/ft6236) - This is the driver package of FT6236 touch chip.
- [gt911](https://github.com/RiceChen0/gt911) - Gt911 drivers for RT-Thread.
- [gt917s](https://github.com/lilisheng411527/gt917s.git) - Gt917s drivers for RT-Thread.
- [ft5426](https://github.com/liuduanfei/ft5426) - This is the driver package of FT5426 touch chip.
- [gt9147](https://github.com/RT-Thread-packages/gt9147) - This is the GT9147 touch driver package.
- [cst816x](https://github.com/Z8MAN8/cst816x) - Cst816x drivers for RT-Thread.
- [gt1151](https://github.com/Jackistang/GT1151) - Gt1151 drivers for RT-Thread.
- [cst812t](https://github.com/StackYuan/cst812t) - Cst812t drivers for RT-Thread.
- [ft6206](https://github.com/RT-Thread-packages/ft6206) - This is the driver package of FT6206 touch chip.
- [bt_mx01](https://github.com/qiyongzhong0/rt-thread-bt_mx01) - Device driver of BT chip MX-01.
- [vs1003](https://github.com/beisongcrt/vs1003.git) - Vs1003 driver.
- [tmc51xx](https://github.com/apeng2012/tmc51xx) - TMC5160 power driver for stepper motors.
- [fingerprint](https://github.com/pk-ing/fingerprint) - Fingerprint module driver.
- [uat](https://github.com/qiyongzhong0/rt-thread-uat) - Micro AT device driver interface component.
- [can_ymodem](https://github.com/redocCheng/rt_can_ymodem) - A device connect can & ymodem.
- [soft_serial](https://github.com/qiyongzhong0/rt-thread-soft-serial) - A software serial driver package by using the hardware timer capture / comparison functionality.
- [mb85rs16](https://github.com/XiaojieFan/mb85rs16.git) - Memory FRAM 16K(2Kx8)Bit SPI Driver Library.
- [pcf8574](https://github.com/RT-Thread-packages/pcf8574) - Remote 8-bit I/O expander for I2C-bus.
- [ld3320](https://github.com/xqyjlj/ld3320) - LD3320 speech recognition chip.
- [RgPower](https://github.com/1300650671/RgPower) - Power value get module driver.
- [button](https://github.com/jiejieTop/rtpkg_button) - Button drive by C, support single and double click, long press, long press release.
- [bt_ecb02c](https://github.com/qiyongzhong0/rt-thread-bt_ecb02c) - Device driver of BT chip ECB02C.
- [at24cxx](https://github.com/XiaojieFan/at24cxx) - Eeprom at24cxx driver library.
- [st7789](https://github.com/Vandoul/ST7789.git) - TFT-LCD ST7789 SPI Graphic driver.
- [sgm706](https://github.com/Prry/rtt-sgm706) - Independent watchdog driver package for sgm706.
- [rc522](https://github.com/greedyhao/rc522_rtt) - Rc522 rfid module driver.
- [littled](https://github.com/luhuadong/rtt-littled) - Littled LED Daemon for LED driver.
- [MotionDriver2RTT](https://github.com/greedyhao/MotionDriver2RTT) - A package porting MotionDriver to RTT.
- [multi_rtimer](https://github.com/Forest-Rain/multi-rtimer) - A real-time and low power software timer module.
- [rs232](https://github.com/diskwu/RTTHREAD_RS232) - Rs232 driver package.
- [sx12xx](https://github.com/XiaojieFan/sx12xx) - Semtech  LoRa RF chip driver library.
- [rplidar](https://github.com/wuhanstudio/rplidar) - A low cost LIDAR sensor suitable for indoor robotic SLAM application.
- [vdevice](https://github.com/RT-Thread-packages/vdevice) - A virtual IO peripheral environment.
- [agile_led](https://github.com/loogg/agile_led) - A agile led package.
- [wk2124](https://github.com/MrMichael/wk2124) - Wk2124(spi to uart) driver library.
- [Misaka_RGB_Bling](https://github.com/xqyjlj/Misaka_RGB_Bling) - Misaka-Network for RGB LED Bling.

### Multimedia

- [NUemWin](https://github.com/wosayttn/NUemWin) - A NUemWin package for rt-thread.
- [LVGL](https://github.com/lvgl/lvgl) - Light and Versatile Graphics Library (official upstream).
- [lv_music_demo](https://github.com/RT-Thread-packages/lv_demo_music) - LVGL music player demo for RT-Thread.
- [LittlevGL2RTT](https://github.com/liu2guang/LittlevGL2RTT) - LittlevGL graphics library (LVGL 7.x, legacy).
- [gui_guider_demo](https://github.com/NXPmicro/gui-guider-demos.git) - LVGL demo generated by GUI Guider.
- [TJpgDec](https://github.com/RT-Thread-packages/TJpgDec) - Tiny JPEG Decompressor.
- [mcurses](https://github.com/wuhanstudio/mcurses) - Micro ncurses library.
- [persimmon](https://github.com/RT-Thread-packages/persimmon) - Persimmon UI for RT-Thread.
- [mp3player](https://github.com/MrzhangF1ghter/mp3player) - A simple mp3 format music player.
- [3gpp_amrnb](https://github.com/myshowtogo/3gpp_amrnb) - 3gpp amrnb codec library.
- [touchgfx2rtt](https://github.com/Aladdin-Wang/touchgfx2rtt.git) - A touchgfx package for rt-thread.
- [vt100](https://github.com/wuhanstudio/vt100) - Iridescent drawing library on MSH.
- [u8g2](https://github.com/wuhanstudio/rt-u8g2) - U8g2 library for rt-thread (legacy).
- [u8g2-official](https://github.com/olikraus/u8g2) - U8g2 library (official upstream).
- [gui_engine](https://github.com/RT-Thread-packages/gui_engine) - GUI Engine by RT-Thread.
- [STemWin](https://github.com/loogg/STemWin) - A STemWin package for rt-thread.
- [mupdf](https://github.com/rtoslab/mupdf-rtt) - A lightweight PDF, XPS, and E-book viewer.
- [openmv](https://github.com/RT-Thread-packages-by-SummerGift/openmv) - Openmv porting for rt-thread.
- [termbox](https://github.com/mysterywolf/termbox) - Library for writing text-based user interfaces.
- [wavplayer](https://github.com/RT-Thread-packages/wavplayer) - Minimal music player for wav file play and record.
- [PDFGen](https://github.com/mysterywolf/PDFGen) - Simple C PDF Writer/Generation library.
- [TinyJPEG](https://github.com/StackRyan/TinyJPEG) - A light-weight JPEG encoder package.
- [helix](https://github.com/liuduanfei/helix) - The Helix MP3 Decoder.
- [qrcode](https://github.com/RT-Thread-packages/qrcode) - A simple library for generating QR codes in C.
- [ugui](https://github.com/xidongxu/ugui.git) - Open source graphics library ugui ported to rtthread.
- [AzureGUIX](https://github.com/HelloByeAll/AzureGUIX) - Microsoft THREADX system middleware AzureGUIX.

### AI

- [nnom](https://github.com/majianjia/nnom) - A higher-level Neural Network framework on Microcontroller (NNoM).
- [quest](https://github.com/wuhanstudio/QuEST) - A simulator of quantum computers on MCU.
- [onnx-backend](https://github.com/wuhanstudio/onnx-backend) - Open Neural Network Exchange backend on RT-Thread.
- [elapack](https://github.com/wuhanstudio/elapack) - Linear algebra library for embedded devices, compatible with matlab.
- [onnx-parser](https://github.com/wuhanstudio/rt-onnx-parser) - Open Neural Network Exchange model parser in C.
- [TensorflowLiteMicro](https://github.com/QingChuanWS/TensorflowLiteMicro) - A lightweight deep learning inference framework based on Google Tensorflow Lite for RT-Thread operating system.
- [libann](https://github.com/wuhanstudio/rt-libann) - A light-weight ANN library, capable of training, saving and loading models.
- [ulapack](https://github.com/wuhanstudio/ulapack) - Linear algebra library for embedded devices.
- [ncnn](https://github.com/yc66542260/ncnn-rtthread) - NCNN package for RT-Thread.
- [r-tinymaix](https://github.com/RiceChen0/r-tinymaix) - R-tinymaix TinyMaix is a tiny inference Neural Network library specifically for microcontrollers (TinyML).
- [naxos](https://github.com/wuhanstudio/naxos) - A C++ Constraint Programming Library.

### Security

- [mbedtls](https://github.com/RT-Thread-packages/mbedtls) - An open source, portable, easy to use, readable and flexible SSL library.
- [libsodium](https://github.com/RT-Thread-packages/libsodium-legacy) - A modern and easy-to-use crypto library (NOT Recommended for MCU. Use libhydrogen instead).
- [tinycrypt](https://github.com/RT-Thread-packages/tinycrypt) - A simple and configurable crypt library.
- [yd_crypto](https://github.com/china-hai/yd_crypto) - Encryption and decryption algorithm library for microcontroller.
- [libhydrogen](https://github.com/wuhanstudio/libhydrogen) - A lightweight, secure, easy-to-use crypto library suitable for constrained environments.
- [trusted-firmware-m](https://github.com/RT-Thread-packages/trusted-firmware-m) - Trusted firmware for M class.

### System

- [lwext4](https://github.com/RT-Thread-packages/lwext4) - An excellent choice of ext2/3/4 filesystem for microcontrollers.
- [mcuboot](https://github.com/iysheng/rt_mcuboot.git) - A common infrastructure for the bootloader, system flash layout on microcontroller systems.
- [qboot](https://github.com/qiyongzhong0/rt-thread-qboot) - A component used to make bootloader quickly.
- [cairo](https://github.com/RT-Thread-packages/cairo) - Multi-platform 2D graphics library.
- [TinyUSB](https://github.com/RT-Thread-packages/tinyusb) - An open source cross-platform USB stack for embedded system.
- [reb](https://github.com/RiceChen0/reb) - Event broker component based on publish subscribe.
- [uffs](https://github.com/RT-Thread-packages/uffs) - Ultra-low-cost Flash File System.
- [TFDB](https://github.com/smartmx/TFDB) - Tiny Flash Database for MCU.
- [sfdb](https://github.com/WKJay/sfdb) - Simple file database.
- [yaffs2](https://github.com/heyuanjie87/yaffs2_rtt_port) - Yaffs2 port to rtthread.
- [rti](https://github.com/RT-Thread-packages/rti) - RT-Thread insight, a probe tool for RT-Thread to help to analyze internal behavior of the system.
- [r-rhealstone](https://github.com/RiceChen0/r-rhealstone) - A cross platform real-time system benchmark testing framework.
- [perf_counter](https://github.com/RT-Thread-packages/perf_counter) - A dedicated performance counter for Cortex-M systick.
- [syswatch](https://github.com/qiyongzhong0/rt-thread-syswatch) - A component used to ensure the long-term normal running of the system.
- [openamp](https://github.com/bigmagic123/openamp.git) - OpenAMP for rt-thread.
- [tz-database](https://github.com/RT-Thread-packages/tz) - Time zone database and code.
- [sqlite](https://github.com/RT-Thread-packages/SQLite) - SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine.
- [levelx](https://github.com/RT-Thread-packages/levelx.git) - Threadx's wear-leveling component.
- [event_recorder](https://github.com/RT-Thread-packages/event_recorder) - A lightweight event record and replay tools for debug and test.
- [FreeRTOS_Wrapper](https://github.com/RT-Thread-packages/FreeRTOS-Wrapper) - FreeRTOS Application Compatibility Layer for RT-Thread.
- [FlashDB](https://github.com/armink/FlashDB) - A lightweight database that supports key-value and time series data.
- [Qfplib_M3](https://github.com/mysterywolf/Qfplib-M3) - A free, fast and accurate ARM Cortex-M3 floating-point library.
- [Qfplib_M0_full](https://github.com/mysterywolf/Qfplib-M0-full) - A free, fast and compact ARM Cortex-M0 floating-point library.
- [Qfplib_M0_tiny](https://github.com/mysterywolf/Qfplib-M0-tiny) - A free ARM Cortex-M0 floating-point library in 1 kbyte.
- [flash_blob](https://github.com/Aladdin-Wang/flash_blob.git) - Tool for quickly generating flash driver files.
- [fal](https://github.com/RT-Thread-packages/fal) - Flash Abstraction Layer implentment. Manage flash device and partition.
- [Arm-2D](https://github.com/liuduanfei/Arm-2D) - Arm-2D Graphics Library.
- [jffs2](https://github.com/RT-Thread-packages/jffs2) - Journalling Flash File System Version2.
- [plccore](https://github.com/hyafz/plccore) - Plccore for RT-Thread.
- [agile_upgrade](https://github.com/loogg/agile_upgrade) - Middleware for fast building bootloader.
- [qpc](https://github.com/Zhyolo/qpc-rtthread) - Lightweight Real-Time Embedded Framework QP/C.
- [CMSIS-NN](https://github.com/RT-Thread-packages/CMSIS-NN) - Efficient Neural Network Kernels for Arm Cortex-M CPUs.
- [CMSIS_RTOS2](https://github.com/RT-Thread-packages/CMSIS_RTOS2) - CMSIS-RTOS2 wrapper for RT-Thread.
- [CMSIS_5](https://github.com/ARM-software/CMSIS_5) - CMSIS-5 Development.
- [CMSIS_RTOS1](https://github.com/RT-Thread-packages/CMSIS_RTOS1) - CMSIS-RTOS1 wrapper for RT-Thread.
- [CMSIS_5_AUX](https://github.com/RT-Thread-packages/CMSIS_5_AUX) - CMSIS-5 Auxiliary Package.
- [CMSIS-Core](https://github.com/RT-Thread-packages/CMSIS-Core) - Standardized API for the Cortex-A/M processor core and peripherals.
- [TaskMsgBus](https://github.com/slyant/TaskMsgBus.git) - For sending and receiving text/object messages between threads based on RT-Thread.
- [thread_pool](https://github.com/armink-rtt-pkgs/thread_pool) - A thread pool base on RT-Thread.
- [kmulti_rtimer](https://github.com/kylepengchn/kmulti_rtimer.git) - A multi timer for rt-thread.
- [Ppool](https://github.com/mysterywolf/Ppool) - Pthread-based thread pool library.
- [CherryUSB](https://github.com/cherry-embedded/CherryUSB) - Tiny and portable USB host/device stack for embedded system with USB IP.
- [littlefs](https://github.com/RT-Thread-packages/littlefs) - A little fail-safe filesystem designed for microcontrollers.
- [sys_load_monitor](https://github.com/armink-rtt-pkgs/sys_load_monitor) - System load monitor.
- [rt-robot](https://github.com/RT-Thread-packages/rt-robot) - RT-Thread Robots platform.
- [LiteOS-SDK](https://github.com/RT-Thread-packages/LiteOS-SDK) - LiteOS SDK.
- [rt_vsnprintf_full](https://github.com/mysterywolf/rt_vsnprintf_full) - Fully functional version of rt_vsnprintf.
- [rt_memcpy_cm](https://github.com/mysterywolf/rt_memcpy_cm) - Cortex-M kernel assembly accelerated version of rt_memcpy function.
- [rt_kprintf_threadsafe](https://github.com/mysterywolf/rt_kprintf_threadsafe) - Thread-safe version of rt_kprintf.
- [rpmsg-lite](https://github.com/flyingcys/rpmsg-lite) - Rpmsg-lite for rt-thread.
- [partition](https://github.com/RT-Thread-packages/partition) - A partition management package bases on block device.
- [EV](https://github.com/sogwms/EV) - Framework for efficient development of vehicles (including drones).
- [mlibc](https://github.com/plctlab/mlibc) - Embedded libc, especially for RISC-V.
- [minIni](https://github.com/hichard/minIni) - MinIni for RT-Thread.
- [pixman](https://github.com/RT-Thread-packages/pixman) - A library that provides low-level pixel manipulation.
- [ramdisk](https://github.com/majianjia/ramdisk) - A RAM memory block device.
- [tlsf](https://github.com/RT-Thread-packages/tlsf) - TLSF is a dynamic memory allocation algorithm with predictable execution time and low fragmentation.
- [filex](https://github.com/RT-Thread-packages/filex) - Fiex in rttthread.
- [rtp](https://github.com/RiceChen0/rtp) - Rtp Cross platform thread pool.
- [uC_Modbus](https://github.com/mysterywolf/uC-Modbus-for-RT-Thread) - UC/Modbus for RT-Thread.
- [uCOSIII_Wrapper](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-III) - ΜC/OS-III RTOS Application Compatibility Layer for RT-Thread.
- [uC_Common](https://github.com/mysterywolf/uC-Common-for-RT-Thread) - UC/Common for RT-Thread.
- [uCOSII_Wrapper](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-II) - ΜC/OS-II RTOS Application Compatibility Layer for RT-Thread.
- [uC_CLK](https://github.com/mysterywolf/uC-Clk-for-RT-Thread) - UC/Clk for RT-Thread.
- [uC_CRC](https://github.com/mysterywolf/uC-CRC-for-RT-Thread) - UC/CRC for RT-Thread.
- [lpm](https://github.com/RT-Thread-packages/lpm) - Logical partition management. Manage storage device and partition.

### Language

- [jerryscript](https://github.com/RT-Thread-packages/jerryscript) - JerryScript port for RT-Thread.
- [simple_xml](https://github.com/xfwangqiang/simple_xml) - Based on the XML parser of the C language, the purpose of this project is to develop a code that can be applied on multiple platforms. At present, the code has been applied to MAINSTREAM OPERATING SYSTEMS SUCH AS WIN10, LINUX, RT-thread, VxWorks and so on.
- [ezXML](https://github.com/RT-Thread-packages/ezXML) - An XML parser C library that's simple and easy to use.
- [LuatOS](https://github.com/openLuat/luatos-soc-rtt) - Powerful embedded Lua Engine for IoT devices.
- [micropython](https://github.com/RT-Thread-packages/micropython) - MicroPython port package for RT-Thread.
- [pikascript](https://github.com/pikasTech/pikascript) - Lightweight Python scripting support tool that is easy to customize.
- [rapidjson](https://github.com/wuhanstudio/rapidjson) - A fast JSON parser/generator for C++ with both SAX/DOM style API.
- [parson](https://github.com/IoTSharp/parson) - Parson is a lightweight json library written in C,write by kgabis.
- [rt_cjson_tools](https://github.com/maplerian/rt_cjson_tools) - Cjson tools library for RT thread.
- [cJSON](https://github.com/RT-Thread-packages/cJSON) - Ultralightweight JSON parser in ANSI C.
- [ljson](https://github.com/qiaoqidui/ljson) - JSON parser in ANSI C.
- [agile_jsmn](https://github.com/loogg/agile_jsmn) - Lightweight JSON parser.
- [jsmn](https://github.com/RT-Thread-packages/jsmn) - Jsmn is a world fastest JSON parser/tokenizer.
- [Lua](https://github.com/liu2guang/Lua2RTT) - Lua port package for RT-Thread.
- [rtt_rust](https://github.com/vito-chl/rtt_rust.git) - Rust support for rt-thread.

### Signal process

- [DigitalCtrl](https://github.com/xuzhuoyi/DigitalCtrl) - Digital closed-loop control algorithm library.
- [qpid](https://github.com/qiyongzhong0/rt-thread-qpid) - A quick and easy-to-use PID automatic control algorithm package, that supports incremental and positional algorithms.
- [CMSIS-DSP](https://github.com/RT-Thread-packages/CMSIS-DSP) - CMSIS-DSP embedded compute library for Cortex-M and Cortex-A.
- [kissfft](https://github.com/mborgerding/kissfft) - A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid.
- [ukal](https://github.com/wuhanstudio/ukal) - Kalman filter based on ulapack.
- [fire_pid_curve](https://github.com/LONGZR007/fire_pid_curve.git) - Fire PID communication protocol debugging assistant.

### Tools

- [SEGGER_RTT](https://github.com/supperthomas/RTTHREAD_SEGGER_TOOL.git) - Use the SEGGER RTT instead of console.
- [vconsole](https://github.com/enkiller/vconsole) - A virtual console package.
- [rtt_auto_exe_cmd](https://github.com/supperthomas/RTT_AUTO_EXE_CMD.git) - Execute the rt-thread cmd auto for ci.
- [logmgr](https://github.com/RT-Thread-packages/logmgr.git) - A log management system for rt-thread.
- [EasyFlash](https://github.com/armink-rtt-pkgs/EasyFlash) - Lightweight embedded flash memory library. Make flash to be a small KV database.
- [cBox](https://github.com/enkiller/cbox) - C language box.
- [EasyLogger](https://github.com/armink-rtt-pkgs/EasyLogger) - A ultra-lightweight(ROM<1.6K, RAM<0.3k), high-performance C/C++ log library.
- [devmem](https://github.com/luanxg/devmem) - Read/write memory/register tools.
- [bs8116a](https://github.com/illusionlee/bs8116a.git) - Touch key of HOLTEK BS8116A-3.
- [cpu_usage](https://github.com/enkiller/cpu_usage) - CPU usage statistics tool.
- [anv_bench](https://github.com/wuhanstudio/anv_bench) - Quick-and-dirty benchmarking system for quick prototyping.
- [adbd](https://github.com/heyuanjie87/adbd) - Android Debug Bridge daemon implementation on RT-Thread.
- [zdebug](https://github.com/beisongcrt/zdebug.git) - Convenient debugging tool, control print log at any time, view, set variable data, execute functions.
- [lwlog](https://github.com/wuhanstudio/lwlog) - Single header logging library.
- [vofa_plus](https://github.com/xiaogeminghai/vofa_plus) - Realize serial port waveform function with vfoa+.
- [rdb](https://github.com/RT-Thread-packages/rdb) - RT-Thread Debug Bridge.
- [lunar_calendar](https://github.com/illusionlee/lunar_calendar.git) - A tool to convert a Gregorian calendar date into a lunar calendar.
- [uMCN](https://github.com/JcZou/uMCN) - UMCN is a light-weight and powerful IPC module based on the publisher/subscriber model.
- [ulog_easyflash](https://github.com/armink-rtt-pkgs/ulog_easyflash) - The ulog flash plugin by EasyFlash.
- [snowflake](https://github.com/2022alpha/snowflake) - Snowflake algorithm is a distributed ID generation algorithm.
- [UrlEncode](https://github.com/jch12138/UrlEncode.git) - A simple tool to Encode/Decode Url.
- [solar_terms](https://github.com/XYX12306/solar_terms.git) - A tool package for judging the relationship between 24 solar terms according to the date.
- [anv_testsuit](https://github.com/wuhanstudio/anv_testsuit) - Minimalist C/C++ unit test framework.
- [wamr](https://github.com/bytecodealliance/wasm-micro-runtime.git) - WebAssembly Micro Runtime For RT-Thread.
- [anv_trace](https://github.com/wuhanstudio/anv_trace) - Trace the program flow.
- [nr_micro_shell](https://github.com/Nrusher/nr_micro_shell) - Lightweight command line interaction tool.
- [anv_memleak](https://github.com/wuhanstudio/anv_memleak) - Check if there are memleaks.
- [ulog_file](https://github.com/RT-Thread-packages/ulog_file.git) - The ulog file backend by filesystem.
- [lwrb2rtt](https://github.com/Jackistang/lwrb2rtt) - Lightweight ring buffer manager.
- [gps_rmc](https://github.com/maplerian/gps_rmc) - Used to parse $XXRMC type data of GPS module.
- [gan_zhi](https://github.com/XYX12306/gan_zhi.git) - A tool package to get tiangan and dizhi informations according to the date and time.
- [SystemView](https://github.com/RT-Thread-packages/SEGGER_SystemView) - SEGGER SystemView.
- [CoreMark](https://github.com/wuhanstudio/coremark) - EEMBC's CoreMark® is a benchmark that measures the performance of microcontrollers (MCUs) and central processing units (CPUs) used in embedded systems.
- [hash-match](https://github.com/smartmx/hash-match) - Using hashmap on MCUs.
- [fdt](https://github.com/RT-Thread-packages/fdt) - Device Tree package in RT-Thread.
- [RT_Trace](https://github.com/Ruboom/RT_Trace) - Using J-Link realizes event monitoring.
- [kdb](https://github.com/RT-Thread-packages/kdb) - Kernel debug tools.
- [armv7m_DWT](https://github.com/balanceTWK/armv7m_DWT.git) - Memory monitoring component based on ARMV7M architecture.
- [MemoryPerf](https://github.com/SummerLife/MemoryPerf) - Memory Performance Testing for ARM CPU.
- [Dhrystone](https://github.com/wuhanstudio/dhrystone) - Dhrystone is a benchmark that measures the performance of microcontrollers (MCUs) and central processing units (CPUs) used in embedded systems.
- [mbedtls_bench](https://github.com/xfan1024/rttpkg-mbedtls_bench) - Performance test for mbedtls.
- [mem_sandbox](https://github.com/mysterywolf/mem_sandbox) - Memory sandbox for RT-Thread.
- [gbk2utf8](https://github.com/Ghazigq/gbk2utf8) - Conversion between GBK and UTF8.
- [Micro-XRCE-DDS-Client](https://github.com/JcZou/Micro-XRCE-DDS-Client) - The middleware component of micro-ros, which provides ros2 topic pub/sub ability.
- [ChineseFontLibrary](https://github.com/lxzzzzzxl/Chinese_font_library) - A Chinese_font_library for rt-thread.
- [regex](https://github.com/thread-liu/tiny-regex-c.git) - A small regex implementation in C.
- [CmBacktrace](https://github.com/armink-rtt-pkgs/CmBacktrace) - Advanced fault backtrace library for ARM Cortex-M series MCU.
