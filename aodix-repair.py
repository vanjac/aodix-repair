import sys, struct

SEARCH_BUFFER = 1024
MAX_PATH = 260

# find a substring in a file (binary) and seek to the location
# return True if string was found
def file_search(f, sub):
    while True:
        data = f.read(SEARCH_BUFFER)
        index = data.find(sub)
        if index != -1:
            f.seek(-len(data) + index, 1)
            return True
        if len(data) <= len(sub):
            return False
        f.seek(-len(sub), 1)  # in case string is across buffer boundary

def main():
    filepath = sys.argv[1]
    with open(filepath, 'r+b') as f:
        f.seek(0x002C6060, 0)
        # little endian unsigned int
        num_events = struct.unpack('<I', f.read(4))[0]
        f.seek(num_events * 16, 1) # start of vst table

        ok_count = 0
        repair_count = 0
        while file_search(f, b'.dll\x00'):
            # include search string, without null
            # leaves enough room for 0x01 at beginning
            f.seek(-MAX_PATH + 4, 1)
            data = f.read(MAX_PATH)
            index = MAX_PATH - 1

            # determine if this is an actual instrument name
            # instrument names start with 0x01
            null_index = None
            valid_vst = True
            while index >= 0:
                value = data[index]
                if value == 1:
                    break
                if null_index:
                    if value != 0:
                        # this is a leftover fragment of a name
                        valid_vst = False
                        break
                else:
                    if value == 0:
                        null_index = index
                index -= 1
            
            if valid_vst and null_index:
                # repair the corrupted name
                vst_name = data[null_index+1:]
                print("Repair:", vst_name)
                f.seek(-MAX_PATH + index + 1, 1)
                f.write(vst_name)
                f.write(bytes([0]))
                f.seek(MAX_PATH - index - len(vst_name), 1)
                repair_count += 1
            elif valid_vst:
                print("OK:    ", data[index+1:])
                ok_count += 1

        print(ok_count, "VSTs OK")
        print(repair_count, "VSTs repaired")

if __name__ == "__main__":
    main()
