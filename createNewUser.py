import os

for num in range(7):
    userNum = num + 54
    os.system('mkdir ../userData/user{}'.format(userNum))
    os.system('mkdir ../userData/user{}/beauty'.format(userNum))
    os.system('python3 dataDistribute.py --user user{} --num 70 --cat {}'.format(userNum, 'beauty'))
    os.system('python3 createDb.py --user user{} --cat beauty'.format(userNum))


