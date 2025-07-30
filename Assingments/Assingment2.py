#Whatsapp Chat Analysis Assignment

# 1.Total chats
def total_chats(msgs):
    return len(msgs)

# 2. Unique user chats
def unique_users(msgs):
    return {m.split(":")[0] for m in msgs}


# 3.Messages count by user
def user_msg_count(msgs,usr):
    return sum(1 for a in msgs if a.startswith(usr+":"))


# 4. active user
def active_user(msgs):
    active_user_count={}
    for m in msgs:
        usr = m.split(":")[0]
        active_user_count[usr]=active_user_count.get(usr,0)+1
    if not active_user_count:
        return None,0
    top_user=max(active_user_count,key=active_user_count.get)
    return top_user,active_user_count[top_user]


# 5. First msg by a user
def first_msgs(msgs,usr):
    user_msgs=[m for m in msgs if m.startswith(usr +":")]
    return (user_msgs[0],user_msgs[-1]) if user_msgs else(None)

# 6. last msg by user
def last_msgs(msgs,usr):
    user_msgs=[m for m in msgs if m.endswith(usr +":")]
    return (user_msgs[0],user_msgs[-1]) if user_msgs else(None)

# 7.Remove duplicate messages
def remove_duplicates(msgs):
    return list(dict.fromkeys(msgs))


#--------------program--------------

n=int(input("Enter number of messages: "))
msgs=[input()for _ in range(n)]

while True:
    print("\noptions:")
    print("1.total chats 2.unique user 3.Messages count 4.active user 5.first msg 6.last msg 7.duplicates")
    ch=int(input("choose: "))

if ch==0:
    print("Exiting..")
    
elif ch==1:
    print("Total chats:", total_chats(msgs))














