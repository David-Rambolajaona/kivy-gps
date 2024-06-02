#!/bin/bash

# Emplacement de l'outil sdkmanager
SDKMANAGER="${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/sdkmanager"

# Accepter les licences
yes | $SDKMANAGER --licenses
