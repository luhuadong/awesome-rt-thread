# Awesome RT-Thread [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> RT-Thread is an open source, neutral, and community-based real-time operating system (RTOS) for embedded systems and Internet of things (IoT). It is developed by the RT-Thread Development Team based in China. 

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
  - [sdk-bsp-ra8d1-vision-board](https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board) - SDK for the Vision-Board development board.
- [Gitee](https://gitee.com/rtthread) - RT-Thread Gitee organization.
  - [rt-thread](https://gitee.com/rtthread/rt-thread) - RT-Thread Gitee repository.
  - [docs-online](https://gitee.com/rtthread/docs-online) - RT-Thread documentation repository.
- [RT-Thread-Mirror](https://gitee.com/RT-Thread-Mirror) - RT-Thread packages mirror in gitee.com.
- [youtube](https://www.youtube.com/@rt-thread) / [bilibili](https://space.bilibili.com/423462075/) - Tutorial videos and conference videos.
- [medium](https://rt-thread.medium.com) / [linkedin](https://www.linkedin.com/company/rt-thread-iot-os/) / [twitter](https://twitter.com/rt_thread) / [facebook](https://www.facebook.com/profile.php?id=100066719216600) - Various social feeds.
- ![](https://www.rt-thread.org/static/imgs/footer/foot_code.png) - WeChat official account QR code.



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
- [ART-Pi](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h750-realthread-artpi) - A DIY open source hardware based on STM32H750 designed by the RT-Thread team.
- [Spark (星火1号)](https://github.com/RT-Thread-Studio/sdk-bsp-stm32f407-spark) - An RTOS development learning board based on STM32F407 specially designed for engineers and college students.
- [HMI Board](https://github.com/RT-Thread-Studio/sdk-bsp-ra6m3-hmi-board) - A high-cost-performance graphic evaluation kit brought to you by RT-Thread in collaboration with Renesas and LVGL.
- [Vision Board](https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board) - A development board with camera based on the Renesas RA8D1 (Cortex-M85).



## Projects

- [Firmament (FMT)](https://github.com/Firmament-Autopilot/FMT-Firmware) - Firmament Autopilot Embedded System.
- [RTduino](https://github.com/RTduino/RTduino) - The Arduino ecosystem compatibility layer for RT-Thread.



## Packages


### IoT

- [protobuf-c](https://github.com/wuhanstudio/protobuf-c) - protobuf-c library for rt-thread. `MIT`
- [EmbeddedProto](https://github.com/wuhanstudio/EmbeddedProto) - A C++ Protocol Buffers implementation specifically suitable for ARM Cortex-M MCUs. `GPL-3.0`
- [agile_ftp](https://github.com/loogg/agile_ftp) - Lightweight ftp server. `LGPL-2.1`
- [mavlink](https://github.com/sogwms/mavlink) - A very lightweight messaging protocol for communicating. `Apache-2.0`
- [zFTP](https://github.com/longtengmcu/zFTP.git) - Please add description of zFTP in English. `Apache-2.0`
- [ipmsg](https://github.com/heyuanjie87/ipmsg) - A LAN instant messaging implement in RT-Thread. `Apache-2.0`
- [dlt645](https://github.com/WKJay/DLT645) - dlt645 master package. `LGPL-2.1`
- [net_server](https://github.com/WKJay/net-server) - Net server supports TCP/TLS. `Apache-2.0`
- [small_modbus](https://github.com/cazure/small_modbus.git) - small modbus. `Apache-2.0`
- [atsrv_socket](https://github.com/RT-Thread-packages/atsrv_socket) - AT server with socket commands. `Apache-2.0`
- [bc28_mqtt](https://github.com/luhuadong/rtt-bc28-mqtt) - connect to Aliyun with Quectel BC28 model. `Apache-2.0`
- [mongoose](https://github.com/armink-rtt-pkgs/mongoose) - Embedded Web Server Library for RT-Thread package. `GPL-2.0`
- [lora_pkt_fwd](https://github.com/Forest-Rain/lora-pkt-fwd) - lora_pkt_fwd is lora(wan) packet forward based on Semtech GWMP. `Apache-2.0`
- [agile_modbus](https://github.com/loogg/agile_modbus) - Lightweight modbus protocol stack. `Apache-2.0`
- [ota_downloader](https://github.com/RT-Thread-packages/ota_downloader) - The firmware downloader bases on RT-Thread OTA component. `Apache-2.0`
- [matter-adaptation-layer](https://github.com/kurisaW/MATTER-Adaptation_Layer) - Matter protocol stack porting on RT-Thread based on guidance from Connectivity Standards Alliance (CSA) Working Group. `Apache-2.0`
- [wlan_cyw43012](https://github.com/Guozhanxin/cyw43012-RTT) - wlan driver from CYW43012. `Apache-2.0`
- [wlanmarvell](https://github.com/JianRuiqian/marvellwifi) - Marvell WiFi driver for rt-thread. `GPL-2.0`
- [rw007](https://github.com/RT-Thread-packages/rw007) - RW007 (SPI Wi-Fi module) driver for RT-Thread. `Apache-2.0`
- [wlan_wiced](https://github.com/RT-Thread-packages/wlan-wiced) - wlan driver from WICED. `GPL-2.0`
- [wlan_bl808](https://github.com/flyingcys/wlan_bl808_rtthread) - wlan driver from BL808. `Apache-2.0`
- [wlan_cyw43439](https://github.com/Z8MAN8/cyw43439-RTT) - wlan driver from CYW43439. `Apache-2.0`
- [abup_fota](https://github.com/RayShen1018/Abup) - The firmware downloader bases on abup FOTA component. `Apache-2.0`
- [bt_cyw43012](https://github.com/Guozhanxin/cyw43012-ble-RTT) - bt driver from CYW43012. `Apache-2.0`
- [bsal](https://github.com/RT-Thread-packages/bsal) - The Bluetooth Stack Layer. `Apache-2.0`
- [lssdp](https://github.com/RT-Thread-packages/lssdp.git) - Lssdp protocol implemented on rt-thread. `MIT`
- [hm](https://github.com/Jackistang/HCI-Middleware) - A generic Bluetooth HCI transport layer. `Apache-2.0`
- [GAgent](https://github.com/RT-Thread-packages/GAgent) - GAgent of Gizwits on RT-Thread. `LGPL-2.1`
- [ali-iotkit](https://github.com/RT-Thread-packages/ali-iotkit) - Ali Cloud SDK for IoT platform. `Apache-2.0`
- [joylink](https://github.com/RT-Thread-packages/joylink) - Joylink Cloud SDK for IoT platform. `Apache-2.0`
- [onenet](https://github.com/RT-Thread-packages/onenet) - China Mobile OneNet cloud SDK for RT-Thread. `LGPL-2.1`
- [ucloud_iot_sdk](https://github.com/ucloud/ucloud-iot-rtthread-package.git) - ucloud iot sdk for uiot-core platform. `Apache-2.0`
- [azure-iot-sdk](https://github.com/RT-Thread-packages/azure-iot-sdk) - Microsoft azure cloud SDK for RT-Thread. `MIT`
- [tencent-iot-sdk](https://github.com/tencentyun/tencent-cloud-iot-package-for-rtthread) - Tencent Cloud IOT SDK for iot_explorer platform. `MIT`
- [iotsharp-c-sdk](https://github.com/IoTSharp/iotsharp-rtthread-package) - IoTSharp client sdk for RT-Thread. `MIT`
- [jiot-c-sdk](https://github.com/jpush/JIoT-rtthread-package.git) - JIGUANG IoT cloud client sdk for RT-Thread. `MIT`
- [nmealib](https://github.com/ShineRoyal/nmealib) - A nmelib library porting on RT thread. `LGPL-2.1`
- [lhc_modbus](https://github.com/LHC324/lhc_modbus) - Lightweight and high-performance C language modbus protocol stack. `Apache-2.0`
- [lorawan_driver](https://github.com/zyk6271/LoRaWAN_Driver) - Support for LoRaWAN Network with RT-Thread. `Apache-2.0`
- [nopoll](https://github.com/RT-Thread-packages/nopoll) - A OpenSource WebSocket implementation (RFC 6455) in ansi C. `LGPL-2.1`
- [cmux](https://github.com/RT-Thread-packages/cmux) - connection multiplexing protocol for RT-Thread, support GSM0710 .etc. `Apache-2.0`
- [rt-link_hw](https://github.com/RT-Thread-packages/rt-link_hw) - The underlying communication port adaptation layer of the rt-link component. `Apache-2.0`
- [RyanW5500](https://github.com/Ryan-CW-Code/RyanW5500) - W5500 BSD socket implementation. `Apache-2.0`
- [lora_pkt_sniffer](https://github.com/Forest-Rain/lora-pkt-sniffer) - lora_pkt_sniffer is a sniffer tool of lora(wan) packet. `Apache-2.0`
- [WebTerminal](https://github.com/armink-rtt-pkgs/WebTerminal) - Terminal runs in a Web browser. `unknown`
- [mymqtt](https://github.com/hichard/mymqtt) - Eclipse Paho MQTT C/C++ client for Embedded platforms.A new efficient and stable way to realize for rt-thread. `EPL-1.0`
- [capnp](https://github.com/wuhanstudio/capnp) - Cap'n Proto serialization/RPC system which is faster than protobuf. `MIT`
- [qxwz](https://github.com/RT-Thread-packages/qianxun.git) - high precision location library for RT-Thread. `Apache-2.0`
- [librws](https://github.com/RT-Thread-packages/librws) - Tiny, cross platform websocket client C library. `MIT`
- [RyanMqtt](https://github.com/Ryan-CW-Code/RyanMqtt) - RyanMqtt client library provides an implementation of the MQTT 3.1.1 specification. It is optimized for resource constrained devices. `Apache-2.0`
- [pahomqtt](https://github.com/RT-Thread-packages/paho-mqtt) - Eclipse Paho MQTT C/C++ client for Embedded platforms. `EPL-1.0`
- [freemodbus](https://github.com/RT-Thread-packages/freemodbus) - Modbus master and slave stack. `BSD`
- [wol](https://github.com/WKJay/wol) - wake on lan package for rt-thread. `Apache-2.0`
- [lwip](https://github.com/RT-Thread-packages/lwip) - LwIP for RT-Thread (upstream). `BSD`
- [netutils](https://github.com/RT-Thread-packages/netutils) - Networking utilities for RT-Thread. `Apache-2.0`
- [wiznet](https://github.com/RT-Thread-packages/wiznet) - WIZnet TCP/IP chips (such as W5500/W5100..) SAL framework implement. `Apache-2.0`
- [zephyr_polling](https://github.com/bobwenstudy/RTT_PACKAGE_zephyr_polling) - Bluetooth BLE Stack. `Apache-2.0`
- [kawaii-mqtt](https://github.com/jiejieTop/kawaii-mqtt) - a kawaii mqtt client based on the socket API, has a very simple api interface, support QoS2、mbedtls. `GPL-2.0`
- [libcurl2rtt](https://github.com/liu2guang/libcurl2rtt) - The curl library ported on the RT-Thread platform. `Apache-2.0`
- [nanopb](https://github.com/RT-Thread-packages/nanopb) - Protocol Buffers for Embedded Systems. `Zlib`
- [tcpserver](https://github.com/Guozhanxin/tcpserver.git) - A TCP server that supports multiple clients. `Apache-2.0`
- [ppp_device](https://github.com/RT-Thread-packages/ppp_device.git) - lwIP PPP porting for Cellular Module( 2G/3G/4G ). `Apache-2.0`
- [at_device](https://github.com/RT-Thread-packages/at_device) - AT component porting or samples for different devices. `LGPL-2.1`
- [lorawan_ed_stack](https://github.com/Forest-Rain/lorawan-ed-stack) - lorawan end-device stack. `Apache-2.0`
- [cyw43xx](https://github.com/RT-Thread-packages/CYW43xx) - CYW43xx WiFi/BT SoC driver. `non-commercial use`
- [umqtt](https://github.com/RT-Thread-packages/umqtt.git) - A light weight, powerful, customizable, easy-to-use and embeddable mqtt client for RT-Thread!. `Apache-2.0`
- [agile_telnet](https://github.com/loogg/agile_telnet) - TCP debug for Ethernet. `LGPL-2.1`
- [pdulib](https://github.com/ShineRoyal/pdulib) - A TEXT parsing library for short messages in PDU format. `LGPL-2.1`
- [webclient](https://github.com/RT-Thread-packages/webclient) - http client library by RT-Thread. `Apache-2.0`
- [wayz_iotkit](https://github.com/wayz-iot/wayz_iotkit) - wayz iot location software package. `GPL-2.0`
- [btstack](https://github.com/supperthomas/RTT_PACKAGE_BTSTACK.git) - Please add description of btstack in English. `non-commercial`
- [NimBLE](https://github.com/RT-Thread-packages/nimble) - An Apache open-source Bluetooth 5.0 stack porting on RT-Thread. `Apache-2.0`
- [smtp_client](https://github.com/WKJay/SMTP_CLIENT) - smtp client package for rt-thread. `LGPL-2.1`
- [llsync_sdk_adapter](https://github.com/supperthomas/LLSync_sdk_adapter) - Please add description of llsync_sdk_adapter in English. `Apache-2.0`
- [zb_coordinator](https://github.com/TaoYang0907/ZB_COORDINATOR_PACKAGE) - Application of AT Command on ZigBee Coordinator. `LGPL-2.1`
- [coap](https://github.com/RT-Thread-packages/coap) - A C implementation of the Constrained Application Protocol. `BSD-2-Clause`
- [webnet](https://github.com/RT-Thread-packages/webnet) - A lightweight, customizable embedded Web Server by RT-Thread. `GPL-2.0`
- [airkissOpen](https://github.com/heyuanjie87/airkissOpen) - Tencent Airkiss Protocol parse library. `Apache-2.0`
- [qmodbus](https://github.com/qiyongzhong0/qmodbus) - A quick and easy to use modbus communication protocol stack. ` LGPL-2.1`

### Misc

- [kendryte-demo](https://github.com/BernardXiong/kendryte-demo) - kendryte k210 demo. `Apache-2.0`
- [optparse](https://github.com/RT-Thread-packages/optparse) - Getopt command-line parameter parser bases on RT-Thread. `Unlicense`
- [crclib](https://github.com/qiyongzhong0/crclib) - A library of functions with 8-bit ,16-bit ,32-bit crc check calculations. ` LGPL-2.1`
- [CorevMCU_CLI](https://github.com/Yaochenger/CorevMCU_CLI) - CLI components of Core-V-MCU. `LGPL-2.1`
- [fastlz](https://github.com/RT-Thread-packages/fastlz) - lightning-fast compression library. `unknown`
- [lwgps](https://github.com/orange2348/lwgps2rtt) - Lightweight GPS NMEA parser. `MIT`
- [MultiButton](https://github.com/RT-Thread-packages/MultiButton) - A compact and easy to use event-driven button driver. `MIT`
- [dstr](https://github.com/RT-Thread-packages/dstr) - dynamic string in C. `LGPL-2.1`
- [phase-locked-loop](https://github.com/haodongnj/PLL) - Phase locked loop and frequency locked loop algorithm. `MIT`
- [state_machine](https://github.com/redoccheng/state_machine) - A feature-rich, yet simple finite state machine (FSM) implementation in C. `LGPL-2.1`
- [libcsv](https://github.com/liu2guang/libcsv) - libcsv is a small, simple and fast CSV library written in pure ANSI C89 that can read and write CSV data. `LGPL-2.1`
- [uparam](https://github.com/aeo123/uparam.git) - Manage system parameters with FLASH. `MIT`
- [hello](https://github.com/RT-Thread-packages/hello) - package sample for rt-thread. `LGPL-2.1`
- [vi](https://github.com/RT-Thread-packages/vi) - The screen-oriented text editor for RT-Thread. `GPL-2.0`
- [armv7m_dwt](https://github.com/sogwms/armv7m_dwt) - armv7m_dwt High precision timing and delay. `Apache-2.0`
- [FlexibleButton](https://github.com/murphyzhao/FlexibleButton) - Small and flexible button driver. `Apache License 2.0`
- [Controller](https://github.com/haodongnj/Controller) - PI, PR and RC controller library. `MIT`
- [heatshrink](https://github.com/liukangcc/heatshrink.git) - A data compression/decompression library for embedded/real-time systems. `ISC License`
- [filesystem_samples](https://github.com/RT-Thread-packages/filesystem-sample) - RT-Thread filesystem samples. `Apache-2.0`
- [network_samples](https://github.com/RT-Thread-packages/network-sample) - RT-Thread network samples. `Apache-2.0`
- [kernel_samples](https://github.com/RT-Thread-packages/kernel-sample) - a kernel_samples package for rt-thread. `Apache-2.0`
- [peripheral_samples](https://github.com/RT-Thread-packages/peripheral-sample) - RT-Thread peripheral samples. `Apache-2.0`
- [ki](https://github.com/mysterywolf/ki) - ki is a small text editor in less than 1K lines of code. `GPL-2.0`
- [soem](https://github.com/lg28870983/soem) - SOEM (Source Open EtherCAT master) port to RT-Thread. `Apache-2.0`
- [miniLZO](https://github.com/RT-Thread-packages/miniLZO) - A mini subset of the LZO real-time data compression library. `GPL-2.0`
- [slcan2rtt](https://github.com/cazure/slcan2rtt.git) - Serial / USB serial CAN Adapter (slcan) on RT-Thread. `Apache-2.0`
- [lzma](https://github.com/RiceChen0/lzma) - A compression library with high compression ratio. `LGPL-2.1`
- [MFBD](https://github.com/smartmx/MFBD) - Multi-Function Button Detection for MCU. `Apache-2.0`
- [qparam](https://github.com/qiyongzhong0/rt-thread-qparam) - A quick and easy-to-use parameter management component, parameter saving recovery modification and quick access functions are implemented. ` LGPL-2.1`
- [design_pattern](https://github.com/chenyingchun0312/design_pattern) - design pattern implementation in C language. `Apache-2.0`
- [minizip](https://github.com/mysterywolf/minizip) - zip manipulation library. `unknown`
- [upacker](https://github.com/aeo123/upacker.git) - building and parsing data frames to be sent over a serial interface. `MIT`
- [zlib](https://github.com/RT-Thread-packages/zlib) - general purpose data compression library. `unknown`
- [TinyFrame](https://github.com/XXXXzzzz000/TinyFrame) - A simple library for building and parsing data frames for serial interfaces (like UART / RS232). `MIT`
- [CanFestival](https://github.com/gbcwbz/canfestival-rtt) - A CanFestival port to RT-Thread operating system. `LGPL-2.1`
- [get_irq_priority](https://github.com/wdfk-prog/rt-thread-get_irq_priority) - get irq priority for Cortex®-M. `LGPL-2.1`
- [ralarm](https://github.com/RiceChen0/ralarm) - An alarm clock component that does not rely on hardware and can be infinitely expanded. `Apache-2.0`
- [cal](https://github.com/mysterywolf/cal) - a terminal calendar. `MIT`
- [cmatrix](https://github.com/wuhanstudio/cmatrix) - 电影《黑客帝国》中的字符雨. `MIT`
- [snake](https://github.com/mysterywolf/snake) - a remake of the old nokia game. `GPL-2.0`
- [TinySquare](https://github.com/AlgoOy/TinySquare) - a lightweight square game engine running on Cortex-M. `Apache-2.0`
- [sl](https://github.com/wuhanstudio/sl) - steam locomotive runs across your terminal when you type 'sl' as you meant to type 'ls'. `MIT`
- [c2048](https://github.com/mysterywolf/c2048) - An indie puzzle video game run on RT-Thread console. `MIT`
- [donut](https://github.com/mysterywolf/donut) - a 3D spinning donut. `None`
- [cowsay](https://github.com/wuhanstudio/cowsay) - cowsay is a program that generates ASCII pictures of a cow with a message. `MIT`
- [threes](https://github.com/mysterywolf/threes) - An indie puzzle video game which was very popular in the year of 2014. `MIT`
- [aclock](https://github.com/mysterywolf/aclock) - a terminal clock. `Apache-2.0`
- [morse](https://github.com/zhkag/morse) - morse code. `None`
- [tetris](https://github.com/volatile-static/rtt_tetris) - Tetris port to RT-Thread console. `MIT`
- [quicklz](https://github.com/RT-Thread-packages/quicklz) - the world's fastest compression library. `GPL-3.0`

### Peripherals

- [rosserial](https://github.com/wuhanstudio/rt-rosserial) - Robots Operating System (ROS1) on rt-thread. `BSD`
- [easyblink](https://github.com/Sunwancn/rtt-pkgs-easyblink) - Blink the LED easily and use a little RAM for RT-Thread or RT-Thread Nano. `Apache-2.0`
- [multi_infrared](https://github.com/jsrdczy/rt_thread_multi_infrared_frame) - multi infrared channels based on rt thread pin and hwtimer. `Apache-2.0`
- [SignalLed](https://github.com/WKJay/SignalLed) - a signal led package for rt-thread. `LGPL-2.1`
- [rx8900](https://github.com/Prry/rtt-rx8900) - Extern RTC driver for rx8900. `Apache-2.0`
- [ds3231](https://github.com/Prry/rtt-ds3231) - Extern RTC driver for ds3231. `Apache-2.0`
- [qkey](https://github.com/qiyongzhong0/rt-thread-qkey) - A quick and easy-to-use key driver package. ` LGPL-2.1`
- [rs485](https://github.com/qiyongzhong0/rt-thread-rs485) - rs485 driver package. ` LGPL-2.1`
- [rda58xx](https://github.com/apeng2012/rda58xx) - RDA5820 single-chip broadcase FM transceiver driver. `MIT`
- [bluetrum_sdk](https://github.com/BLUETRUM/bluetrum_sdk) - bluetrum sdk. `MIT`
- [nrfx](https://github.com/xckhmf/nrfx) - Standalone set of drivers for peripherals present in Nordic Semiconductor's SoCs. `Unknown`
- [embARC_bsp](https://github.com/foss-for-synopsys-dwc-arc-processors/embarc_bsp) - embARC_bsp(Synopsys ARC Processer Board Support Package Software ) package. `Apache-2.0`
- [nuclei_sdk](https://github.com/Nuclei-Software/nuclei-sdk) - Nuclei RISC-V Software Development Kit. `Apache-2.0`
- [raspberrypi-pico-sdk](https://github.com/RT-Thread-packages/raspberrypi-pico-sdk) - Raspberry Pi Pico SDK. `BSD-3-Clause`
- [nrf5x_sdk](https://github.com/supperthomas/nrf5x_sdk) - Software development kit for the nRF52 Series and nRF51 Series SoCs. `unknown`
- [K210-SDK](https://github.com/RT-Thread-packages/kendryte-k210-sdk) - Kendryte K210 SDK. `Apache-2.0`
- [kendryte-sdk](https://github.com/RT-Thread-packages/kendryte_sdk) - Kendryte K210 SDK. `unknown`
- [ESP-IDF](https://github.com/RT-Thread-packages/esp-idf) - Espressif IoT Development Framework. `Apache-2.0`
- [stm32l4_cmsis_driver](https://github.com/RT-Thread-packages/stm32l4_cmsis_driver) - STM32 L4 CMSIS driver package. `Apache-2.0`
- [stm32_sdio](https://github.com/RT-Thread-packages/stm32_sdio) - STM32 SDIO controller drivers library. `LGPL-2.1`
- [stm32l4_hal_driver](https://github.com/RT-Thread-packages/stm32l4_hal_driver) - STM32 L4 HAL driver package. `BSD-3-Clause`
- [stm32wb55_sdk](https://github.com/xupenghu/stm32wb55_sdk.git) - stm32wb55_sdk software package. `Apache-2.0`
- [lrf-nv7lidar](https://github.com/RT-Thread-packages/nv7lidar) - LRF-NV7 laser ranging module. `LGPL-2.1`
- [LedBlink](https://github.com/aeo123/LedBlink.git) - easy led blink support;. `GPL-2.0`
- [io_input_filter](https://github.com/lizdDong/io_input_filter) - IO Input Filter. `Apache-2.0`
- [mcp23008](https://github.com/XiaojieFan/mcp23008.git) - Remote 8-bit I/O expander for I2C-bus. `Apache-2.0`
- [quick_led](https://github.com/qiyongzhong0/rt-thread-qled) - A quick and easy-to-use led driver package. ` LGPL-2.1`
- [i2c-tools](https://github.com/wuhanstudio/rt-i2c-tools) - A collection of i2c tools including scan/read/write. `MIT`
- [mfoc](https://github.com/wuhanstudio/mfoc) - Mifare Classic Offline Cracker. `GPL-2.0`
- [agile_button](https://github.com/loogg/agile_button) - A agile button package. `LGPL-2.1`
- [dm9051](https://github.com/aozima/dm9051) - DM9051 SPI ethernet driver. `Apache-2.0`
- [max7219](https://github.com/redocCheng/max7219) - a MAX7219 package for the digital tube. `Apache-2.0`
- [nrf24l01](https://github.com/sogwms/nrf24l01) - Single-chip 2.4GHz wireless transceiver. `Apache-2.0`
- [lkdGui](https://github.com/guoweilkd/lkdGui) - lkdGui is a graphical interface for monochrome displays. `GPL-2.0`
- [spi-tools](https://github.com/vandoul/rt-spi-tools) - A collection of spi tools including init/config/trans. `MIT`
- [aip650](https://github.com/Maihuanyi/aip650) - A quick and easy-to-use digit led and key driver package for aip650 and tm1650. ` LGPL-2.1`
- [x9555](https://github.com/WennianYan/x9555) - 16-bit 1.65- to 5.5-V I2C/SMBus I/O expander with interrupt, weak pull-up & config registers. `Apache-2.0`
- [ssd1306](https://github.com/luhuadong/rtt-ssd1306) - Drive OLEDs based on SSD1306, SH1106, SH1107 and SSD1309, supports I2C and SPI. `Apache-2.0`
- [agile_console](https://github.com/loogg/agile_console) - Simple debugging device Middleware. `LGPL-2.1`
- [Misaka_AT24CXX](https://github.com/xqyjlj/Miaska_AT24CXX) - Misaka-Network for AT24CXX EEPROM. `Apache-2.0`
- [rfm300](https://github.com/kylepengchn/rfm300.git) - ISM Transceiver Module With +20dBm(100mW) Output Power. `Apache-2.0`
- [tca9534](https://github.com/Prry/rtt-tca9534) - a 8-bit I/O expander for i2c-bus. `Apache-2.0`
- [lora_radio_driver](https://github.com/Forest-Rain/lora-radio-driver) - lora chipset(SX126x\SX127x) driver. `Apache-2.0`
- [pms_series](https://github.com/MrpYoung/pms_series) - Digital universal particle concentration sensor driver library. `MIT`
- [as608](https://github.com/greedyhao/as608.git) - AS608 fingerprint module driver. `Apache-2.0`
- [tmp1075](https://github.com/Prry/rtt-tmp1075) - Digital temperature sensor driver package for TMP1075. `Apache-2.0`
- [mpu6xxx](https://github.com/RT-Thread-packages/mpu-6xxx) - a package of mpu6xxx driver library, compatible with mpu6000, mpu6050, mpu6500, mpu9250 and other chips. `Apache-2.0`
- [dht11](https://github.com/murphyzhao/dht11_rtt) - Digital temperature and humidity sensor(Single bus). `Apache-2.0`
- [bmp280](https://github.com/nfsq246/RTT_BMP280) - bmp280 iic drive. `other`
- [sths34pf80](https://github.com/zyk6271/STHS34PF80) - This is the STHS34PF80 sensor driver package. `Apache-2.0`
- [ap3216c](https://github.com/RT-Thread-packages/ap3216c) - a digital ambient light and a proximity sensor ap3216c driver library. `Apache-2.0`
- [bmp180](https://github.com/Prry/rtt-bmp180) - barometric, temperature. `Apache-2.0`
- [ds18b20](https://github.com/willianchanlovegithub/ds18b20) - a package of digital temperature sensor ds18b20. `Apache-2.0`
- [hs300x](https://github.com/Guozhanxin/hs300x) - digital humidity and temperature sensor hs300x driver library. `Apache-2.0`
- [bme680](https://github.com/luhuadong/rtt-bme680) - Digital 4-in-1 sensor with gas, humidity, pressure and temperature. `Apache-2.0`
- [qmp6989](https://github.com/kylepengchn/qmp6989.git) - High accuracy and small size barometric pressure sensor,support: barometer, temperature. `Apache-2.0`
- [PAJ7620](https://github.com/orange2348/paj7620) - Gesture sensor PAJ7620 driver package. `Apache-2.0`
- [hmc5883](https://github.com/gmyFighting/hmc5883) - bmi088 software package. `Apache-2.0`
- [mlx90397](https://github.com/lgnq/mlx90397) - The MLX90397 is the newest addition to the Melexis position sensing portfolio, bringing the highest flexibility in the portfolio’s smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%. `Apache-2.0`
- [bme280](https://github.com/RT-Thread-packages/bme280) - barometric, humidity. `other`
- [hts221](https://github.com/RT-Thread-packages/hts221) - temperature, humidity. `other`
- [ina226](https://github.com/xupenghu/ina226.git) - ina226 software package. `Apache-2.0`
- [gp2y10](https://github.com/luhuadong/rtt-gp2y10) - dust sensor by Sharp for detect air quality. `Apache-2.0`
- [gy271](https://github.com/jch12138/gy271) - a package of gy271 driver library. `Apache-2.0`
- [mlx90393](https://github.com/lgnq/mlx90393) - The MLX90393 is the newest addition to the Melexis position sensing portfolio, bringing the highest fl exibility in the portfolio’s smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%. `Apache-2.0`
- [hdc1000](https://github.com/Forest-Rain/hdc1000) - hdc1000 sensor driver base on RT-Thread sensor frame. `Apache-2.0`
- [bmi160_bmx160](https://github.com/RT-Thread-packages/bmi160_bmx160) - The device driver package for BMX160 and BMI160. `other`
- [max30102](https://github.com/Jackistang/max30102_rtt) - heart rate and oxygen saturation measure. `Apache-2.0`
- [max31865](https://github.com/SimpleInit/max31865) - a package of digital temperature sensor. `Apache-2.0`
- [sht3x](https://github.com/donghao2nanjing/sht3x) - digital humidity and temperature sensor sht3x driver library. `LGPLv2.1`
- [aht10](https://github.com/RT-Thread-packages/aht10) - digital humidity and temperature sensor aht10 driver library. `Apache-2.0`
- [bh1750](https://github.com/sanjaywu/bh1750_sensor) - temperature, humidity. `Apache-2.0`
- [dhtxx](https://github.com/luhuadong/rtt-dhtxx) - DHTxx one-wire digital temperature and humidity sensor. `Apache-2.0`
- [cw2015](https://github.com/qingehao/CW2015) - fuel gauging system IC for Lithium-ion(Li+) Battery. `Apache-2.0`
- [sht4x](https://github.com/flyingcys/sht4x) - digital humidity and temperature sensor sht4x driver library. `Apache-2.0`
- [ad7746](https://github.com/wuhanstudio/rt-ad7746) - AD7746  a high resolution, capacitance-to-digital converter (CDC). `MIT`
- [adt74xx](https://github.com/IoTSharp/ADT74XX) - digital  temperature sensor adt74xx driver library. `LGPLv2.1`
- [ina260](https://github.com/xupenghu/ina260.git) - ina260 software package. `Apache-2.0`
- [ccs811](https://github.com/luhuadong/rtt-ccs811) - Digital Gas Sensor for Monitoring Indoor Air Quality. `Apache-2.0`
- [isl29035](https://github.com/ShermanShao/isl29035) - Driver library for Renesas Ambient light sensor ISL29035. `RENESAS SOFTWARE LICENSE TERMS`
- [vl53l0x](https://github.com/Prry/rtt-vl53l0x) - Time of flight sensor driver package for vl53l0x. `Apache-2.0`
- [pmsxx](https://github.com/luhuadong/rtt-pmsxx) - Plantower pms serial PM2.5 sensor driver. `Apache-2.0`
- [da270](https://github.com/MiraMEMS-Wonderful/da270-RT-Thread) - This is the driver package of MiraMEMS DA270 accelerometer for RT-Thread. `GPL-3.0`
- [spl0601](https://github.com/RT-Thread-packages/spl0601) - The Digital Air Pressure Sensor SPL06-01 driver package. `other`
- [max6675](https://github.com/JonasWen/max6675) - a package of digital temperature sensor max6675. `Apache-2.0`
- [balance](https://github.com/xiaogeminghai/balance) - Use hx71xx and weighing pressure sensor to measure weight. `GPL-2.0`
- [lis2dh12](https://github.com/StackRyan/lis2dh12.git) - accelerometer, tempature. `other`
- [lsm6dsm](https://github.com/my-RT-packages/lsm6dsm.git) - STMicroelectronics's LSM6DSM driver,support Accelerometer/gyro/step count/temperature. `MIT`
- [sht2x](https://github.com/RT-Thread-packages/sht2x) - digital humidity and temperature sensor sht2x driver library. `Apache-2.0`
- [lsm303agr](https://github.com/RT-Thread-packages/lsm303agr) - accelerometer, magnetometer. `other`
- [df220](https://github.com/MiraMEMS-Wonderful/df220-RT-Thread.git) - This is the driver package of MiraMEMS df220 force sensor for RT-Thread. `GPL-3.0`
- [lsm6dsl](https://github.com/RT-Thread-packages/lsm6dsl) - accelerometer, gyroscope, step. `other`
- [ms5611](https://github.com/sogwms/ms5611) - The Digital Air Pressure Sensor MS5611 driver package. `Apache-2.0`
- [icm20608](https://github.com/RT-Thread-packages/icm20608) - a 3-axis gyroscope and a 3-axis accelerometer driver library. `Apache-2.0`
- [as7341](https://github.com/RiceChen0/as7341) - AS7341 visible light sensor, can measure 8 wavelengths of visible light. `Apache-2.0`
- [rt3020](https://github.com/RichtekTechnology/RT3020) - This is the driver package of RT3020 accelerometer. `Apache-2.0`
- [ms5805](https://github.com/schuck-wang/RTThread-MS5805) - The Digital Air Pressure Sensor MS5805 driver package. `Apache-2.0`
- [mmc3680kj](https://github.com/mumuge1/mmc3680kj) - mmc3680kj drive. `other`
- [mlx90632](https://github.com/xupenghu/mlx90632.git) - mlx90632 software package. `Apache-2.0`
- [zmod4410](https://github.com/ShermanShao/zmod4410) - The ZMOD4410 Gas Sensor Module is designed for detecting total volatile organic compounds (TVOC) and monitoring indoor air quality (IAQ). `RENESAS SOFTWARE LICENSE TERMS`
- [max17048](https://github.com/aeo123/MAX17048.git) - Bat monitor. `MIT`
- [bmi088](https://github.com/gmyFighting/bmi088) - bmi088 software. `Apache-2.0`
- [shtc1](https://github.com/nfsq246/RTT_SHTC1) - temperature, humidity. `other`
- [sr04](https://github.com/alec-shan/hc-sr04) - driver package for hc-sr04 using rt-thread sensor package. `Apache-2.0`
- [hshcal001](https://github.com/lucaslsh/hshcal001.git) - temperature, humidity. `Apache-2.0`
- [bma400](https://github.com/RT-Thread-packages/bma400) - accelerometer, step. `other`
- [tsl4531](https://github.com/JellyYe/tsl4531pkgs.git) - TSL4531 sensor driver package ,support lux. `Apache-2.0`
- [mlx90392](https://github.com/lgnq/mlx90392) - The MLX90392 is the newest addition to the Melexis position sensing portfolio, bringing the highest fl exibility in the portfolio’s smallest assembly. Complementing this, the magnetic fi eld sensor is designed for micropower applications, with programmable duty cycles in the range of 0.1% to 100%. `Apache-2.0`
- [sgp30](https://github.com/luhuadong/rtt-sgp30) - air sensor by Sensirion for detect TVOC and CO2. `Apache-2.0`
- [lps22hb](https://github.com/RT-Thread-packages/lps22hb) - This is the LPS22HB sensor driver package. `other`
- [vsensor](https://github.com/RT-Thread-packages/vsensor) - virtual sensor device. `Apache-2.0`
- [ws2812b](https://github.com/maplerian/rt_ws2812b) - Ws2812b software driver package for RT-Thread is driven by SPI+DMA. `Apache-2.0`
- [beep](https://github.com/Sunwancn/rtt-pkgs-beep) - Control the buzzer to make beeps at different intervals. `Apache-2.0`
- [libnfc](https://github.com/wuhanstudio/libnfc) - Platform independent Near Field Communication (NFC) library. `LGPL-3.0`
- [realtek_ameba](https://github.com/flyingcys/realtek_ameba) - realtek_ameba package on RT-Thread. `LGPL-2.1`
- [kobuki](https://github.com/wuhanstudio/kobuki) - Kobuki Robot serial communication driver. `MIT`
- [infrared](https://github.com/RT-Thread-packages/infrared_framework) - Infrared framework based on rt-thread's pin,pwm and hwtimer driver. `Apache-2.0`
- [pca9685](https://github.com/greedyhao/pca9685) - I2C-bus controlled 16-channel PWM controller. `Apache-2.0`
- [ly68l6400](https://github.com/Ghazigq/ly68l6400) - device drive for ly68l6400. `LGPL-2.1`
- [System_Run_LED](https://github.com/WennianYan/System_Run_LED) - Super simple and practical system running indicator light control thread. `Apache-2.0`
- [nes](https://github.com/Ghazigq/nes) - nes simulator c Library. `Apache-2.0`
- [micro_ros](https://github.com/wuhanstudio/micro_ros) - ROS 2 on microcontrollers. `Apache-2.0`
- [ili9341](https://github.com/Rbb666/ILI9341.git) - TFT-LCD ILI9341 SPI screen driver software package. `Apache-2.0`
- [lora_gw_driver_lib](https://github.com/Forest-Rain/lora-gw-driver-lib) - lora-gw-driver-lib is lora gateway chip(SX130x) driver binary libraries. `Apache-2.0`
- [wm_libraries](https://github.com/WinnerMicro/rtpkg-wm_libraries) - a library package for WinnerMicro devices. `Apache-2.0`
- [lora_modem_driver](https://github.com/Forest-Rain/lora-modem-driver) - lora_modem_driver is a serial driver of lora//lorawan modem. `Apache-2.0`
- [xpt2046](https://github.com/LeeChunHei/xpt2046_touch_rtt) - xpt2046 touch driver package. `MIT`
- [ft6236](https://github.com/RT-Thread-packages/ft6236) - This is the driver package of FT6236 touch chip. `Apache-2.0`
- [gt911](https://github.com/RiceChen0/gt911) - gt911 drivers for RT-Thread. `Apache-2.0`
- [gt917s](https://github.com/lilisheng411527/gt917s.git) - gt917s drivers for RT-Thread. `LGPL-2.1`
- [ft5426](https://github.com/liuduanfei/ft5426) - This is the driver package of FT5426 touch chip. `Apache-2.0`
- [gt9147](https://github.com/RT-Thread-packages/gt9147) - This is the GT9147 touch driver package. `Apache-2.0`
- [cst816x](https://github.com/Z8MAN8/cst816x) - cst816x drivers for RT-Thread. `Apache-2.0`
- [gt1151](https://github.com/Jackistang/GT1151) - gt1151 drivers for RT-Thread. `Apache-2.0`
- [cst812t](https://github.com/StackYuan/cst812t) - cst812t drivers for RT-Thread. `Apache-2.0`
- [ft6206](https://github.com/RT-Thread-packages/ft6206) - This is the driver package of FT6206 touch chip. `Apache-2.0`
- [bt_mx01](https://github.com/qiyongzhong0/rt-thread-bt_mx01) - Device driver of BT chip MX-01. ` LGPL-2.1`
- [vs1003](https://github.com/beisongcrt/vs1003.git) - vs1003 driver. `GPL-2.0`
- [tmc51xx](https://github.com/apeng2012/tmc51xx) - TMC5160 power driver for stepper motors. `MIT`
- [fingerprint](https://github.com/pk-ing/fingerprint) - fingerprint module driver. `GPL-3.0`
- [uat](https://github.com/qiyongzhong0/rt-thread-uat) - Micro AT device driver interface component. ` LGPL-2.1`
- [can_ymodem](https://github.com/redocCheng/rt_can_ymodem) - a device connect can & ymodem. `Apache-2.0`
- [soft_serial](https://github.com/qiyongzhong0/rt-thread-soft-serial) - A software serial driver package by using the hardware timer capture / comparison functionality. ` LGPL-2.1`
- [mb85rs16](https://github.com/XiaojieFan/mb85rs16.git) - Memory FRAM 16K(2Kx8)Bit SPI Driver Library. `Apache-2.0`
- [pcf8574](https://github.com/RT-Thread-packages/pcf8574) - Remote 8-bit I/O expander for I2C-bus. `Apache-2.0`
- [ld3320](https://github.com/xqyjlj/ld3320) - LD3320 speech recognition chip. `Apache-2.0`
- [RgPower](https://github.com/1300650671/RgPower) - power value get module driver. `Apache-2.1`
- [button](https://github.com/jiejieTop/rtpkg_button) - button drive by C, support single and double click, long press, long press release. `GPL-3.0`
- [bt_ecb02c](https://github.com/qiyongzhong0/rt-thread-bt_ecb02c) - Device driver of BT chip ECB02C. ` LGPL-2.1`
- [at24cxx](https://github.com/XiaojieFan/at24cxx) - eeprom at24cxx driver library. `Apache-2.0`
- [st7789](https://github.com/Vandoul/ST7789.git) - TFT-LCD ST7789 SPI Graphic driver. `Apache-2.0`
- [sgm706](https://github.com/Prry/rtt-sgm706) - Independent watchdog driver package for sgm706. `Apache-2.0`
- [rc522](https://github.com/greedyhao/rc522_rtt) - rc522 rfid module driver. `Apache-2.0`
- [littled](https://github.com/luhuadong/rtt-littled) - Littled LED Daemon for LED driver. `Apache-2.0`
- [MotionDriver2RTT](https://github.com/greedyhao/MotionDriver2RTT) - A package porting MotionDriver to RTT. `LGPL-2.1`
- [multi_rtimer](https://github.com/Forest-Rain/multi-rtimer) - a real-time and low power software timer module. `Apache-2.0`
- [rs232](https://github.com/diskwu/RTTHREAD_RS232) - rs232 driver package. `LGPL-2.1`
- [sx12xx](https://github.com/XiaojieFan/sx12xx) - Semtech  LoRa RF chip driver library. `Apache-2.0`
- [rplidar](https://github.com/wuhanstudio/rplidar) - a low cost LIDAR sensor suitable for indoor robotic SLAM application. `MIT`
- [vdevice](https://github.com/RT-Thread-packages/vdevice) - A virtual IO peripheral environment. `Apache-2.0`
- [agile_led](https://github.com/loogg/agile_led) - A agile led package. `LGPL-2.1`
- [wk2124](https://github.com/MrMichael/wk2124) - wk2124(spi to uart) driver library. `Apache-2.0`
- [Misaka_RGB_Bling](https://github.com/xqyjlj/Misaka_RGB_Bling) - Misaka-Network for RGB LED Bling. `Apache-2.0`

### Multimedia

- [NUemWin](https://github.com/wosayttn/NUemWin) - a NUemWin package for rt-thread. `LGPL-2.1`
- [LVGL](https://github.com/lvgl/lvgl) - Light and Versatile Graphics Library (official upstream). `MIT`
- [lv_music_demo](https://github.com/RT-Thread-packages/lv_demo_music) - LVGL music player demo for RT-Thread. `MIT`
- [LittlevGL2RTT](https://github.com/liu2guang/LittlevGL2RTT) - LittlevGL graphics library (LVGL 7.x, legacy). `MIT`
- [gui_guider_demo](https://github.com/NXPmicro/gui-guider-demos.git) - LVGL demo generated by GUI Guider. `MIT`
- [TJpgDec](https://github.com/RT-Thread-packages/TJpgDec) - Tiny JPEG Decompressor. `BSD`
- [mcurses](https://github.com/wuhanstudio/mcurses) - micro ncurses library. `MIT`
- [persimmon](https://github.com/RT-Thread-packages/persimmon) - Persimmon UI for RT-Thread. `unknown`
- [mp3player](https://github.com/MrzhangF1ghter/mp3player) - a simple mp3 format music player. `Apache-2.0`
- [3gpp_amrnb](https://github.com/myshowtogo/3gpp_amrnb) - 3gpp amrnb codec library. `Apache`
- [touchgfx2rtt](https://github.com/Aladdin-Wang/touchgfx2rtt.git) - a touchgfx package for rt-thread. `LGPL-2.1`
- [vt100](https://github.com/wuhanstudio/vt100) - iridescent drawing library on MSH. `MIT`
- [u8g2](https://github.com/wuhanstudio/rt-u8g2) - u8g2 library for rt-thread (legacy). `BSD`
- [u8g2-official](https://github.com/olikraus/u8g2) - u8g2 library (official upstream). `BSD`
- [gui_engine](https://github.com/RT-Thread-packages/gui_engine) - GUI Engine by RT-Thread. ` LGPL-2.1`
- [STemWin](https://github.com/loogg/STemWin) - a STemWin package for rt-thread. `LGPL-2.1`
- [mupdf](https://github.com/rtoslab/mupdf-rtt) - a lightweight PDF, XPS, and E-book viewer. `AGPL-3.0`
- [openmv](https://github.com/RT-Thread-packages-by-SummerGift/openmv) - openmv porting for rt-thread. `MIT`
- [termbox](https://github.com/mysterywolf/termbox) - library for writing text-based user interfaces. `MIT`
- [wavplayer](https://github.com/RT-Thread-packages/wavplayer) - Minimal music player for wav file play and record. `Apache-2.0`
- [PDFGen](https://github.com/mysterywolf/PDFGen) - Simple C PDF Writer/Generation library. `Unlicense`
- [TinyJPEG](https://github.com/StackRyan/TinyJPEG) - a light-weight JPEG encoder package. `Apache-2.0`
- [helix](https://github.com/liuduanfei/helix) - The Helix MP3 Decoder. `AGPL-3.0`
- [qrcode](https://github.com/RT-Thread-packages/qrcode) - A simple library for generating QR codes in C. `MIT`
- [ugui](https://github.com/xidongxu/ugui.git) - Open source graphics library ugui ported to rtthread. `unknown`
- [AzureGUIX](https://github.com/HelloByeAll/AzureGUIX) - Microsoft THREADX system middleware AzureGUIX. `Apache-2.0`

### AI

- [nnom](https://github.com/majianjia/nnom) - A higher-level Neural Network framework on Microcontroller (NNoM). `Apache-2.0`
- [quest](https://github.com/wuhanstudio/QuEST) - A simulator of quantum computers on MCU. `MIT`
- [onnx-backend](https://github.com/wuhanstudio/onnx-backend) - Open Neural Network Exchange backend on RT-Thread. `MIT`
- [elapack](https://github.com/wuhanstudio/elapack) - Linear algebra library for embedded devices, compatible with matlab. `MIT`
- [onnx-parser](https://github.com/wuhanstudio/rt-onnx-parser) - Open Neural Network Exchange model parser in C. `MIT`
- [TensorflowLiteMicro](https://github.com/QingChuanWS/TensorflowLiteMicro) - a lightweight deep learning inference framework based on Google Tensorflow Lite for RT-Thread operating system. `LGPLv2.1`
- [libann](https://github.com/wuhanstudio/rt-libann) - A light-weight ANN library, capable of training, saving and loading models. `MIT`
- [ulapack](https://github.com/wuhanstudio/ulapack) - Linear algebra library for embedded devices. `MIT`
- [ncnn](https://github.com/yc66542260/ncnn-rtthread) - NCNN package for RT-Thread. `BSD-3-Clause`
- [r-tinymaix](https://github.com/RiceChen0/r-tinymaix) - r-tinymaix TinyMaix is a tiny inference Neural Network library specifically for microcontrollers (TinyML). `Apache-2.0`
- [naxos](https://github.com/wuhanstudio/naxos) - A C++ Constraint Programming Library. `LGPL-3.0`

### Security

- [mbedtls](https://github.com/RT-Thread-packages/mbedtls) - An open source, portable, easy to use, readable and flexible SSL library. `Apache-2.0`
- [libsodium](https://github.com/RT-Thread-packages/libsodium-legacy) - A modern and easy-to-use crypto library (NOT Recommended for MCU. Use libhydrogen instead). `ISC`
- [tinycrypt](https://github.com/RT-Thread-packages/tinycrypt) - A simple and configurable crypt library. ` BSD-2-Clause`
- [yd_crypto](https://github.com/china-hai/yd_crypto) - Encryption and decryption algorithm library for microcontroller. `Apache-2.0`
- [libhydrogen](https://github.com/wuhanstudio/libhydrogen) - A lightweight, secure, easy-to-use crypto library suitable for constrained environments. `ISC`
- [trusted-firmware-m](https://github.com/RT-Thread-packages/trusted-firmware-m) - Trusted firmware for M class. ` BSD-3-Clause`

### System

- [lwext4](https://github.com/RT-Thread-packages/lwext4) - an excellent choice of ext2/3/4 filesystem for microcontrollers. `GPL-2.0`
- [mcuboot](https://github.com/iysheng/rt_mcuboot.git) - A common infrastructure for the bootloader, system flash layout on microcontroller systems. `Apache-2.0`
- [qboot](https://github.com/qiyongzhong0/rt-thread-qboot) - A component used to make bootloader quickly. ` LGPL-2.1`
- [cairo](https://github.com/RT-Thread-packages/cairo) - Multi-platform 2D graphics library. `LGPL/MPL`
- [TinyUSB](https://github.com/RT-Thread-packages/tinyusb) - An open source cross-platform USB stack for embedded system. `MIT`
- [reb](https://github.com/RiceChen0/reb) - Event broker component based on publish subscribe. `Apache-2.0`
- [uffs](https://github.com/RT-Thread-packages/uffs) - Ultra-low-cost Flash File System. `LGPL-2`
- [TFDB](https://github.com/smartmx/TFDB) - Tiny Flash Database for MCU. `MIT`
- [sfdb](https://github.com/WKJay/sfdb) - Simple file database. `Apache-2.0`
- [yaffs2](https://github.com/heyuanjie87/yaffs2_rtt_port) - yaffs2 port to rtthread. `GPL-2.0`
- [rti](https://github.com/RT-Thread-packages/rti) - RT-Thread insight, a probe tool for RT-Thread to help to analyze internal behavior of the system. `LGPL-2.1`
- [r-rhealstone](https://github.com/RiceChen0/r-rhealstone) - A cross platform real-time system benchmark testing framework. `Apache-2.0`
- [perf_counter](https://github.com/RT-Thread-packages/perf_counter) - A dedicated performance counter for Cortex-M systick. `Apache-2.0`
- [syswatch](https://github.com/qiyongzhong0/rt-thread-syswatch) - A component used to ensure the long-term normal running of the system. ` LGPL-2.1`
- [openamp](https://github.com/bigmagic123/openamp.git) - OpenAMP for rt-thread. `LGPL-2.1`
- [tz-database](https://github.com/RT-Thread-packages/tz) - time zone database and code. `BSD-3-Clause`
- [sqlite](https://github.com/RT-Thread-packages/SQLite) - SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. `unknown`
- [levelx](https://github.com/RT-Thread-packages/levelx.git) - Threadx's wear-leveling component. `MIT`
- [event_recorder](https://github.com/RT-Thread-packages/event_recorder) - A lightweight event record and replay tools for debug and test. `Apache-2.0`
- [FreeRTOS_Wrapper](https://github.com/RT-Thread-packages/FreeRTOS-Wrapper) - FreeRTOS Application Compatibility Layer for RT-Thread. `Apache-2.0`
- [FlashDB](https://github.com/armink/FlashDB) - A lightweight database that supports key-value and time series data. `Apache-2.0`
- [Qfplib_M3](https://github.com/mysterywolf/Qfplib-M3) - a free, fast and accurate ARM Cortex-M3 floating-point library. `GPL`
- [Qfplib_M0_full](https://github.com/mysterywolf/Qfplib-M0-full) - a free, fast and compact ARM Cortex-M0 floating-point library. `GPL`
- [Qfplib_M0_tiny](https://github.com/mysterywolf/Qfplib-M0-tiny) - a free ARM Cortex-M0 floating-point library in 1 kbyte. `GPL`
- [flash_blob](https://github.com/Aladdin-Wang/flash_blob.git) - Tool for quickly generating flash driver files. `Apache-2.0`
- [fal](https://github.com/RT-Thread-packages/fal) - Flash Abstraction Layer implentment. Manage flash device and partition. ` LGPL-2.1`
- [Arm-2D](https://github.com/liuduanfei/Arm-2D) - Arm-2D Graphics Library. `Apache-2.0`
- [jffs2](https://github.com/RT-Thread-packages/jffs2) - Journalling Flash File System Version2. `GPL-2.0`
- [plccore](https://github.com/hyafz/plccore) - plccore for RT-Thread. `LGPL-2.1`
- [agile_upgrade](https://github.com/loogg/agile_upgrade) - Middleware for fast building bootloader. `Apache-2.0`
- [qpc](https://github.com/Zhyolo/qpc-rtthread) - Lightweight Real-Time Embedded Framework QP/C. `GPL-3.0`
- [CMSIS-NN](https://github.com/RT-Thread-packages/CMSIS-NN) - Efficient Neural Network Kernels for Arm Cortex-M CPUs. `Apache-2.0`
- [CMSIS_RTOS2](https://github.com/RT-Thread-packages/CMSIS_RTOS2) - CMSIS-RTOS2 wrapper for RT-Thread. `Apache-2.0`
- [CMSIS_5](https://github.com/ARM-software/CMSIS_5) - CMSIS-5 Development. `Apache-2.0`
- [CMSIS_RTOS1](https://github.com/RT-Thread-packages/CMSIS_RTOS1) - CMSIS-RTOS1 wrapper for RT-Thread. `Apache-2.0`
- [CMSIS-DSP](https://github.com/RT-Thread-packages/CMSIS-DSP) - A comprehensive DSP library for Cortex-M processor-based devices. `Apache-2.0`
- [CMSIS_5_AUX](https://github.com/RT-Thread-packages/CMSIS_5_AUX) - CMSIS-5 Auxiliary Package. `Apache-2.0`
- [CMSIS-Core](https://github.com/RT-Thread-packages/CMSIS-Core) - Standardized API for the Cortex-A/M processor core and peripherals. `Apache-2.0`
- [TaskMsgBus](https://github.com/slyant/TaskMsgBus.git) - For sending and receiving text/object messages between threads based on RT-Thread. `Apache-2.0`
- [thread_pool](https://github.com/armink-rtt-pkgs/thread_pool) - a thread pool base on RT-Thread. `MIT`
- [kmulti_rtimer](https://github.com/kylepengchn/kmulti_rtimer.git) - a multi timer for rt-thread. `Apache-2.0`
- [Ppool](https://github.com/mysterywolf/Ppool) - Pthread-based thread pool library. `LGPL-2.1`
- [CherryUSB](https://github.com/cherry-embedded/CherryUSB) - Tiny and portable USB host/device stack for embedded system with USB IP. `Apache-2.0`
- [littlefs](https://github.com/RT-Thread-packages/littlefs) - A little fail-safe filesystem designed for microcontrollers. `BSD-3-Clause`
- [sys_load_monitor](https://github.com/armink-rtt-pkgs/sys_load_monitor) - system load monitor. `Apache-2.0`
- [rt-robot](https://github.com/RT-Thread-packages/rt-robot) - RT-Thread Robots platform. `MIT`
- [LiteOS-SDK](https://github.com/RT-Thread-packages/LiteOS-SDK) - LiteOS SDK. `Apache-2.0`
- [rt_vsnprintf_full](https://github.com/mysterywolf/rt_vsnprintf_full) - fully functional version of rt_vsnprintf. `Apache-2.0`
- [rt_memcpy_cm](https://github.com/mysterywolf/rt_memcpy_cm) - Cortex-M kernel assembly accelerated version of rt_memcpy function. `Apache-2.0`
- [rt_kprintf_threadsafe](https://github.com/mysterywolf/rt_kprintf_threadsafe) - thread-safe version of rt_kprintf. `Apache-2.0`
- [rpmsg-lite](https://github.com/flyingcys/rpmsg-lite) - rpmsg-lite for rt-thread. `Apache-2.0`
- [partition](https://github.com/RT-Thread-packages/partition) - A partition management package bases on block device. `LGPL-2.1`
- [EV](https://github.com/sogwms/EV) - Framework for efficient development of vehicles (including drones). `Apache-2.0`
- [mlibc](https://github.com/plctlab/mlibc) - Embedded libc, especially for RISC-V. `MIT`
- [minIni](https://github.com/hichard/minIni) - minIni for RT-Thread. `Apache-2.0`
- [pixman](https://github.com/RT-Thread-packages/pixman) - A library that provides low-level pixel manipulation. `MIT`
- [ramdisk](https://github.com/majianjia/ramdisk) - A RAM memory block device. `Apache-2.0`
- [tlsf](https://github.com/RT-Thread-packages/tlsf) - TLSF is a dynamic memory allocation algorithm with predictable execution time and low fragmentation. `Apache-2.0`
- [filex](https://github.com/RT-Thread-packages/filex) - fiex in rttthread. `Unknown`
- [rtp](https://github.com/RiceChen0/rtp) - rtp Cross platform thread pool. `Apache-2.0`
- [uC_Modbus](https://github.com/mysterywolf/uC-Modbus-for-RT-Thread) - uC/Modbus for RT-Thread. `Apache-2.0`
- [uCOSIII_Wrapper](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-III) - μC/OS-III RTOS Application Compatibility Layer for RT-Thread. `Apache-2.0`
- [uC_Common](https://github.com/mysterywolf/uC-Common-for-RT-Thread) - uC/Common for RT-Thread. `Apache-2.0`
- [uCOSII_Wrapper](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-II) - μC/OS-II RTOS Application Compatibility Layer for RT-Thread. `Apache-2.0`
- [uC_CLK](https://github.com/mysterywolf/uC-Clk-for-RT-Thread) - uC/Clk for RT-Thread. `Apache-2.0`
- [uC_CRC](https://github.com/mysterywolf/uC-CRC-for-RT-Thread) - uC/CRC for RT-Thread. `Apache-2.0`
- [lpm](https://github.com/RT-Thread-packages/lpm) - Logical partition management. Manage storage device and partition. `Apache-2.0`

### Language

- [jerryscript](https://github.com/RT-Thread-packages/jerryscript) - JerryScript port for RT-Thread. `Apache-2.0`
- [simple_xml](https://github.com/xfwangqiang/simple_xml) - Based on the XML parser of the C language, the purpose of this project is to develop a code that can be applied on multiple platforms. At present, the code has been applied to MAINSTREAM OPERATING SYSTEMS SUCH AS WIN10, LINUX, RT-thread, VxWorks and so on. `MIT`
- [ezXML](https://github.com/RT-Thread-packages/ezXML) - An XML parser C library that's simple and easy to use. `MIT`
- [LuatOS](https://github.com/openLuat/luatos-soc-rtt) - Powerful embedded Lua Engine for IoT devices. `Apache-2.0`
- [micropython](https://github.com/RT-Thread-packages/micropython) - MicroPython port package for RT-Thread. `MIT`
- [pikascript](https://github.com/pikasTech/pikascript) - Lightweight Python scripting support tool that is easy to customize. `MIT`
- [rapidjson](https://github.com/wuhanstudio/rapidjson) - A fast JSON parser/generator for C++ with both SAX/DOM style API. `MIT`
- [parson](https://github.com/IoTSharp/parson) - parson is a lightweight json library written in C,write by kgabis. `MIT`
- [rt_cjson_tools](https://github.com/maplerian/rt_cjson_tools) - Cjson tools library for RT thread. `Apache-2.0`
- [cJSON](https://github.com/RT-Thread-packages/cJSON) - Ultralightweight JSON parser in ANSI C. `MIT`
- [ljson](https://github.com/qiaoqidui/ljson) - JSON parser in ANSI C. `unknown`
- [agile_jsmn](https://github.com/loogg/agile_jsmn) - Lightweight JSON parser. `MIT`
- [jsmn](https://github.com/RT-Thread-packages/jsmn) - Jsmn is a world fastest JSON parser/tokenizer. `MIT`
- [Lua](https://github.com/liu2guang/Lua2RTT) - Lua port package for RT-Thread. `MIT`
- [rtt_rust](https://github.com/vito-chl/rtt_rust.git) - Rust support for rt-thread. `Apache-2.0`

### Signal process

- [DigitalCtrl](https://github.com/xuzhuoyi/DigitalCtrl) - Digital closed-loop control algorithm library. `MIT`
- [qpid](https://github.com/qiyongzhong0/rt-thread-qpid) - A quick and easy-to-use PID automatic control algorithm package, that supports incremental and positional algorithms. ` LGPL-2.1`
- [CMSIS-DSP](https://github.com/RT-Thread-packages/CMSIS-DSP) - CMSIS-DSP embedded compute library for Cortex-M and Cortex-A. `Apache-2.0`
- [kissfft](https://github.com/mborgerding/kissfft) - a Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid. `BSD-3-Clause`
- [ukal](https://github.com/wuhanstudio/ukal) - Kalman filter based on ulapack. `MIT`
- [fire_pid_curve](https://github.com/LONGZR007/fire_pid_curve.git) - . `LGPL-2.1`
- [.vscode](https://github.com/LONGZR007/fire_pid_curve.git) - . `LGPL-2.1`

### Tools

- [SEGGER_RTT](https://github.com/supperthomas/RTTHREAD_SEGGER_TOOL.git) - use the SEGGER RTT instead of console. `Apache-2.0`
- [vconsole](https://github.com/enkiller/vconsole) - A virtual console package. `Apache-2.0`
- [rtt_auto_exe_cmd](https://github.com/supperthomas/RTT_AUTO_EXE_CMD.git) - [AUTO]Exe the rtt cmd auto for ci. `Apache-2.0`
- [logmgr](https://github.com/RT-Thread-packages/logmgr.git) - A log management system for rt-thread. `Apache-2.0`
- [EasyFlash](https://github.com/armink-rtt-pkgs/EasyFlash) - Lightweight embedded flash memory library. Make flash to be a small KV database. `MIT`
- [cBox](https://github.com/enkiller/cbox) - C language box. `Apache-2.0`
- [EasyLogger](https://github.com/armink-rtt-pkgs/EasyLogger) - A ultra-lightweight(ROM<1.6K, RAM<0.3k), high-performance C/C++ log library. `MIT`
- [devmem](https://github.com/luanxg/devmem) - read/write memory/register tools. `GPL-2.0`
- [bs8116a](https://github.com/illusionlee/bs8116a.git) - Touch key of HOLTEK BS8116A-3. `MIT`
- [cpu_usage](https://github.com/enkiller/cpu_usage) - CPU usage statistics tool. `Apache-2.0`
- [anv_bench](https://github.com/wuhanstudio/anv_bench) - quick-and-dirty benchmarking system for quick prototyping. `MIT`
- [adbd](https://github.com/heyuanjie87/adbd) - Android Debug Bridge daemon implementation on RT-Thread. `Apache-2.0`
- [zdebug](https://github.com/beisongcrt/zdebug.git) - Convenient debugging tool, control print log at any time, view, set variable data, execute functions. `Apache-2.0`
- [lwlog](https://github.com/wuhanstudio/lwlog) - single header logging library. `MIT`
- [vofa_plus](https://github.com/xiaogeminghai/vofa_plus) - Realize serial port waveform function with vfoa+. `GPL-2.0`
- [rdb](https://github.com/RT-Thread-packages/rdb) - RT-Thread Debug Bridge. `GPL-2.0`
- [lunar_calendar](https://github.com/illusionlee/lunar_calendar.git) - A tool to convert a Gregorian calendar date into a lunar calendar. `MIT`
- [uMCN](https://github.com/JcZou/uMCN) - uMCN is a light-weight and powerful IPC module based on the publisher/subscriber model. `Apache-2.0`
- [ulog_easyflash](https://github.com/armink-rtt-pkgs/ulog_easyflash) - The ulog flash plugin by EasyFlash. `MIT`
- [snowflake](https://github.com/2022alpha/snowflake) - Snowflake algorithm is a distributed ID generation algorithm. `MIT`
- [UrlEncode](https://github.com/jch12138/UrlEncode.git) - a simple tool to Encode/Decode Url. `LGPL-2.1`
- [solar_terms](https://github.com/XYX12306/solar_terms.git) - A tool package for judging the relationship between 24 solar terms according to the date. `MIT`
- [anv_testsuit](https://github.com/wuhanstudio/anv_testsuit) - minimalist C/C++ unit test framework. `MIT`
- [wamr](https://github.com/bytecodealliance/wasm-micro-runtime.git) - WebAssembly Micro Runtime For RT-Thread. `Apache-2.0`
- [anv_trace](https://github.com/wuhanstudio/anv_trace) - trace the program flow. `MIT`
- [nr_micro_shell](https://github.com/Nrusher/nr_micro_shell) - Lightweight command line interaction tool. `MIT`
- [anv_memleak](https://github.com/wuhanstudio/anv_memleak) - check if there are memleaks. `MIT`
- [ulog_file](https://github.com/RT-Thread-packages/ulog_file.git) - The ulog file backend by filesystem. `Apache-2.0`
- [lwrb2rtt](https://github.com/Jackistang/lwrb2rtt) - Lightweight ring buffer manager. `MIT`
- [gps_rmc](https://github.com/maplerian/gps_rmc) - Used to parse $XXRMC type data of GPS module. `Apache-2.0`
- [gan_zhi](https://github.com/XYX12306/gan_zhi.git) - A tool package to get tiangan and dizhi informations according to the date and time. `MIT`
- [SystemView](https://github.com/RT-Thread-packages/SEGGER_SystemView) - SEGGER SystemView. `unknown`
- [CoreMark](https://github.com/wuhanstudio/coremark) - EEMBC’s CoreMark® is a benchmark that measures the performance of microcontrollers (MCUs) and central processing units (CPUs) used in embedded systems. `apache`
- [hash-match](https://github.com/smartmx/hash-match) - using hashmap on MCUs. `Apache-2.0`
- [fdt](https://github.com/RT-Thread-packages/fdt) - Device Tree package in RT-Thread. `LGPL-3.0`
- [RT_Trace](https://github.com/Ruboom/RT_Trace) - using J-Link realizes event monitoring. `Commercial License`
- [kdb](https://github.com/RT-Thread-packages/kdb) - Kernel debug tools. `Apache-2.0`
- [armv7m_DWT](https://github.com/balanceTWK/armv7m_DWT.git) - Memory monitoring component based on ARMV7M architecture. `MIT`
- [MemoryPerf](https://github.com/SummerLife/MemoryPerf) - Memory Performance Testing for ARM CPU. `MIT`
- [Dhrystone](https://github.com/wuhanstudio/dhrystone) - Dhrystone is a benchmark that measures the performance of microcontrollers (MCUs) and central processing units (CPUs) used in embedded systems. `apache`
- [mbedtls_bench](https://github.com/xfan1024/rttpkg-mbedtls_bench) - performance test for mbedtls. `MIT`
- [mem_sandbox](https://github.com/mysterywolf/mem_sandbox) - memory sandbox for RT-Thread. `MIT`
- [gbk2utf8](https://github.com/Ghazigq/gbk2utf8) - conversion between GBK and UTF8. `Apache-2.0`
- [Micro-XRCE-DDS-Client](https://github.com/JcZou/Micro-XRCE-DDS-Client) - The middleware component of micro-ros, which provides ros2 topic pub/sub ability. `Apache-2.0`
- [ChineseFontLibrary](https://github.com/lxzzzzzxl/Chinese_font_library) - a Chinese_font_library for rt-thread. `LGPL-2.1`
- [regex](https://github.com/thread-liu/tiny-regex-c.git) - A small regex implementation in C. `Unlicense`
- [CmBacktrace](https://github.com/armink-rtt-pkgs/CmBacktrace) - Advanced fault backtrace library for ARM Cortex-M series MCU. `MIT`
