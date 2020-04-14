import re

#matchChecker returns matches made by re.findall on succesful matches
def matchChecker(match, dataType):
    if len(match) > 0:
        if dataType == "string":
            return match[0]
        elif dataType == "int":
            return int(match[0])

cwMsg = """👾Encounter:
Forest Wolf lvl.99
2 x Forest Boar lvl.16

🐺🦎[FTW]Lynnsane ⚔️:333 🛡:666 Lvl: 22
Your result on the battlefield:
🔥Exp: 111
💰Gold: 222
❤️Hp: -333

Your attacks: 8/10
Hostile strikes: 1/6
Last hit: 1
Death: 2"""

#setting up the data dictionary
data = {}

#filling the data dictionary
data['castle'] = matchChecker(re.findall('^.{1}', cwMsg), 'string')
data['guildemoji'] = matchChecker(re.findall('(?<=[🦅🦈🐉🐺🦌🥔🌑]{1}).+(?=\[)', cwMsg), 'string')
data['username'] = matchChecker(re.findall('(?<=[\]|🦅🦈🐉🐺🦌🥔🌑])[a-zA-Z]+(?= ⚔️)', cwMsg), 'string')
data['guildtag'] = matchChecker(re.findall('(?<=\[).{2,3}(?=\])', cwMsg), 'string')
data['attack'] = matchChecker(re.findall('(?<=⚔️:)[0-9]{1,4}', cwMsg), 'int')
data['defense'] = matchChecker(re.findall('(?<=🛡:)[0-9]{1,4}', cwMsg), 'int')
data['level'] = matchChecker(re.findall('(?<=Lvl: )[0-9]{1,2}', cwMsg), 'int')
data['exp'] = matchChecker(re.findall('(?<=🔥Exp: )[0-9]{1,2}', cwMsg), 'int')
data['gold'] = matchChecker(re.findall('(?<=💰Gold: )[-0-9]+', cwMsg), 'int')
data['hp'] = matchChecker(re.findall('(?<=❤️Hp: )[-0-9]+', cwMsg), 'int')
data['lasthit'] = matchChecker(re.findall('(?<=Last hit: )[0-9]+', cwMsg), 'int')
data['death'] = matchChecker(re.findall('(?<=Death: )[0-9]+', cwMsg), 'int')

#output dictionary
print(data)


