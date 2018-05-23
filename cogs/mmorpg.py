'''
MMORPG COG written by Noble#5556

'''

import os
import re
import discord
import asyncio
import json
import random
from discord.ext import commands
import requests
import socket
import locale
from bs4 import BeautifulSoup
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

class mmorpg:
    def __init__(self,bot):
        self.bot = bot
    @property
    def server_details(self):
        '''loading the game api for server details'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["api_link"] == "api_link_here":
                api_link = os.environ.get("api_link")
            else:
                api_link = link["api_link"]
        return api_link
    @property
    def character_page_link(self):
        '''getting the character link'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["char_link"] == "link_here":
                char_link = os.environ.get("char_link")
            else:
                char_link = link["char_link"]
        return char_link
    @property
    def item_link(self):
        '''getting the item_api'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["item_link"] == "item_link_here":
                item_link = os.environ.get("item_link")
            else:
                item_link = link["item_link"]
        return item_link


    def dostuff(self, text):
        text = str(text)
        text = text.partition("&")[0]
        return text[2:]

    @commands.command(aliases=['character'])
    async def char(self, ctx, *, args:str = None):
        '''Finding the character page of the player'''
        try:
            player = []
            badges = []
            if args == None:
                await ctx.send(content = "`Missing name`")
                return
            link = self.character_page_link
            new_text = args.replace(' ','+')
            link = link+new_text
            info = {}
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            g_data = soup.find_all("h3")
            f_data = soup.find_all("div",{"class": "text-center nopadding"})
            img_data = soup.findAll('img',alt=True,src = True)
            c = soup.find("img", alt=True, src=re.compile(r'\/Content\/img\/char\/.+.png'))
            await ctx.trigger_typing()
            for n in f_data:
                kjk = n.text
                player.append(kjk)
                lolewii = '\n'.join(player)
            for h in g_data:
                fmf = h.text
                badges.append(fmf)
                klma = '\n'.join(badges)
            info['cl'] = c['alt']

            info['clpic'] = 'https://game.aq3d.com' + c['src']
            #loki = lolewii+"Class:"+"\n"+info['cl']+"\n"+"\n"+" **__Badges__** \n"+" **"+klma+"**"
            player_name = lolewii
            player_class = info['cl']
            player_badges = klma
            #return {"user": loki,"pic": info['clpic']}
            data = f"**Name:** {player_name}\n"
            data += f"**Class:** {player_class}\n\n"
            data += f"**Badges:**\n\n{player_badges}"
            try:
                character_embed = discord.Embed(title = "{}".format(player_name), url = link)
                character_embed.set_author(name = "Character Info:",icon_url = "https://www.aq3d.com/media/1322/aq3d-dragonheadlogo.png" )
                character_embed.add_field(name = "**Class:**", value = player_class, inline = True)
                character_embed.add_field(name = "**__Badges__**", value = player_badges, inline = False)
                character_embed.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                character_embed.set_footer(text = "|Char-Page, +mchar for mobile friendly|",icon_url = self.bot.user.avatar_url)
                character_embed.set_image(url = "{}".format(info['clpic']))
                character_embed.color=discord.Colour.red()
                await ctx.send(content= "**use +mchar for mobile friendly**", embed = character_embed)
            except:

                paginated_text = ctx.paginate(data)
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        em = discord.Embed(color= 0000, description = page)
                        em.set_image(url = "{}".format(info['clpic']))
                        em.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                        em.set_footer(text = "|Char-Page, +mchar for mobile friendly|",icon_url = self.bot.user.avatar_url)
                        out = await ctx.send(embed = em)
                        break
                    em = discord.Embed(color = 0000, description = page)
                    em.set_image(url = "{}".format(info['clpic']))
                    em.set_thumbnail(url = "https://image.ibb.co/bTDven/logo_aq3d.png")
                    em.set_footer(text = "|Char-Page, +mchar for mobile friendly|",icon_url = self.bot.user.avatar_url)
                    await ctx.send(embed = em)

            del player[:]
            del badges [:]
        except Exception as e:
            print(e)
            try:
                text_made = f"Name: {player_name}\nClass: {player_class}\n\nBadges:\n{player_badges}"
                await ctx.send("__**Note:**__ This is being displayed like this because I am missing The **Embed Permission** in the server.\n"+"```"+text_made+"```")
            except Exception as err:
                print(err)
                await ctx.send("`-NONE FOUND-`")

    @commands.command(aliases=['mobilecharacter'])
    async def mchar(self, ctx, *, args:str = None):
        '''Finding the character page of the player (mobile version)'''
        try:
            player = []
            badges = []
            if args == None:
                await ctx.send(content = "`Missing name`")
                return
            link = self.character_page_link
            new_text = args.replace(' ','+')
            link = link+new_text
            info = {}
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            g_data = soup.find_all("h3")
            f_data = soup.find_all("div",{"class": "text-center nopadding"})
            img_data = soup.findAll('img',alt=True,src = True)
            c = soup.find("img", alt=True, src=re.compile(r'\/Content\/img\/char\/.+.png'))
            await ctx.trigger_typing()
            for n in f_data:
                kjk = n.text
                player.append(kjk)
                lolewii = '\n'.join(player)
            for h in g_data:
                fmf = h.text
                badges.append(fmf)
                klma = '\n'.join(badges)
            info['cl'] = c['alt']

            info['clpic'] = 'https://game.aq3d.com' + c['src']
            #loki = lolewii+"Class:"+"\n"+info['cl']+"\n"+"\n"+" **__Badges__** \n"+" **"+klma+"**"
            player_name = lolewii
            player_class = info['cl']
            player_badges = klma
            #return {"user": loki,"pic": info['clpic']}
            data = f"-Character Info-\n\nName: {player_name}\n"
            data += f"Class: {player_class}\n\n"
            data += f"Badges:\n\n{player_badges}"
            try:
                out = await ctx.send("```\n"+data+"\n```")
            except:
                paginated_text = ctx.paginate(data)
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```\n{page}\n```')
                        break
                    await ctx.send(f'```\n{page}\n```')

            del player[:]
            del badges [:]
        except Exception as e:
            print(e)
            await ctx.send("`-NONE FOUND-`")




    @commands.command(aliases=['aq3dservers','serveraq3d','aqs'])
    async def aq3dserver(self,ctx):
        '''Details about aq3d Servers'''
        try:
            link = self.server_details
            rw = requests.get(link)
            soup = BeautifulSoup(rw.content, 'lxml')
            g= soup.find("p").get_text()
            server_details = json.loads(g)


            try:
                server1_state = server_details[0]["State"]
                if server1_state == True:
                    server1_state = "**Online**"
                elif not server1_state:
                    server1_state = "**Unknown**"
                else:
                    server1_state = "**Offline**"
            except Exception as e:
                print(e)
                server1_state = "**Unknown**"

            try:
                server2_state = server_details[1]["State"]

                if server2_state == True:
                    server2_state = "**Online**"
                elif not server2_state:
                    server2_state = "**Unknown**"
                else:
                    server2_state = "**Offline**"
            except Exception as e:
                print(e)
                server2_state = "**Unknown**"

            try:
                countr = server_details[0]["UserCount"]
                if countr:
                    countr = server_details[0]["UserCount"]
                elif not countr:
                    countr = "0"
            except Exception as e:
                print(e)
                countr = "None"
            try:
                countb = server_details[1]["UserCount"]
                if countb:
                    countb = server_details[1]["UserCount"]
                elif not countb:
                    countb = "0"
            except Exception as e:
                print(e)
                countb = "None"

            data = "Server Name: **{}**\n".format(server_details[0]["Name"])
            data +="Count: {}/{}\n".format(countr,server_details[1]["MaxUsers"])
            data +="Status: %s\n\n"%(server1_state)
            data += "Server Name: **{}**\n".format(server_details[1]["Name"])
            data +="Count: {}/{}\n".format(countb,server_details[1]["MaxUsers"])
            data +="Status: %s\n\n"%(server2_state)
            data +="\n__**Total Players: {}**__\n\n".format(int(countr)+int(countb))
            server_embed = discord.Embed(description = data)
            server_embed.set_author(name = "Server Details:")
            server_embed.set_thumbnail(url = "https://www.aq3d.com/media/1507/aq3d-full-logo760.png")
            server_embed.set_footer(text = "|Federation| requested by {}".format(ctx.message.author.name), icon_url = self.bot.user.avatar_url)
            server_embed.color=discord.Colour.blue()
            await ctx.send(embed = server_embed)
        except Exception as e:
            print(e)
            await ctx.send("`Servers are offline or under testing. `")

    @commands.command()
    async def aq3ditem(self,ctx, *,args:str = None):
        '''AQ3D item details'''
        try:
            buggy = []
            if args == None:
                await ctx.send("`Missing item name`")
                return
            link = self.item_link
            new_text = args.replace(' ','-')
            new_text = new_text.replace("'", "-")
            new_text = new_text.replace("’", "-")
            new_text = new_text.lower()
            link = link+new_text
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            things = {}
            things["Text"] = soup.find("div", {"id": "page-content"}).get_text()
            things=dict(map(str.strip,x) for x in things.items())
            matcher = things["Text"].replace("\n\n","")
            print(matcher)
            pattern = re.compile("//<.*",re.DOTALL)
            m = pattern.findall(things["Text"])
            replacer = m
            print(m)
            if not m:
                new = things["Text"].replace("\n\n\n",'\n')
            else:
                new = things["Text"].replace(replacer[0], "----")
                new = new.replace("\n\n\n",'\n')
            buggy.append(new)
            new_data = '\n'.join(buggy)
            await ctx.trigger_typing()

            try:
                c = soup.find("img", alt=True,src=re.compile(r'\/i.imgur.com\/.+.png'))
                data = c['src']
            except:
                c = soup.find("img", alt=True, src=re.compile(r'\/local--files\/.+.png'))
                data = c['src']

            #return {"stuff": new_data, "pic": data}
            try:
                item_embed = discord.Embed(description = new_data)
                item_embed.set_author(name = "Item Info: |%s|"%(args))
                item_embed.set_image(url = data)
                item_embed.color=discord.Colour.green()
                item_embed.set_footer(text = "|Federation| requested by {}".format(ctx.message.author.name), icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = item_embed)
                del buggy[:]
            except Exception as e:
                item_embed = discord.Embed(description = "-NONE-, Please, check the name of the item correctly.")
                item_embed.color=discord.Colour.red()
                await ctx.send(embed = item_embed)
                print(str(e))
                del buggy[:]
        except Exception as e:
            print(e)
            #pass
            try:
                results = []
                new_text = args.replace(' ','-')
                new_text = new_text.lower()
                query = new_text
                link = "http://aq-3d.wikidot.com/search:site/q/"+query

                r = requests.get(link)
                soup = BeautifulSoup(r.content, 'lxml')
                names = soup.find_all("div", {"class": "title"})
                for x in names:
                    results.append(x.text)
                refined_names = ''.join(results[:4])
                if not refined_names:
                    refined_name = "None found!"
                    em = discord.Embed(description = refined_name)
                    em.set_author(name = "Search Query:")
                    em.set_footer(text = "|Federation| requested by {}".format(ctx.message.author.name), icon_url = self.bot.user.avatar_url)
                    em.color=discord.Colour.red()
                    await ctx.send(content = "`Error: Couldn't find!!", embed = em)
                else:
                    refined_names = "**"+refined_names+"**"
                    em = discord.Embed(description = refined_names)
                    em.set_author(name = "Search Query:")
                    em.set_footer(text = "|Federation| requested by {}".format(ctx.message.author.name), icon_url = self.bot.user.avatar_url)
                    em.color=discord.Colour.red()
                    await ctx.send(content = "`Error: Couldn't find! Did you mean any of these: Search again using one of the names as listed below.`", embed = em)
            except Exception as e:
                print(e)
                await ctx.send("`Error: Internal Error`")


    @commands.command(aliases=['aqwserver','serveraqw'])
    async def aqwservers(self,ctx):
        '''aqw servers info'''
        try:
            session = requests.Session()
            botss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ips = "{}".format(os.environ.get("IP_add"))
            url = '{}'.format(os.environ.get("aqw_link"))
            port = "{}".format(os.environ.get("PORT_A"))
            port = int(port)
            botss.connect((ips, port))
            values = {'unm': '{}'.format(os.environ.get("log_in")),
                      'pwd': '{}'.format(os.environ.get("passw"))}
            m = session.post(url, data = values)
            soup = BeautifulSoup(m.content, 'lxml')
            names = []
            counts = []
            languages = []
            g_data = soup.find_all("servers")
            await ctx.trigger_typing()
            for s in g_data:
                names.append(s["sname"])
                counts.append(s["icount"])
                languages.append(s["slang"])

            data = "**Server:** {}\n".format(names[0])
            data += "**Counts:** {}\n".format(counts[0])
            data += "**Lang:** {}\n\n".format(languages[0])
            data1 = "**Server:** {}\n".format(names[1])
            data1 += "**Counts:** {}\n".format(counts[1])
            data1 += "**Lang:** {}\n\n".format(languages[1])
            data2 = "**Server:** {}\n".format(names[2])
            data2 += "**Counts:** {}\n".format(counts[2])
            data2 += "**Lang:** {}\n\n".format(languages[2])
            data3 = "**Server:** {}\n".format(names[3])
            data3 += "**Counts:** {}\n".format(counts[3])
            data3 += "**Lang:** {}\n\n".format(languages[3])
            data4 = "**Server:** {}\n".format(names[4])
            data4 += "**Counts:** {}\n".format(counts[4])
            data4 += "**Lang:** {}\n\n".format(languages[4])
            data5 = "**Server:** {}\n".format(names[5])
            data5 += "**Counts:** {}\n".format(counts[5])
            data5 += "**Lang:** {}\n\n".format(languages[5])
            data6 = "**Server:** {}\n".format(names[6])
            data6 += "**Counts:** {}\n".format(counts[6])
            data6 += "**Lang:** {}\n\n".format(languages[6])
            data7 = "**Server:** {}\n".format(names[7])
            data7 += "**Counts:** {}\n".format(counts[7])
            data7 += "**Lang:** {}\n\n".format(languages[7])
            data8 = "**Server:** {}\n".format(names[8])
            data8 += "**Counts:** {}\n".format(counts[8])
            data8 += "**Lang:** {}\n\n".format(languages[8])
            data9 = "**Server:** {}\n".format(names[9])
            data9 += "**Counts:** {}\n".format(counts[9])
            data9 += "**Lang:** {}\n\n".format(languages[9])
            em = discord.Embed()
            em.set_thumbnail(url = "https://www.aq.com/img/network/logo-md-aqw.png")
            em.set_author(name = "AQW SERVERS:", icon_url = "http://2.bp.blogspot.com/-Y9DNqq4OjEE/TcrNi3qSACI/AAAAAAAAAEk/Bfk_CKqN3B0/s320/aqw.jpg")
            em.add_field(name = "1.", value = data,inline = False)
            em.add_field(name = "2.", value = data1,inline = True)
            em.add_field(name = "3.", value = data2,inline = True)
            em.add_field(name = "4.", value = data3,inline = True)
            em.add_field(name = "5.", value = data4,inline = True)
            em.add_field(name = "6.", value = data5,inline = True)
            em.add_field(name = "7.", value = data6,inline = True)
            em.add_field(name = "8.", value = data7,inline = True)
            em.add_field(name = "9.", value = data8,inline = True)
            em.add_field(name = "10.", value = data9,inline = True)
            em.set_footer(text = "|Federation|", icon_url = self.bot.user.avatar_url)
            em.colour = discord.Colour.red()
            await ctx.send(embed = em)
            botss.shutdown(socket.SHUT_RDWR)
            botss.close()
        except Exception as e:
            await ctx.send("`Error: {}`".format(e))


    @commands.command(aliases = ['aqwbadge'])
    async def aqwbadges(self,ctx,args:str = None, args1:str = None):
        try:
            if args == None:
                await ctx.send("`Error: No Name Provided!`")
                return
            if args1 == None:
                searched = args
                print(args)
                args = args.lower()
                args = args.replace(' ', '+')
                url = "{}".format(os.environ.get("BADGE_AQW"))
                url = url+args
                r = requests.get(url)
                badges = []
                soup = BeautifulSoup(r.content, 'lxml')
                data = soup.find('div',{"class": "achievements"})
                data = data.find_all("a")
                await ctx.trigger_typing()
                for x in data:
                    try:
                        badge = x.attrs
                        badges.append("`"+badge["title"]+"`")
                    except AttributeError:
                        pass
                badge_names = ', '.join(badges)
                em = discord.Embed(description = badge_names)
                em.set_author(name = "Player Badges for |{}|:".format(searched), icon_url = "http://aqworldswiki.com/images/aqworldswiki.com/7/77/Artix.png")
                em.set_thumbnail(url = "https://vignette.wikia.nocookie.net/aqwikia/images/e/eb/AQ_new_logo.png")
                em.colour = discord.Colour.red()
                await ctx.send(content = "**UNDER TESTING: (will be developed further)**",embed =em)
            else:
                args1 = int(args1)
                searched = args
                args = args.lower()
                args = args.replace(' ', '+')
                url = "{}".format(os.environ.get("BADGE_AQW"))
                url = url+args
                r = requests.get(url)
                badges = []
                soup = BeautifulSoup(r.content, 'lxml')
                data = soup.find('div',{"class": "achievements"})
                data = data.find_all("a")
                await ctx.trigger_typing()
                for x in data:
                    try:
                        badge = x.attrs
                        badges.append("`"+badge["title"]+"`")
                    except AttributeError:
                        pass
                badge_names = ', '.join(badges[:args1])
                em = discord.Embed(description = badge_names)
                em.set_author(name = "Player Badges for |{}|:".format(searched), icon_url = "http://aqworldswiki.com/images/aqworldswiki.com/7/77/Artix.png")
                em.set_thumbnail(url = "https://vignette.wikia.nocookie.net/aqwikia/images/e/eb/AQ_new_logo.png")
                em.colour = discord.Colour.red()
                em.set_footer(text = "|Winter-Song|",icon_url = self.bot.user.avatar_url)
                await ctx.send(content = "**UNDER TESTING: (will be developed further)**",embed =em)

        except Exception as e:
            #print(e)
            #await ctx.trigger_typing()
            await ctx.send("```Error: None Found!\nPossible Causes:\n1.You entered the value of badges required but you didn't use quotations.\n2.You entered a two syllable name but you didn't use the quotations.\n3.Player doesn't exist or you don't have any badges yet!.```")

    @commands.command(aliases = ['aqchar', 'aqwcharacter'])
    async def aqwchar(self,ctx, *,args:str = None):
        '''AQW  CHAR PAGE'''
        try:
            if args == None:
                await ctx.send("`Error: No Name Provided!`")
                return
            args = args.lower()
            args = args.replace(' ', '+')
            url = "{}".format(os.environ.get("BADGE_AQW"))
            url = url+args
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'lxml')
            the_script = []
            script = soup.find_all("script")
            await ctx.trigger_typing()
            for x in script:
                the_script.append(x.text)
            made_script_string = '\n'.join(the_script)
            the_magic = re.compile('var flashvars = (.*?);')
            the_flash_vars = the_magic.findall(made_script_string)
            the_flash_vars = str(the_flash_vars)
            clean_var = the_flash_vars[5:len(the_flash_vars)-4]
            #print(clean_var)
            #name
            thonk_name = re.compile('strName=(.*)')
            get_name = thonk_name.findall(clean_var)
            get_name = self.dostuff(get_name)
            #Gender
            thonk_gender = re.compile('strGender=(.*)')
            get_gender = thonk_gender.findall(clean_var)
            get_gender = self.dostuff(get_gender)
            if get_gender == "M":
                get_gender = "Male"
            else:
                get_gender = "Female"
            #LEVEL
            thonk_level = re.compile('intLevel=(.*)')
            get_level = thonk_level.findall(clean_var)
            get_level = self.dostuff(get_level)
            #Class
            thonk_class = re.compile('strClassName=(.*)')
            get_class = thonk_class.findall(clean_var)
            get_class = self.dostuff(get_class)
            #armor
            thonk_ar = re.compile('strArmorName=(.*)')
            get_ar = thonk_ar.findall(clean_var)
            get_ar = self.dostuff(get_ar)
            #Weapon
            thonk_weapon = re.compile('strWeaponName=(.*)')
            get_weapon = thonk_weapon.findall(clean_var)
            get_weapon = self.dostuff(get_weapon)
            #Pet
            thonk_pet = re.compile('strPetName=(.*)')
            get_pet = thonk_pet.findall(clean_var)
            get_pet = self.dostuff(get_pet)
            if not get_pet:
                get_pet = "None"
            badge_info = """__USAGE:__ Use w!aqwbadges "name of the player".\nThe quotations are necessary.\nIf excess of badges, use w!badge "name" "amount" < This will display only the required amount of Badges."""
            em = discord.Embed(title = "{}".format(get_name), url = url)
            em.set_thumbnail(url = "https://www.aq.com/img/network/logo-md-aqw.png")
            em.set_author(name = "AQW Character:", icon_url = "http://aqworldswiki.com/images/aqworldswiki.com/7/77/Artix.png")
            em.colour = discord.Colour.red()
            em.add_field(name = "Name:", value = get_name,inline = False)
            em.add_field(name = "Gender:", value = get_gender,inline = False)
            em.add_field(name = "Level:", value = get_level,inline = False)
            em.add_field(name = "Class Name:", value = get_class,inline = False)
            em.add_field(name = "Armor Name:", value = get_ar,inline = False)
            em.add_field(name = "Weapon Name: ", value = get_weapon,inline = False)
            em.add_field(name = "Pet Name:", value = get_pet,inline = False)
            em.add_field(name = "Badges: ", value = badge_info, inline = False)
            em.set_footer(text = "|Winter-Song|",icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = em)
        except Exception as e:
            #print(e)
            #await ctx.trigger_typing()
            await ctx.send("`Error: None Found!`")

    @commands.command(aliases = ["aqwiki","aqitem"])
    async def aqwitem(self,ctx, *,args:str = None):
        '''AQW item details'''
        try:
            if args == None:
                await ctx.send("`Error; Item name not provided.`")
                return
            new_text = args.replace(' ','-')
            new_text = new_text.lower()
            link = "{}".format(os.environ.get("item_aqw"))
            link = link+new_text
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            things = {}
            things["Text"] = soup.find("div", {"id": "page-content"}).get_text()
            things=dict(map(str.strip,x) for x in things.items())
            new = things["Text"].replace("\n\n\n",'\n')
            #print(new)
            await ctx.trigger_typing()
            try:
                c = soup.find("img", alt=True,src=re.compile(r'\/i.imgur.com\/.+.png'))
                data = c['src']
            except:
                c = soup.find("img", alt=True, src=re.compile(r'\/local--files\/.+.png'))
                data = c['src']
            #print(data)
            try:
                item_embed = discord.Embed(description = new)
                item_embed.set_author(name = "Item Info: |%s|"%(args))
                item_embed.set_image(url = data)
                item_embed.color=discord.Colour.green()
                item_embed.set_footer(text = "|Winter-Song| requested by {}".format(ctx.message.author.name), icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = item_embed)
            except Exception as e:
                item_embed = discord.Embed(description = "-NONE-\n**Possible Causes:**\n1. Name Provided isn't an item: weapon, armor etc but a class.\n2. Item doesn't exist.\n3. Item name is incorrect.\n4. I messed up!")
                item_embed.color=discord.Colour.red()
                await ctx.send(embed = item_embed)
                print(str(e))

        except Exception as e:
        #    pass
            item_embed = discord.Embed(description = "-NONE-\n**Possible Causes:**\n1. Name Provided isn't an item: weapon, armor etc but a class.\n2. Item doesn't exist.\n3. Item name is incorrect.\n4. I messed up!")
            item_embed.color=discord.Colour.red()
            await ctx.send(embed = item_embed)
            #await ctx.send("```-NONE-\n**Possible Causes:**\n1. Name Provided isn't an item: weapon, armor etc but a class.\n2. Item doesn't exist.\n3. Item name is incorrect.\n4. I messed up!```")



def setup(bot):
	bot.add_cog(mmorpg(bot))
