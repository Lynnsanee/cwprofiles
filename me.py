import re

#matchChecker returns matches made by re.findall on succesful matches
def matchChecker(match, dataType):
    if len(match) > 0:
        if dataType == "string":
            return match[0]
        elif dataType == "int":
            return int(match[0])

#example input message
cwMsg = """🌟Congratulations! New level!🌟
Press /level_up

Battle of the seven castles in 1h 48 minutes!

🐺🦎[FTW]Lynnsane Esquire of Wolfpack Castle
🏅Level: 666
⚔️Atk: 333 🛡Def: 999
🔥Exp: 123/456
❤️Hp: 111/222
💧Mana: 123/911
🔋Stamina: 0/20 ⏰2min
💰1 👝2 💎3

🎽Equipment +10⚔️+20🛡
🎒Bag: 0/15 /inv

State:
🛡Defending 🐺Wolfpack Castle

More: /hero"""

#setting up the data dictionary
data = {}

#filling the data dictionary
data['castle'] = matchChecker(re.findall('[🦅🦈🐉🐺🦌🥔🌑]{1}', cwMsg), 'string')
data['guildEmoji'] = matchChecker(re.findall('(?<=[🦅🦈🐉🐺🦌🥔🌑]{1}).+(?=\[)', cwMsg), 'string')
data['guildTag'] = matchChecker(re.findall('(?<=\[).{2,3}(?=\])', cwMsg), 'string')
data['username'] = matchChecker(re.findall('(?<=[\]|🦅🦈🐉🐺🦌🥔🌑])[a-zA-Z]+(?= Knight| Ranger| Sentinel| Collector| Alchemist| Blacksmith| Esquire| Master of| of )', cwMsg), 'string')
data['class'] = matchChecker(re.findall('Knight|Ranger|Sentinel|Collector|Alchemist|Blacksmith|Esquire|Master{1}', cwMsg), 'string')
data['level'] = matchChecker(re.findall('(?<=🏅Level: )[0-9]{1,2}', cwMsg), 'int')
data['attack'] = matchChecker(re.findall('(?<=Atk: )[0-9]{1,2}', cwMsg), 'int')
data['defense'] = matchChecker(re.findall('(?<=🛡Def: )[0-9]{1,2}', cwMsg), 'int')
data['totalExp'] = matchChecker(re.findall('(?<=🔥Exp: )[0-9]+', cwMsg), 'int')
data['nextExp'] = matchChecker(re.findall('(?<=/)[0-9]+', cwMsg), 'int')
data['hp'] = matchChecker(re.findall('(?<=❤️Hp: )[0-9]+', cwMsg), 'int')
data['maxHp'] = matchChecker(re.findall(f'(?<={data["hp"]}/)[0-9]+', cwMsg), 'int')
data['stamina'] = matchChecker(re.findall('(?<=🔋Stamina: )[0-9]+', cwMsg), 'int')
data['maxStamina'] = matchChecker(re.findall(f'(?<={data["stamina"]}/)[0-9]+', cwMsg), 'int')
data['mana'] = matchChecker(re.findall('(?<=💧Mana: )[0-9]+', cwMsg), 'int')
data['maxMana'] = matchChecker(re.findall(f'(?<={data["mana"]}/)[0-9]+', cwMsg), 'int')
data['bag'] = matchChecker(re.findall('(?<=🎒Bag: )[0-9]+', cwMsg), 'int')
data['maxBag'] = matchChecker(re.findall(f'(?<={data["bag"]}/)[0-9]+', cwMsg), 'int')
data['gold'] = matchChecker(re.findall('(?<=💰)[0-9]+', cwMsg), 'int')
data['pog'] = matchChecker(re.findall('(?<=👝)[0-9]+', cwMsg), 'int')
data['diamond'] = matchChecker(re.findall('(?<=💎)[0-9]+', cwMsg), 'int')
data['isLevelUp'] = ("Press /level_up" in cwMsg)

#output dictionary
print(data)
