# importing work here
from __future__ import unicode_literals
from pyrogram import Client, filters 
from pyrogram.types import ChatPermissions
import wikipedia
import os
import pyjokes
from quoters import Quote
import requests
from pyrogram.types import Message
from urllib.parse import urlparse
import youtube_dl
import sys
import traceback
from io import StringIO
from inspect import getfullargspec
import wget
import json
from config import Config, JSMAPI 
from sudoers import sudoers, root

# sharing my very sensitive info
app = Client("kodyk_bot", bot_token= Config.BOT_TOKEN ,
             api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",)

# stuff starts here
# /hello
@app.on_message(filters.command(["hello"]))
async def hello(_, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

# /start 
@app.on_message(filters.command(["start"]))
async def start(_, message):
    await message.reply_text('''
```
Hello NoobCoder, these are some commands you can try with the BOT,
        
        General:
        /areuded To Check if the bot is Alive
        /creator Creator's GitHub Profile
        /sourcecode Link to GitHub Repo
        /website Creator's Website
        /wikipedia Search For Articles in Wikipedia
        /quote Get Quotes
        /crackjoke Get A Geeky Joke
        /stackoverflow Search For Answers in StackOverFlow
        /dlmusic Download Music from YouTube and SoundCloud  
        /saavndl Download Music from JioSaavn
        /fastdl Download Music from JioSaavn (For Slow Hoeroku like Servers)
        /howzdweather Get Weather Report of a City
        
        Owner:
        /l To run your Python Code from Telegram 
        /shutdown Shutdown the Linux Machine on which the bot is running
        /cancelshutdown Cancel Shutdown

        Group Management:
        /mutenow Mute a User
        /unmutenow Unmute a User
        /delete Delete a Message
      

        Will add more commands soon...
```
        ''')

# howztheworld
@app.on_message(filters.command(["howztheworld"]))
async def howzwrld(_, message):
    await message.reply_text("The world is not perfect but it aint that bad...")

# /creator
@app.on_message(filters.command(["creator"]))
async def creator(_, message):
    await message.reply_text("https://github.com/Kody-K/")

# /sourcecode
@app.on_message(filters.command(["sourcecode"]))
async def whomadeu(_, message):
    await message.reply_text("https://github.com/Kody-K/kodykbot")

# kill yourself
@app.on_message(filters.regex("kill yourself"))
async def killyourself(_, message):
    await message.reply_text(f"same 2 you {message.from_user.mention}")

# areuded
@app.on_message(filters.regex("areuded"))
async def areuded(_, message):
    await message.reply_text("i am alive, go to hell")

# /website
@app.on_message(filters.command(["website"]))
async def website(_, message):
    await message.reply_text("kodyk.rf.gd")

# /wikipedia
@app.on_message(filters.command(['wikipedia']))
async def wikisearch(_, message):
        wikiquery = message.text.replace("wikipedia ", '')
        try:
            await message.reply_text("Searching Wikipedia...")
            wikiresult = wikipedia.summary(wikiquery, sentences = 4)
            await message.reply_text(wikiresult)
        except:
            await message.reply_text("Found Nothing...")

# /shutdown
@app.on_message(filters.command(['shutdown']) & filters.user(root))
async def shutdown(_, message):
    await message.reply_text("Shutting Down Servers in 60s...")
    os.system("sudo shutdown")

# /cancelshutdown
@app.on_message(filters.command(['cancelshutdown']) & filters.user(root))
async def cancelshutdown(_, message):
    await message.reply_text("Shutting Down Servers Cancelled")
    os.system("sudo shutdown -c")

# /crackjoke
@app.on_message(filters.command(['crackjoke']))
async def crackjoke(_, message):
    joke = pyjokes.get_joke(language="en", category="neutral")
    await message.reply_text(joke)

# /quote
@app.on_message(filters.command(['quote']))
async def quoter(_, message):
    quote = Quote.print()
    await message.reply_text(quote)

# /stackoverflow
@app.on_message(filters.command(['stackoverflow']))
async def stackoverflow(_, message):
        try:
            stfquery = message.text.split(None,1)[1]
            await message.reply_text("Searching for Answers...")
            stfresult = os.popen('howdoi ' + stfquery ).read()
            await message.reply_text(stfresult)
        except:
            await message.reply_text("Found Nothing...")

# /howzdweather
@app.on_message(filters.command(["howzdweather"]))
async def weather(_, message: Message):
    city = message.text.split(None, 1)[1]
    if len(message.command) != 2:
        await message.reply_text("/howzdweather [city]")
        return
    r = requests.get(f"https://wttr.in/{city}?mnTC0")
    data = r.text
    await message.reply_text(f"`{data}`")

# /dlmusic
ydl_opts = {
    'format': 'bestaudio',
    'writethumbnail': True
}

# /dlmusic
@app.on_message(filters.command(["dlmusic"]) & filters.user(sudoers))
async def music(_, message: Message):
    if len(message.command) != 2:
        await message.reply_text("`/dlmusic` needs a link as argument")
        return
    link = message.text.split(None, 1)[1]
    m = await message.reply_text(f"Downloading {link}",
                                 disable_web_page_preview=True)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            # .webm -> .weba
            basename = audio_file.rsplit(".", 1)[-2]
            thumbnail_url = info_dict['thumbnail']
            thumbnail_file = basename + "." + \
                get_file_extension_from_url(thumbnail_url)
            if info_dict['ext'] == 'webm':
                audio_file_weba = basename + ".weba"
                os.rename(audio_file, audio_file_weba)
                audio_file = audio_file_weba
    except Exception as e:
        await m.edit(str(e))
        return
        # info
    title = info_dict['title']
    webpage_url = info_dict['webpage_url']
    performer = info_dict['uploader']
    duration = int(float(info_dict['duration']))
    caption = f"[{title}]({webpage_url})"
    await m.delete()
    await message.reply_chat_action("upload_document")
    await message.reply_audio(audio_file, caption=caption,
                              duration=duration, performer=performer,
                              title=title, thumb=thumbnail_file)
    os.remove(audio_file)
    os.remove(thumbnail_file)


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]

# /fastdl
@app.on_message(filters.command("fastdl"))
async def song(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text("/fastdl requires an argument.")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        r = requests.get(f"{JSMAPI}{query}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]['song']
    slink = r.json()[0]['media_url']
    ssingers = r.json()[0]['singers']
    await message.reply_audio(audio=slink, title=sname,
                              performer=ssingers)
# /saavndl
@app.on_message(filters.command("saavndl"))
async def song(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text("/saavndl requires an argument.")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        r = requests.get(f"{JSMAPI}{query}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]['song']
    slink = r.json()[0]['media_url']
    ssingers = r.json()[0]['singers']
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await message.reply_audio(audio=ffile, title=sname,
                              performer=ssingers)
    os.remove(ffile)
    await m.delete()

# /mute
@app.on_message(filters.user(sudoers) & ~filters.forwarded & ~filters.via_bot & filters.command("mutenow"))
async def mute(_, message):    
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    victim = message.reply_to_message.from_user.id
    try:
        await message.chat.restrict_member(victim, permissions=ChatPermissions())
        await message.reply_text("Muted!")
    except:
        await message.reply_text("An Error Occured!")

# /unmute
@app.on_message(filters.user(sudoers) & ~filters.forwarded & ~filters.via_bot & filters.command("unmutenow"))
async def unmute(_, message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    victim = message.reply_to_message.from_user.id
    try:
        await message.chat.unban_member(victim)
        await message.reply_text("Unmuted!")
    except:
        await message.reply_text("An Error Occured!")

# /delete
@app.on_message(filters.user(sudoers) & filters.command("delete"))
async def delete(_, message: Message):
    await message.reply_to_message.delete()
    await message.delete()

# eval
async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)




async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_message(filters.user(root) & ~filters.forwarded & ~filters.via_bot & filters.command("l"))
async def executor(client, message):
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.delete()
        return
    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        "**QUERY**:\n```{}```\n\n**OUTPUT**:\n```{}```".format(
            cmd,
            evaluation.strip()
        )
    )
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await message.delete()
    else:
        await edit_or_reply(message, text=final_output)

app.run()


