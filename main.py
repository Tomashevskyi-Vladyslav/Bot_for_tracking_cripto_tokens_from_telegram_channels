from telethon import TelegramClient, events
from requests.exceptions import RequestException
import time
import re
import ast

api_id =  # Personal information from telegram api
api_hash = ' ' # Personal information from telegram api

client = TelegramClient('anon', api_id, api_hash) # Passing all necessary values ​​to the session client
client.start()

trackingList = list()
take_from_only = list()
ParsTocen = []
ParsTocen1 = []
counter = -1
counter2 = -1

#Block for accessing the database----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open("DB.txt", "r") as file1:
    take_info_from_doc = file1.read()

try:# Converting a string to a dictionary
    trackingList = ast.literal_eval(take_info_from_doc)
    take_info_from_doc = None
    
except Exception as err:
    print(f"Error while processing data: {err}")

with open("take_token_from_only.txt", "r") as file1:
    take_info_from_doc_only = file1.read()

try:# Converting a string to a dictionary
    take_from_only = ast.literal_eval(take_info_from_doc_only)
    take_info_from_doc_only = None
    
except Exception as err:
    print(f"Error while processing data: {err}")
#End block for accessing the database----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.on(events.NewMessage('OttoBASEDeployments'))
async def shipment_1 (event) -> None:
    global trackingList

    try :
        token_pattern = r"\(([^\)]+)\)"
        match = re.search(token_pattern, event.message.message)

        if match:
            token_name = match.group(1)
            print(f"{token_name.lower()} OttoBASEDeployments")

            if str(token_name.lower()) in trackingList and take_from_only[trackingList.index(token_name.lower())] == 0:
                await client.send_message('hdidkwnqbqfzyskn2816', f"""‼️OttoBASEDeployments‼️\n\n{event.text}""")

    except Exception as err:
        await client.send_message('hdidkwnqbqfzyskn2816', "❌Some exception OttoBASEDeployments❌")

@client.on(events.NewMessage('bananadeployerBASE'))
async def shipment_2 (event) -> None:
    global trackingList

    try :
        token_pattern = r"\(\$([^\)]+)\)"
        match = re.search(token_pattern, event.message.message)

        if match:
            token_name = match.group(1)
            print(f"{token_name.lower()} bananadeployerBASE")

            if str(token_name.lower()) in trackingList and take_from_only[trackingList.index(token_name.lower())] == 0:
                await client.send_message('hdidkwnqbqfzyskn2816', f"""‼️bananadeployerBASE‼️\n\n{event.text}""")

    except Exception as err:
        await client.send_message('hdidkwnqbqfzyskn2816', "❌Some exception bananadeployerBASE❌")

@client.on(events.NewMessage('virtuals_deploy'))
async def shipment_3 (event) -> None:
    global trackingList

    try :
        token_pattern = r"\\\(\$([^\)]+)\\\)"
        match = re.search(token_pattern, event.message.message)

        if match:
            token_name = match.group(1)
            print(f"{token_name.lower()} virtuals_deploy")

            if str(token_name.lower()) in trackingList and take_from_only[trackingList.index(token_name.lower())] == 1:
                await client.send_message('hdidkwnqbqfzyskn2816', f"""‼️virtuals_deploy‼️\n\n{event.text}""")
    except Exception as err:
        await client.send_message('hdidkwnqbqfzyskn2816', "❌Some exception virtuals_deploy❌")


@client.on(events.NewMessage('bananadeployerSOL'))
async def shipment_4 (event) -> None:
    global trackingList

    try :
        token_pattern = r"\(\$([^\)]+)\)"
        match = re.search(token_pattern, event.message.message)

        if match:
            token_name = match.group(1)
            print(f"{token_name.lower()} bananadeployerSOL")

            if str(token_name.lower()) in trackingList and take_from_only[trackingList.index(token_name.lower())] == 2:
                await client.send_message('hdidkwnqbqfzyskn2816', f"""‼️bananadeployerSOL‼️\n\n{event.text}""")

    except Exception as err:
        await client.send_message('hdidkwnqbqfzyskn2816', "❌Some exception bananadeployerSOL❌")


