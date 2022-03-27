# TODO: auto-detect version?
with open("arm9.bin", "rb") as arm9:
    with open("patched/arm9.bin", "wb+") as patched:
        arm9_bytes = bytearray(arm9.read())

        shiny_lock_branch = arm9_bytes.index(bytes.fromhex("3C F9 07 98 00")) + 4 # if (shiny == 0) 0x20724AE
        arm9_bytes[shiny_lock_branch] = 0x01 # -> if (shiny == 1)

        mt_replace = arm9_bytes.index(bytes.fromhex("60 40 00 04 05 43")) # forced shiny pid 0x20724E4
        arm9_bytes[mt_replace:mt_replace+6] = bytes.fromhex("AD F7 74 FD 05 00") # mt_rng pid 

        patched.write(arm9_bytes)