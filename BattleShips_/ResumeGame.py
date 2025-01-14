
def save(board,name):
	strData = []
	for i in board:
		row = []
		for j in i:
			row.append(str(j))
		strData.append(row)
			
	data = ''
	for x in range(len(strData)):
		data = data + ",".join(strData[x]) + "\n"

	with open(f'{name}.csv','w') as f:
		f.write(data)
		f.close()

def format(list):
    for i in list:
        if i[0] == '':
            i[0]=' '+i[0]
        if i[-1] == '':
            i[-1] = i[-1]+' '
    return list
def openSave(name):
    with open(f'{name}.csv' ,'r') as f:
        
        #print(data)
        list = []
        for i in f:
            i = i.strip()
            i = i.split(',')
            list.append(i)
        list = format(list)

        return list


import json
def SaveTurn(PlayerShipsDestroyed,ComputerShipsDestroyed):
	f = open('Turn.json','r+')
	data = json.load(f)
	#print(data["Turn"][0]['who'])
	data["Turn"][0]['who'] = 'player'
	data["Turn"][1]['playerShipsDestroyed'] = PlayerShipsDestroyed
	data["Turn"][2]['computerShipsDestroyed'] = ComputerShipsDestroyed
	f.seek(0)
	json.dump(data, f)
	f.truncate()
def TurnData():
	f = open('Turn.json','r+')
	data = json.load(f)
	#print(data["Turn"][0]['who'])
	return [  data["Turn"][0]['who'], data["Turn"][1]['playerShipsDestroyed'] , data["Turn"][2]['computerShipsDestroyed'] ] 
