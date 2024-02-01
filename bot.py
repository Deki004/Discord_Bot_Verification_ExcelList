import excel_file_read
import message_handling
import discord


sorted_discord_ids = excel_file_read.read_save()

async def action(message, user_message):
    try:
        response = message_handling.call(user_message)
        await message.author


def run_discord_bot():
    TOKEN = 'MTIwMTU0MDAyMDQ0MDQwNDA4OQ.GaXyaR.z6ja4m6C248nE6JJRNITqP3T_RhKeBzsWMAmFY'
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



    client.run(TOKEN)