import amino
chatmenu=[]
chatname={}
client = amino.Client()
em = input('Email: ')
ps = input('Password: ')
client.login(email=em, password=ps)
print("joined")

communities = client.sub_clients()
for name, id in zip(communities.name, communities.comId): print('\n'+name, id)

comId = input('\ncomId: ')

subclient = amino.SubClient(comId=comId, profile=client.profile)

x=0
chats = subclient.get_public_chat_threads(size=100)
for name, id in zip (chats.title, chats.chatId):
         if name!=None:
           print(x+1," : ", name)
           chatname[x]=str(name)
           chatmenu.append(str(id))
           try:
           	 subclient.join_chat(id)
           	 print("joined ", name)
           except:
           	pass
x+=1