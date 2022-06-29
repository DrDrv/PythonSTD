def presentations(data: list):
    """data presentations"""
    from func import log
    if not data:
        print("\033[31m У вас пока нет ни каких дел!")
        print(f"\033[0m {'+'*100}")
    else:
        i = 0
        for item in data:
            index = data.index(item)
            data[index] = str(item)[2:-2]
            row = data[index].split(';')
            print(f"\033[32m {i} {row[0]} | {row[1]} ")
            i += 1
        print(f"\033[0m {'='*75}")
        log(f' Просмотр задач ')
    return list(data)