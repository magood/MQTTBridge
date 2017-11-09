#!/bin/bash
source /home/deployer/MQTTBridge/MQTTBridge/env/bin/activate
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
cd /home/deployer/MQTTBridge/MQTTBridge
python MQTTBridge.py log
