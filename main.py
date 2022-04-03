versions = ["JPN","ENG","ITA","GER","FRE","SPA","KOR"]
print("\n".join(f"{i} - {v}" for i,v in enumerate(versions)))
version = versions[int(input("Version: "))]
print(f"{version} Selected")
with open("arm9.bin", "rb") as arm9:
    with open("patched/arm9.bin", "wb+") as patched:
        arm9_bytes = bytearray(arm9.read())
        if version == "JPN":
            offset = 0x71F44 # 02071F44
            bl_instruction = 0xFD74F7AD
        elif version == "SPA":
            offset = 0x724A8 # 020724A8
            bl_instruction = 0xFC6CF7AD
        elif version == "KOR":
            offset = 0x725AC # 020725AC
            bl_instruction = 0xFBB6F7AD
        else:
            offset = 0x724B0 # 020724B0
            bl_instruction = 0xFC68F7AD
        
        arm9_bytes[offset:offset+0x4] = int.to_bytes(0x28019807,4,"little") # skip nonshiny pid generation
        arm9_bytes[offset+0x34:offset+0x38] = int.to_bytes(bl_instruction,4,"little") # make a call to mersenne twister
        arm9_bytes[offset+0x38:offset+0x3C] = int.to_bytes(0xE0560005,4,"little") # use result of call as pid

        patched.write(arm9_bytes)