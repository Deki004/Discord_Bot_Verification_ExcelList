import openpyxl
import discord
from discord.ext import commands

# ROLE_NAME = 'KD3090'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


def read_column_values(filename, sheetname, column_letter):
    values = []
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook[sheetname]
        for cell in sheet[column_letter]:
            values.append(cell.value)
        workbook.close()
        values.sort()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except KeyError:
        print(f"Error: Sheet '{sheetname}' not found in '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

    return values


async def on_ready():
    print("Bot is running!")


async def on_message(message, ROLENAME=None):
    user_input = message.content.lower()
    if user_input == '!verify':
        if isinstance(message.author, discord.Member):
            if str(message.author.id) in column_values:
                role = discord.utils.get(message.guild.roles, id=1208716108807282709)
                if role:
                    await message.author.add_roles(role)
                    await message.channel.send(f'{message.author.mention} has been verified and given the role.')
                else:
                    await message.channel.send('Role not found.')
            else:
                await message.channel.send('Your Discord ID is not in the verification list. Please verify with a '
                                           'screenshot + Gov ID + Gov Name')
        else:
            await message.channel.send('Cannot verify users outside of guilds.')
    await client.process_commands(message)


# Example usage:
filename = "ID_List.xlsx"
sheetname = "ID_List"
column_letter = "C"  # Change this to the desired column letter
column_values = read_column_values(filename, sheetname, column_letter)
# print("Values in column:", column_values)

client.run('TOKEN')
