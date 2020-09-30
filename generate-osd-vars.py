#!/usr/bin/python3
#show the HBA cards used, the chassis size, if the chassis is a hybrid or not,
#if CAS is used or not, the lvm volumes

import subprocess
subprocess.run(["$ALIAS_DEVICE_PATH"])