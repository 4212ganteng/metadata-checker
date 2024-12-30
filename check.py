import subprocess
import sys

def get_video_metadata(video_file):
    try:
        # Menggunakan ffprobe untuk mendapatkan metadata video
        command = [
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration,bit_rate',
            '-show_streams',
            '-of', 'json',
            video_file
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print(f"[ERROR] Gagal mendapatkan metadata: {result.stderr}")
            sys.exit(1)

        return result.stdout
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        sys.exit(1)

def main():
    video_file = input("Masukkan path ke file video: ")

    # Memeriksa apakah file ada
    try:
        with open(video_file, 'r'):
            pass
    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan: {video_file}")
        sys.exit(1)

    # Mendapatkan metadata video
    metadata = get_video_metadata(video_file)
    print("[INFO] Metadata video:")
    print(metadata)

if __name__ == "__main__":
    main()