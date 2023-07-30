#!/usr/bin/env python

import os

Import("env", "projenv")

def postAction(source, target, env):
    uploaderflags= env.get("UPLOADERFLAGS")
    flash_args = [env.get("UPLOADER"),"--chip",projenv.get("BOARD_MCU")]
    flash_args.append("merge_bin")
    flash_args.append("--target-offset")
    flash_args.append("0x1000") # Offset 0x1000 to accomodate mu editor
    flash_args.append("-o")
    flash_args.append("bins/"+projenv.get("PIOENV")+"_fw.bin")
    flash_args.extend(uploaderflags[uploaderflags.index('--flash_mode'):])
    flash_args[flash_args.index('--flash_mode')+1] = projenv.get("BOARD_FLASH_MODE")
    flash_args[flash_args.index('--flash_freq')+1] = str(int(projenv.get("BOARD_F_FLASH")[:-1])//1000000)+"m" 
    flash_args.append(env.get("ESP32_APP_OFFSET"))
    flash_args.append(flash_args[flash_args.index('--flash_size')+3] .rsplit('/', 1)[0] + "/firmware.bin")
    cmd =  ' '.join(flash_args)
    print(cmd)

    os.system(cmd)

env.AddPostAction("buildprog", postAction)



