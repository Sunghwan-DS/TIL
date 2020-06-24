def solution(records):
    notification = []
    save = []

    for sentence in records:
        name, command = sentence.split()
        if name == 'check':
            save.append(notification.pop())
        elif notification and command == notification[len(notification) - 1][1]:
            notification[len(notification) - 1][0].append(name)
        else:
            notification.append([[name], command])

        # print("알림:", notification)
        # print("보관함:", save)

    answer = []
    for sentence in save:
        # print(sentence)
        name, command = sentence[0], sentence[1]
        if command == 'share':
            if len(set(name)) > 2:
                answer.append("%s and %d others shared your post"%(name[0], len(set(name)) - 1))
            elif len(set(name)) == 2:
                for n in name:
                    if n != name[0]:
                        other_name = n
                        break
                answer.append("%s and %s shared your post"%(name[0], other_name))
            else:
                answer.append("%s shared your post"%(name[0]))

        if command == 'comment':
            if len(set(name)) > 2:
                answer.append("%s and %d others commented on your post"%(name[0], len(set(name)) - 1))
            elif len(set(name)) == 2:
                for n in name:
                    if n != name[0]:
                        other_name = n
                        break
                answer.append("%s and %s commented on your post"%(name[0], other_name))
            else:
                answer.append("%s commented on your post"%(name[0]))
    return answer

print(solution(["john share", "mary comment", "jay share", "check notification", "check notification", "sally comment", "james share", "check notification", "lee share", "laura share", "will share", "check notification", "alice comment", "check notification"]))