class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bio = ''
        self.newsfeed = []
        self.friendlist = []
        self.status = []
        self.chat = []
        self.groups = []
    
    def update_bio(self,profileinfo):
        self.bio = profileinfo
        print('Bio updated')
    
    def update_status(self,status):
        self.status.append({'status':status,'likes':0,'comments':[]})
    
    def update_comment(self,friend,status_index,comment):
        if 0<= status_index < len(friend.status):
            friend.status[status_index]['comments'].append(comment)
            print('commented successfully')
        else:
            print('Choose available index')

    
    def add_friend(self,friend_username):
        self.friendlist.append(friend_username)
    
    def show_newsfeed(self):
        if self.friendlist:
            for friend in self.friendlist:
                if friend.status:
                    for ind,status in enumerate(friend.status):
                        print(f"{friend.username}'s status{ind}: {status['status']} Likes:{status['likes']} ")
                else:
                    print('Its empty. \nNoone from your friendlist posted a status')
        else:
            print('Newsfeed is empty. You have no friends')

    def send_messege(self,receiver,messege):
        receiver.chat.append({'From':self.username,'messege':messege})
        print('Messege sent')
    
    def join_group(self,groupname):
        self.groups.append(groupname)

class SocialNetwork:
    def __init__(self):
        self.user = {}
        self.groups = {}

    def register_user(self,username,password):
        if username in self.user:
            print('User name already exists')
            return
        self.user[username] = User(username,password)
        print(f'User {username} registered successfully')
        return
    
    def authenticate_user(self,username,password):
        if username in self.user:
            if self.user[username].username == username and self.user[username].password == password:
                print('Authenticated successfully')
                return self.user[username]
            else:
                print('Invalid username or password')
        else:
            print(f'username {username} not found')

def main():
    network = SocialNetwork()

    while True:
        print('\n1.Register')
        print('2.Login')
        print('3.Exit')

        choice = input('Select Option(1,2,3): ')
        
        if choice == '1':
            username = input('Enter username: ')
            password = input('Enter password: ')

            network.register_user(username,password)
        
        elif choice == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')

            user = network.authenticate_user(username,password)

            if user:
                while True:
                    print('\n1.Update Bio')
                    print('2.Send Messege')
                    print('3.Go to Newsfeed')
                    print('4.Comment on friends status')
                    print('5.Go to Chats')
                    print('6.Post Status')
                    print('7.Add Friend')
                    print('8.See Friend list')
                    print('9.Logout')

                    userchoice = input('Select Option (1,2,3,4,5,6,7,8,9): ')

                    if userchoice == '1':
                        newbio = input('Enter new Bio: ')
                        user.update_bio(newbio)
                    
                    elif userchoice == '2':
                        receiver = input('enter receiver username: ')
                        if receiver in network.user:
                            if network.user[receiver] in user.friendlist:
                                messege = input('enter your messege: ')
                                user.send_messege(network.user[receiver],messege)
                            else:
                                print(f'You are not friend with {receiver}')
                        else:
                            print('Username does not exists')
                    
                    elif userchoice == '3':
                        user.show_newsfeed()
                    
                    elif userchoice == '4':
                        friend_username = input('Enter friend username: ')
                        
                        if friend_username in network.user:
                            friend = network.user[friend_username]
                            if network.user[friend_username] in user.friendlist:
                                if friend.status:
                                    for ind,status in enumerate(friend.status):
                                        print(f"status_index: {ind} {status['status']} Likes:{status['likes']}")
                                    status_index = int(input('Enter Status index: '))
                                    comment = input("Add comment")
                                    user.update_comment(friend,status_index,comment)
                                else:
                                    print(f'{friend_username} did not post staus yet')
                            else:
                                print(f'You are not friend with {friend_username}')
                        else:
                            print('username does not exist')
                    elif userchoice == '5':
                        if user.chat:
                            for chat in user.chat:
                                print(chat)
                        else:
                            print('Inbox is empty')
                    
                    elif userchoice == '6':
                        status = input('Enter Status: ')
                        user.update_status(status)
                    
                    elif userchoice == '7':
                        friend_id = input("Enter Friend's username: ")
                        if friend_id in network.user:
                            if network.user[friend_id] in user.friendlist:
                                print(f"You are already friend with {network.user[friend_id].username}")
                            else:
                                user.friendlist.append(network.user[friend_id])
                                print(f"{network.user[friend_id].username} added as a friend")
                        else:
                            print(f"User name {friend_id} doesn't exists")
                    
                    elif userchoice == '8':
                        if user.friendlist:
                            for ind,friend in enumerate(user.friendlist):
                                print(f'{ind+1}.{friend.username}',end=' ')
                            print('\n')
                        else:
                            print('You have no friends')

                    elif userchoice =='9':
                        break

                    else:
                        print('Choose valid option')
                
        elif choice == '3':
            break
        
        else:
            print('Choose a valid option')

if __name__ == '__main__':
    main()

    
    