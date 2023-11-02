T = int(input())

for test_case in range(1, T+1):
    date=input()
    year, month, day=date[:4],date[4:6],date[6:]
    val_date=year+'/'+month+'/'+day
    max_days={'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}

    if month not in max_days:
        print(f'#{test_case} -1')
    elif int(day)>max_days[month]:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {val_date}')
