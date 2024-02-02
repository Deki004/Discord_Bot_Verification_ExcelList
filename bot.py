import excel_file_read
import message_handling
import role_giving
import discord


sorted_discord_ids = excel_file_read.read_save()

async def action(message, user_message):
    try:
        response = message_handling.call(user_message)
        await message.author
    except:



def run_discord_bot():
    TOKEN = 'TOKEN'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_id = int(client.user.id)

        check = role_giving.check(user_id, sorted_discord_ids)
        # noinspection PySimplifyBooleanCheck
        if check == True:
            role_giving.roles()
        else:




    client.run(TOKEN)
