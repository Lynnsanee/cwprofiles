import re

#matchChecker returns matches made by re.findall on succesful matches
def matchChecker(match, dataType):
    if len(match) > 0:
        if dataType == "string":
            return match[0]
        elif dataType == "int":
            return int(match[0])

#example input message
cwMsg = """You successfully defeated [27]TheLegend. As he was crawling away, you picked up some of the gold he left behind. Retreating warrior brandished his ⚡️+4 Hunter dagger and swore heavily. 
Received 10 gold and 100 exp."""

#setting up the data dictionary
data = {}

#filling the data dictionary
data['guildtag'] = matchChecker(re.findall('(?<=\[).{2,3}(?=\])', cwMsg), 'string')
data['ingamename'] = matchChecker(re.findall('[a-zA-Z0-9]+(?=. As)', cwMsg), 'string')
data['item'] = matchChecker(re.findall('(?<=brandished his ).+(?= and swore heavily)', cwMsg), 'string')
data['gold'] = matchChecker(re.findall('(?<=Received ).+(?= gold)', cwMsg), 'int')
data['exp'] = matchChecker(re.findall('(?<=and ).+(?= exp)', cwMsg), 'int')

#output dictionary
print(data)