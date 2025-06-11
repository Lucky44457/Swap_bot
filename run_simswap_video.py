import sys, os, subprocess

if len(sys.argv) != 4:
    print("Usage: python run_simswap_video.py source.jpg target.mp4 output.mp4")
    sys.exit(1)

src, tgt, out = sys.argv[1], sys.argv[2], sys.argv[3]

cmd = [
    "python3", "test_video_swapsingle.py",
    "--isTrain", "false",
    "--name", "people",
    "--Arc_path", "arcface_model/arcface_checkpoint.tar",
    "--pic_a_path", src,
    "--video_path", tgt,
    "--output_path", out
]
res = subprocess.run(cmd)
sys.exit(res.returncode)
