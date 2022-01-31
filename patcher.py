import sys

def main():
    if len(sys.argv) < 4:
        print("Usage: python patcher.py patch.txt input.exe output.exe")
        return
    patch_path = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]
    with open(in_path, 'rb') as in_file:
        data = bytearray(in_file.read())  # all bytes
    addr = 0
    with open(patch_path, 'r') as patch_file:
        for line in patch_file:
            line = line.strip()
            if line.startswith('#'):
                continue
            elif line.startswith('@'):
                addr = int(line[1:], 16)
            else:
                patch_data = bytes.fromhex(line)
                data[addr:addr+len(patch_data)] = patch_data
                addr += len(patch_data)
    with open(out_path, 'wb') as out_file:
        out_file.write(data)
    print("done!")

if __name__ == "__main__":
    main()
