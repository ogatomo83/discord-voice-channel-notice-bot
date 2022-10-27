import discord
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client(intents=discord.Intents.default())

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(1034998618341527592)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [1034551190786150451, 1034551190786150452, 1034551190786150457, 1034551190786150458]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("" + before.channel.name + " から、" + member.name + "  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("" + after.channel.name + " に、" + member.name + "  が参加しました！")

# Botのトークンを指定
client.run(os.environ['TOKEN'])