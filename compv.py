import os, argparse, subprocess

def encode(file_path, q=30):
    dirname = os.path.dirname(file_path)
    basename = os.path.basename(file_path)
    root, ext = os.path.splitext(basename)
    output_filename = root + '.comp' + ext
    output_filepath = os.path.join(dirname, output_filename)
    
    ffmpeg_args = [
        "-i", file_path,
        "-y",
        "-c:v", "hevc_nvenc",
        "-c:a", "copy",
        "-cq", str(q),
        output_filepath
        ]
    cmd = ["ffmpeg"]
    cmd.extend(ffmpeg_args)
    
    cp = subprocess.run(cmd, cwd=dirname)
    
    print()
    
    if cp.returncode == 0 and os.path.exists(output_filepath):
        sz_before = os.path.getsize(file_path)
        sz_before /= 1024 * 1024
        sz = os.path.getsize(output_filepath)
        sz /= 1024 * 1024
        
        # if file is broken
        if sz < 10:
            return
        
        r = sz / sz_before
        print("Compressed: {:.2f} (MiB) -> {:.2f} (MiB)".format(sz_before, sz))
        print("Saved {:.2f} MiB ({:.2f}%)".format(sz_before - sz, (1 - r) * 100))
        
        print()
        
        f = input("Delete original file? (y/n): ")
        if f.lower() == 'y':
            os.remove(file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Path to the file to be compressed')
    args = parser.parse_args()
    encode(args.input)

if __name__ == '__main__':
    main()