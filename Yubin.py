from setting import *

client = commands.AutoShardedBot(command_prefix='/', intents=discord.Intents.all(), help_command=None)
with open("BYEOLKI\Yubin\config.json" , "r" , encoding = "UTF-8") as f:
    data = json.load(f)
token = data['Token']

async def checkCode(msg: discord.Interaction):
    if len(msg.message.content.split(" ")) > 1:
        code = msg.message.content.split(" ")[1]
        if code == client.user.discriminator:
            return 1

@client.command()
@commands.check(checkCode)
async def reload(msg: discord.Interaction):
    await msg.message.reply(
        content='대충 리로드 한 듯?',
        mention_author=False
    )
    os.system(f'pm2 restart {data["Name"]}')

@client.event
async def on_ready():
    await cogs_load()
    await client.tree.sync()
    print('대충 봇 켜진 듯?')

async def cogs_load():
    CogsFiles = [file[:-3] for file in os.listdir('BYEOLKI\Yubin\Cogs') if file.endswith(".py")]

    for file in CogsFiles:
        await client.load_extension(f"Cogs.{file}")

client.run(token)