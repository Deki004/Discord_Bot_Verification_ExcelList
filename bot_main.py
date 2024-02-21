import openpyxl
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefixes = {}


def get_prefix(client, message):
    return prefixes.get(message.guild.id, '!')


client = commands.Bot(command_prefix=get_prefix, intents=intents)


def read_column_values(filename, sheetname, column_letter):
    values = []
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook[sheetname]
        for cell in sheet[column_letter]:
            values.append(str(cell.value))
        workbook.close()
        values.sort()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except KeyError:
        print(f"Error: Sheet '{sheetname}' not found in '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

    return values


@client.event
async def on_ready():
    print("Bot is running!")


@client.command()
async def verify(ctx):
    if isinstance(ctx.author, discord.Member):
        if str(ctx.author.id) in column_values:
            role = discord.utils.get(ctx.guild.roles, id=ROLEID)
            if role is not None:
                await ctx.author.add_roles(role)
                await ctx.send(f"{ctx.author.mention} has been verified and given the role.")
            else:
                await ctx.send("Role not found")
        else:
            await ctx.send(
                "Your Discord ID is not in the verification list. Please verify with a screenshot + Gov ID + Gov Name")
    else:
        await ctx.send("Cannot verify users outside of guilds.")


filename = "ID_List.xlsx"
sheetname = "ID_List"
column_letter = "C"
column_values = read_column_values(filename, sheetname, column_letter)


# @client.command()
# async def setprefix(ctx, prefix):
#    if commands.author.has_permissions(administrator=True):
#        prefixes[ctx.guild.id] = prefix
#        await ctx.send(f"The prefix has changed to: `{prefix}`")
#    else:
#        await ctx.send("Youre not allowed to do that!")

@client.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    prefixes[ctx.guild.id] = prefix
    await ctx.send(f"The prefix has changed to: `{prefix}`")


TOKEN = "MTIwMTU0MDAyMDQ0MDQwNDA4OQ.GdE53t.llLi9WXm-ZlFqLg9B-d0_PpBdtW4BAN_Ac2aT8"
ROLEID = 1208716108807282709
client.run(TOKEN)
