import discord
import asyncio
from discord.ext import commands

class EventLog:

    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message):
        '''Message delete event'''
        msg = message.content
        author = message.author
        em = discord.Embed(color = 0xffd500)
        if author.id == self.bot.user.id or author.bot == True:
            return
        if message.attachments:
            links = []
            for x in message.attachments:
                links.append(x.url)
            linkss = '\n'.join(links)
            data = "```Message Deleted! <Attachments Detected>"
            data += f"\nAuthor: {message.author}\nID: {author.id}\n"
            data += f"Message ID: {message.id}\n"
            data += f"Channel:\nName: {message.channel.name}\nID: {message.channel.id}\n\n"
            data += f"Content:```\n {msg}\n{linkss}"
            channel_id = 448873236290207744
            channel = self.bot.get_channel(channel_id)
            await channel.send(data)
        else:
            em.set_author(name = "Message Deleted! <Text Type>", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
            em.add_field(name = "Author: ", value = str(message.author) + f"\nID: {author.id}",inline = False)
            em.add_field(name = "Message ID:", value = message.id, inline = False)
            em.add_field(name = "Channel:", value = f"Name: {message.channel.name}" + f"\nID: {message.channel.id}", inline = False)
            em.add_field(name = "Content: ", value = "```"+msg+"```", inline = False)
            em.set_thumbnail(url = author.avatar_url)
            em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
            channel_id = 448873236290207744
            channel = self.bot.get_channel(channel_id)
            await channel.send(embed = em)

    async def on_message_edit(self, before, after):
        '''Message EDIT EVENT'''
        author = before.author = after.author
        if author.id == self.bot.user.id or author.bot == True:
            return
        msg_before = before.content
        msg_after = after.content
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Message Edited!", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "Author:", value = str(author) + f"\nID: {author.id}" ,inline = False)
        em.add_field(name = "Channel:", value = f"Name: {before.channel.name}\nID: {before.channel.id}", inline = False)
        em.add_field(name = "Original Message:", value = "```"+msg_before+"```", inline = False)
        em.add_field(name = "New Message:", value = "```"+msg_after+"```", inline = False)
        em.set_thumbnail(url = author.avatar_url)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_member_update(self, before, after):
        '''Member Nick Name update'''
        if before.nick != after.nick:
            em =discord.Embed(color = 0xffd500)
            em.set_author(name = "Nick Name Update!", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
            em.add_field(name = "User:", value = f"Name: {before.name}\nID: {before.id}", inline = False)
            em.add_field(name = "Old NickName: ", value = f"```{before.nick}```", inline = False)
            em.add_field(name = "New NickName:", value = f"```{after.nick}```", inline = False)
            em.set_thumbnail(url = before.avatar_url)
            em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
            channel_id = 448873236290207744
            channel = self.bot.get_channel(channel_id)
            await channel.send(embed = em)
        if before.roles != after.roles:
            em =discord.Embed(color = 0xffd500)
            em.set_author(name = "Member Role Updated", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
            em.add_field(name = "User:", value = f"Name: {before}", inline = False)
            r = [x.name for x in before.roles]
            em.add_field(name = "Old Roles ", value = f"```{r}```", inline = False)
            r1 = [x.name for x in after.roles]
            em.add_field(name = "New Roles:", value = f"```{r1}```", inline = False)
            em.set_thumbnail(url = before.avatar_url)
            em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
            channel_id = 448873236290207744
            channel = self.bot.get_channel(channel_id)
            await channel.send(embed = em)


    async def on_member_ban(self, guild, user):
        '''Ban event'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Member banned:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "User:", value = f"{user}")
        em.set_thumbnail(url = user.avatar_url)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_member_unban(self, guild, user):
        '''UnBan event'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Member unbanned:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "User:", value = f"{user}")
        em.set_thumbnail(url = user.avatar_url)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_guild_role_create(self, role):
        '''Role created'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Role Created:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "Name:", value = f"{role.name}", inline = False)
        perm = [x for x in role.permissions]
        em.add_field(name = "Name:", value = f"{perm}",inline = False)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_guild_role_delete(self, role):
        '''Role deleted'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Role Deleted:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "Name:", value = f"{role.name }")
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_guild_role_update(self, before,after):
        '''Role update'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Role Updated:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "Old Name:", value = f"{before.name}", inline = False)
        perm = [x for x in before.permissions]
        em.add_field(name = "Old Permissions:",value = f"```{perm}```", inline = False)
        em.add_field(name = "New Name:",value = f"{after.name}", inline = False)
        perm2 = [x for x in after.permissions]
        em.add_field(name = "New Permissions:",value = f"```{perm2}```", inline =  False)
        em.set_footer(text = "|Federation|",icon_url = self.bot.user.avatar_url)
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

    async def on_member_remove(self, member):
        '''member removed'''
        em =discord.Embed(color = 0xffd500)
        em.set_author(name = "Member Left:", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
        em.add_field(name = "Member:", value = f"{member}")
        channel_id = 448873236290207744
        channel = self.bot.get_channel(channel_id)
        await channel.send(embed = em)

def setup(bot):
    bot.add_cog(EventLog(bot))
