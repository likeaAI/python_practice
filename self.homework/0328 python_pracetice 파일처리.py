# 아이디와 패스워드로 나눠보자.
# 이해가 안가는데 ?



def passwd_to_dict(filename) :
    users = {}
    with open(filename) as passwd :
        for line in passwd :
            if not line.startswith('#' , '\n') :
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