@client.on(events.NewMessage('hdidkwnqbqfzyskn2816'))
async def main(event) -> None: 

    if event.message.message[0] == "A" and event.message.message[1] == "d" and event.message.message[2] == "d" or event.message.message[0] == "a" and event.message.message[1] == "d" and event.message.message[2] == "d":
        
        counter = -1
        List = []

        for i in event.message.message:

            if i == "$":
                counter = 0

            elif counter == 0:
                List.append(i.lower())

        List = "".join(List)
        
        if not List in trackingList and len(List) != 0:

            trackingList.append(List)
            take_from_only.append(0)

            with open("DB.txt", "w") as file:
                file.write(f"{trackingList}")

            with open("take_token_from_only.txt", "w") as file:
                file.write(f"{take_from_only}")
                
            await client.send_message('hdidkwnqbqfzyskn2816', f"✅ Everything was added correctly, A token has been added: {List} ✅\n\n‼️Get information exclusively from: bananadeployerBASE and from OttoBASEDeployments‼️")
            await client.send_message('hdidkwnqbqfzyskn2816', f"{trackingList}")

        elif List in trackingList:
            await client.send_message('hdidkwnqbqfzyskn2816', f"❌ Something went wrong, make sure that this token is not in the list and try again ❌")


    if event.message.message[0] == "V" and event.message.message[1] == "d" and event.message.message[2] == " " and event.message.message[3] == "a" and event.message.message[4] == "d" and event.message.message[5] == "d" or event.message.message[0] == "v" and event.message.message[1] == "d" and event.message.message[2] == " " and event.message.message[3] == "a" and event.message.message[4] == "d" and event.message.message[5] == "d":
        
        counter = -1
        List = []

        for i in event.message.message:

            if i == "$":
                counter = 0

            elif counter == 0:
                List.append(i.lower())

        List = "".join(List)
        
        if not List in trackingList and len(List) != 0:

            trackingList.append(List)
            take_from_only.append(1)

            with open("DB.txt", "w") as file:
                file.write(f"{trackingList}")

            with open("take_token_from_only.txt", "w") as file:
                file.write(f"{take_from_only}")
                
            await client.send_message('hdidkwnqbqfzyskn2816', f"✅ Everything was added correctly, A token has been added: {List} ✅\n\n‼️Get information exclusively from: virtuals_deploy‼️")
            await client.send_message('hdidkwnqbqfzyskn2816', f"{trackingList}")

        elif List in trackingList:
            await client.send_message('hdidkwnqbqfzyskn2816', f"❌ Something went wrong, make sure that this token is not in the list and try again ❌")


    if event.message.message[0] == "B" and event.message.message[1] == "d" and event.message.message[2] == "s" and event.message.message[3] == " " and event.message.message[4] == "a" and event.message.message[5] == "d" and event.message.message[6] == "d" or event.message.message[0] == "b" and event.message.message[1] == "d" and event.message.message[2] == "s" and event.message.message[3] == " " and event.message.message[4] == "a" and event.message.message[5] == "d" and event.message.message[6] == "d":
        
        counter = -1
        List = []

        for i in event.message.message:

            if i == "$":
                counter = 0

            elif counter == 0:
                List.append(i.lower())

        List = "".join(List)
        
        if not List in trackingList and len(List) != 0:

            trackingList.append(List)
            take_from_only.append(2)

            with open("DB.txt", "w") as file:
                file.write(f"{trackingList}")

            with open("take_token_from_only.txt", "w") as file:
                file.write(f"{take_from_only}")

            await client.send_message('hdidkwnqbqfzyskn2816', f"✅ Everything was added correctly, A token has been added: {List} ✅\n\n‼️Get information exclusively from: bananadeployerSOL‼️")
            await client.send_message('hdidkwnqbqfzyskn2816', f"{trackingList}")

        elif List in trackingList:
            await client.send_message('hdidkwnqbqfzyskn2816', f"❌ Something went wrong, make sure that this token is not in the list and try again ❌")


    if event.message.message[0] == "D" and event.message.message[1] == "e" and event.message.message[2] == "l" and event.message.message[3] == "l" or event.message.message[0] == "d" and event.message.message[1] == "e" and event.message.message[2] == "l" and event.message.message[3] == "l":
        
        counter = -1
        List = []

        for i in event.message.message:
            
            if i == "$":
                counter = 0

            elif counter == 0:
                List.append(i.lower())

        List = "".join(List)
        
        if List in trackingList and len(List) != 0:

            take_from_only.pop(trackingList.index(List))
            trackingList.remove(List)


            with open("DB.txt", "w") as file:
                file.write(f"{trackingList}")

            with open("take_token_from_only.txt", "w") as file:
                file.write(f"{take_from_only}")


            await client.send_message('hdidkwnqbqfzyskn2816', f"✅ Everything was deleted correctly, A token has been deleted: {List} ✅")
            await client.send_message('hdidkwnqbqfzyskn2816', f"{trackingList}")

        elif not List in trackingList:
            await client.send_message('hdidkwnqbqfzyskn2816', "❌ Something went wrong, make sure this token is included in the list and try again ❌")


    if event.message.message == "Help" or event.message.message == "help" or event.message.message == "/help" or event.message.message == "/Help":
        await client.send_message('hdidkwnqbqfzyskn2816', f"""**Commands supported by the Bot**\n\n**'/add'** - Adding token tracking in the OttoBASEDeployments and bananadeployerBASE channel\n\n**'/vd add'** - Adding token tracking in the virtuals_deploy channel\n\n**'/bds add'** - Adding token tracking in the bananadeployerSOL channel\n\n**'/dell'** - Remove token from tracker\n\n**'/show'** - Show all tokens that are in the track""")

    if event.message.message == "Show" or event.message.message == "show" or event.message.message == "/show" or event.message.message == "/Show":
        
        string = ""

        for i in range(len(trackingList)):

            if take_from_only[i] == 0:
                string += f"{trackingList[i]} - ‼️Forwarding from OttoBASEDeployments and bananadeployerBASE‼️\n\n"

            if take_from_only[i] == 1:
                string += f"{trackingList[i]} - ‼️Forwarding from virtuals_deploy‼️\n\n"

            if take_from_only[i] == 2:
                string += f"{trackingList[i]} - ‼️Forwarding from bananadeployerSOL‼️\n\n"

        await client.send_message('hdidkwnqbqfzyskn2816', f"""{string}""")

    if event.message.message == "/add" or event.message.message == "/Add":
        await client.send_message('hdidkwnqbqfzyskn2816', f"""📌The 'add' command is necessary to add token tracking from the OttoBASEDeployments and bananadeployerBASE channels\n\n➡️The command is written like this: <add $token_name>""")

    if event.message.message == "/Vd add" or event.message.message == "/vd add":
        await client.send_message('hdidkwnqbqfzyskn2816', f"""📌The 'vd add' command is necessary to add token tracking from the virtuals_deploy channel\n\n➡️The command is written like this: <vd add $token_name>""")

    if event.message.message == "/bds add" or event.message.message == "/Bds add":
        await client.send_message('hdidkwnqbqfzyskn2816', f"""📌The 'bds add' command is necessary to add token tracking from the bananadeployerSOL channel\n\n➡️The command is written like this: <bds add $token_name>""")

    if event.message.message == "/dell" or event.message.message == "/Dell":
        await client.send_message('hdidkwnqbqfzyskn2816', f"""📌The dell command is necessary to remove the token tracking from the tracking sheet\n\n➡️It is written like this: <dell $token_name>""")

while True:
    try:
        client.run_until_disconnected() 
    except Exception as err:
        print(err)
        print('* Connection failed, waiting to reconnect...')
        time.sleep(15)
        print('* Reconnecting.') 
