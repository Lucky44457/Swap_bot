import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 23939637
API_HASH = "477f51720ede3eef6997dbc442151c43"
BOT_TOKEN = "7796721104:AAFZ1S0SB96J-xUXrGA1505f13SBkNtq_Io"

app = Client("faceswap_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
sessions = {}

# 🚀 Commands
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(c: Client, m: Message):
    await m.reply("👋 Send a face photo to begin.")

@app.on_message(filters.command("help") & filters.private)
async def help_cmd(c: Client, m: Message):
    await m.reply("📚 Usage:\n1. /start\n2. Send source face image\n3. Send target video\n4. Use /cancel to reset")

@app.on_message(filters.command("cancel") & filters.private)
async def cancel_cmd(c: Client, m: Message):
    sessions.pop(m.from_user.id, None)
    await m.reply("✔️ Session cleared. Start again with /start")

# 📷 Handle source photo
@app.on_message(filters.photo & filters.private)
async def photo_handler(c: Client, m: Message):
    uid = m.from_user.id
    path = await m.download(f"{uid}_source.jpg")
    sessions[uid] = {"source": path}
    await m.reply("✅ Source face saved. Now send the target video.")

# 🎥 Handle target video
@app.on_message(filters.video & filters.private)
async def video_handler(c: Client, m: Message):
    uid = m.from_user.id
    if uid not in sessions or "source" not in sessions[uid]:
        return await m.reply("🚫 Send source face first.")
    src = sessions[uid]["source"]
    video_path = await m.download(f"{uid}_target.mp4")
    await m.reply("⏳ Processing... this can take a while")
    out = f"{uid}_result.mp4"
    proc = await asyncio.create_subprocess_exec("python3", "run_simswap_video.py", src, video_path, out)
    await proc.communicate()
    if os.path.exists(out):
        await m.reply_video(out, caption="✅ Here’s your swapped video")
    else:
        await m.reply("❌ Something went wrong during processing.")
    sessions.pop(uid, None)
    for f in (src, video_path, out):
        if os.path.exists(f): os.remove(f)

if __name__ == "__main__":
    app.run()
