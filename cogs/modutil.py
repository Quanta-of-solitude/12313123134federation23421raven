"""Mod COG"""

import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import random
import myjson
import json
import os
import io

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def format_mod_embed(self, ctx, user, success, method, duration = None, location=None):
        """defaults"""
        emb = discord.Embed(timestamp=ctx.message.created_at)
        emb.set_author(name=method.title(), icon_url=user.avatar_url)
        emb.color = await ctx.get_dominant_color(user.avatar_url)
        emb.set_footer(text=f'User ID: {user.id}')
        if success:
            if method == 'ban' or method == 'hackban':
                emb.description = f'{user} was just {method}ned.'
            elif method == 'unmute':
                emb.description = f'{user} was just {method}d.'
            elif method == 'mute':
                emb.description = f'{user} was just {method}d for {duration}.'
            else:
                emb.description = f'{user} was just {method}ed.'
        else:
            emb.description = f"I do not have the required permissions to {method} {user.name}."

        return emb

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='Please write a reason!'):

        '''Kick someone from the server.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.kick_members == True or ctx.message.author.id == 280271578850263040:
            try:
                await ctx.guild.kick(member, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'kick')

            await ctx.send(embed=emb)

        else:
            okay = 'You do not have the required permissions to **KICK** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Kick', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)


    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='Please write a reason!'):
        '''Ban someone from the server.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id ==280271578850263040:
            try:
                await ctx.guild.ban(member, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'ban')

            await ctx.send(embed=emb)
        else:
            okay2 = 'You do not have the required permissions to **BAN** or **UNBAN** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Ban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay2, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)
    @commands.command()
    async def clean(self, ctx, limit : int=15):
        '''Clean a number of bot messages (owners only defined..)'''
        if ctx.message.author.id == 280271578850263040:
            await ctx.purge(limit=limit+1, check=lambda m: m.author == self.bot.user)

    @commands.command()
    async def unban(self, ctx, name_or_id, *, reason=None):
        '''Unban someone '''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040:
            ban = await ctx.get_ban(name_or_id)
            try:
                await ctx.guild.unban(ban.user, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, ban.user, success, 'unban')

            await ctx.send(embed=emb)
        else:
            okay3 = 'You do not have the required permissions to **BAN** or **UNBAN** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Unban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay3, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)

    @commands.command(aliases=['del','p','prune'])
    async def purge(self, ctx, limit : int, member:discord.Member=None):
        '''Clean a number of messages'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_messages == True or ctx.message.author.id == 280271578850263040:
            if member is None:
                await ctx.purge(limit=limit+1)
            else:
                async for message in ctx.channel.history(limit=limit+1):
                    if message.author is member:
                        await message.delete()
        else:
            okay4 = 'You do not have the required permissions to **Purge Messages**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Purge', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay4, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)

    @commands.command()
    async def banlist(self, ctx):
        '''See a list of banned users in the guild'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040:
            try:
                bans = await ctx.guild.bans()
            except:
                return await ctx.send('I dont have the perms to see bans.')

            em = discord.Embed(title=f'List of Banned Members ({len(bans)}):')
            em.description = ', '.join([str(b.user) for b in bans])
            em.color = await ctx.get_dominant_color(ctx.guild.icon_url)

            await ctx.send(embed=em)
        else:
            okay5 = 'You do not have the required permissions to **See Ban List**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Error', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay5, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)



    @commands.command()
    async def baninfo(self, ctx, *, name_or_id):
        '''Check the reason of a ban from the audit logs.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040:
            ban = await ctx.get_ban(name_or_id)
            em = discord.Embed()
            em.color = await ctx.get_dominant_color(ban.user.avatar_url)
            em.set_author(name=str(ban.user), icon_url=ban.user.avatar_url)
            em.add_field(name='Reason', value=ban.reason or 'None')
            em.set_thumbnail(url=ban.user.avatar_url)
            em.set_footer(text=f'User ID: {ban.user.id}')

            await ctx.send(embed=em)
        else:
            okay6 = 'You do not have the required permissions to **See Ban infos**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Error', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay6, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)


    @commands.command(aliases=['adrl','giverole'])
    async def addrole(self, ctx, member: discord.Member, *, rolename: str):
        '''Add a role to someone else.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('That role does not exist.')
            try:
                await member.add_roles(role)
                await ctx.send(f'Added: `{role.name}`')
            except:
                await ctx.send("I don't have the perms to add that role.")
        else:
            await ctx.send('You Do Not Have The Required Permission To **Add Roles**.')



    @commands.command(aliases=['rmrl','rmrole'])
    async def removerole(self, ctx, member: discord.Member, *, rolename: str):
        '''Remove a role from someone else.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('`That role does not exist.``')
            try:
                await member.remove_roles(role)
                await ctx.send(f'Removed: `{role.name}`')
            except:
                await ctx.send("I don't have the perms to remove that role.")
        else:
            await ctx.send('You Do Not Have The Required Permission To **Remove Roles**.')


    @commands.command()
    async def hackban(self, ctx, userid, *, reason=None):
        '''Ban someone not in the server'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040:
            try:
                userid = int(userid)
            except:
                await ctx.send('Invalid ID!')

            try:
                await ctx.guild.ban(discord.Object(userid), reason=reason)
            except:
                success = False
            else:
                success = True

            if success:
                async for entry in ctx.guild.audit_logs(limit=1, user=ctx.guild.me, action=discord.AuditLogAction.ban):
                    emb = await self.format_mod_embed(ctx, entry.target, success, 'hackban')
            else:
                emb = await self.format_mod_embed(ctx, userid, success, 'hackban')
            await ctx.send(embed=emb)
        else:
            okay7 = 'You do not have the required permissions to **Ban** or **Unban** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Ban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay7, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)


    @commands.command()
    async def mute(self, ctx, member:discord.Member, duration, *, reason=None):
        '''Denies someone from chatting in all text channels and talking in voice channels for a specified duration'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040:
            unit = duration[-1]
            if unit == 's':
                time = int(duration[:-1])
                longunit = 'seconds'
            elif unit == 'm':
                time = int(duration[:-1]) * 60
                longunit = 'minutes'
            elif unit == 'h':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'hours'
            else:
                await ctx.send('Invalid Unit! Use `s`, `m`, or `h`.')
                return

            progress = await ctx.send('Muting user!')
            try:
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)

                for channel in ctx.guild.voice_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'mute', f'{str(duration[:-1])} {longunit}')
            progress.delete()
            await ctx.send(embed=emb)
            await asyncio.sleep(time)
            try:
                for channel in ctx.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                pass
        else:
            okay8 = 'You do not have the required permissions to **Mute** or **Unmute** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Mute', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay8, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)


    @commands.command()
    async def unmute(self, ctx, member:discord.Member, *, reason=None):
        '''Removes channel overrides for specified member'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040:
            progress = await ctx.send('Unmuting user!')
            try:
                for channel in ctx.message.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'unmute')
            progress.self.delete()
            await ctx.send(embed=emb)
        else:
            okay9 = 'You do not have the required permissions to **Mute** or **Unmute** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Mute', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay9, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Federation|')

            await ctx.send(embed=em)

    @commands.command()
    async def warn(self,ctx,member:discord.Member=None,*,reason:str=None):
        '''warn system'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.author.guild_permissions.ban_members == True or ctx.author.guild_permissions.kick_members == True:
            try:
                if reason == None:
                    await ctx.send("**Please Provide a reason!**")
                    return

                user = member
                url2 = "{}".format(os.environ.get("warn_logs"))
                warn = myjson.get(url2)
                warn = json.loads(warn)
                if "{}".format(user.id) not in warn:
                    warn[f"{user.id}"] = {}
                    warn[f"{user.id}"]["count"] = 1
                    warn[f"{user.id}"]["name"] = "{}".format(str(user))
                    warn[f"{user.id}"]["reason"] = str(reason)
                    url2 = myjson.store(json.dumps(warn),update=url2)
                else:
                    warn[f"{user.id}"]["count"] += 1
                    warn[f"{user.id}"]["name"] = "{}".format(str(user))
                    warn[f"{user.id}"]["reason"] = str(reason)
                    url2 = myjson.store(json.dumps(warn),update=url2)
                em = discord.Embed(color = 0xffd500)
                notify = ctx.guild.get_member(user_id = int(user.id))
                em.set_author(name = "Member Warned!", icon_url = "https://image.ibb.co/jmajRT/Federation.png")
                em.add_field(name = "**Member:** ", value = "**"+str(user)+"**"+ f"\n**ID: {user.id}**",inline = False)
                em.add_field(name = "**Warned By:**", value = f"**{ctx.author}**", inline = False)
                em.add_field(name = "**Reason:**", value = "```"+reason+"```", inline = False)
                em.add_field(name = "**Count:**", value = "{}".format(warn[f"{user.id}"]["count"]), inline = False)
                channel_id = 449617657910525953
                channel = self.bot.get_channel(channel_id)
                await channel.send(embed = em)
                await ctx.send("`Sent warning to {}, and count recorded.`".format(user))
            except Exception as e:
                print(e)
                await ctx.send("`Either can't send warn message to member, or member provided isnt in the server.`")


    @commands.command()
    async def resetcounter(self, ctx, *,uids:str = None):
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.author.guild_permissions.ban_members == True or ctx.author.guild_permissions.kick_members == True:
            try:
                url2 = "{}".format(os.environ.get("warn_logs"))
                warn = myjson.get(url2)
                warn = json.loads(warn)
                if uids == None:
                    await ctx.send("`No member provided`")
                    return
                if "{}".format(uids) in warn:
                    warn[f"{uids}"]["count"] = 0
                    warn[f"{uids}"]["reason"] = "None"
                    url2 = myjson.store(json.dumps(warn),update=url2)
                    await ctx.send("`Warnings reset for {}`".format(warn[f"{uids}"]["name"]))
                else:
                    await ctx.send("`No such id in database`")
            except Exception as e:
                print(e)
                await ctx.send("`Couldn't connect to database atm, try again later.`")
    @commands.command()
    async def warnlist(self,ctx):
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.author.guild_permissions.ban_members == True or ctx.author.guild_permissions.kick_members == True:
            try:
                url2 = "{}".format(os.environ.get("warn_logs"))
                warn = myjson.get(url2)
                warn = json.loads(warn)
                warnlist = []
                for x in warn:

                    warnlist.append("Count: {}       {}".format(warn[x]["count"],warn[x]["name"]))
                warnstr = '\n'.join(warnlist)
                try:
                    await ctx.send(f"```{warnstr}```")
                except:
                    paginated_text = ctx.paginate(warnstr)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```\n{page}\n```')
                            break
                        await ctx.send(f'```\n{page}\n```')

            except Exception as e:
                print(e)




def setup(bot):
	bot.add_cog(Mod(bot))
