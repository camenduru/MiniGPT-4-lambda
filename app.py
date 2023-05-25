import os
os.system(f"git lfs install")
os.system(f"git clone -b dev https://github.com/camenduru/minigpt4 /home/demo/source/minigpt4")
os.chdir(f"/home/demo/source/minigpt4")

os.system(f"https://huggingface.co/ckpt/minigpt4/resolve/main/minigpt4.pth -O /home/demo/source/minigpt4/checkpoint.pth")
os.system(f"https://huggingface.co/ckpt/minigpt4/resolve/main/blip2_pretrained_flant5xxl.pth -O /home/demo/source/minigpt4/blip2_pretrained_flant5xxl.pth")

os.system(f"pip install -r requirements.txt")
os.system(f"python app.py")