import csv


def date_to_zodiac(date: str):
    chunks = date.strip().split()
    if len(chunks) < 2:
        return None
    if not chunks[0].isdigit():
        return None
    day = int(chunks[0])
    if day < 1 or day > 31:
        return None

    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
              'августа', 'сентября', 'октября', 'ноября', 'декабря']
    # only 12 elements so seems fine to do search twice
    month = months.index(chunks[1]) + 1 if chunks[1] in months else None
    if not month:
        return None

    # every element represents a map with an end date for a particilar month (0 month - january)
    # e.g. aries (Овен) sign is active from 21st of March till 20th of April
    # so, third element would have a map that has record {31: 'Овен'}
    # and forth element would be a map with a record {20: 'Овен'}
    month_to_zodiac = [
        {20: 'Козерог', 31: 'Водолей'},
        {20: 'Водолей', 29: 'Рыбы'},
        {20: 'Рыбы', 31: 'Овен'},
        {20: 'Овен', 30: 'Телец'},
        {20: 'Телец', 31: 'Близнецы'},
        {21: 'Близнецы', 30: 'Рак'},
        {22: 'Рак', 31: 'Лев'},
        {23: 'Лев', 31: 'Дева'},
        {23: 'Дева', 30: 'Весы'},
        {23: 'Весы', 31: 'Скорпион'},
        {22: 'Скорпион', 30: 'Стрелец'},
        {21: 'Стрелец', 31: 'Козерог'},
    ]

    # use the fact that dicts are ordered in python3.7 and higher
    for end_day, sign in month_to_zodiac[month - 1].items():
        if day < end_day:
            return sign
    return None

def normalize_department(department: str):
    department = department.lower()
    if 'ги' in department or 'фипл' in department:
        department = 'ги'
    elif 'фит' in department:
        department = 'фит'
    return department

def convert_to_zodiac(fname: str):
    header_birth = 'Ваша дата рождения (напишите в формате типа "12 февраля")'
    headers_aggression = [
        'Меня злит или раздражает что-то почти каждый день',
        'Мои друзья и знакомые часто страдают от моей вспыльчивости\n.',
        'Когда я разозлюсь, я могу потерять контроль над собой'
    ]
    header_department = 'Ваш факультет (сокращенно, например ФИТ)\nЕсли не учились в НГУ, поставьте прочерк'

    aggresions = []

    with open(fname, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            birth = row[header_birth]
            print(f'Дата рождения: {birth}')
            department = normalize_department(row[header_department])
            print(f'Факультет: {department}')
            zodiac = date_to_zodiac(birth)
            print(f'Знак зодиака: {zodiac}')
            if not zodiac:
                continue
            avg_aggr = sum([int(row[h]) for h in headers_aggression]) / 3
            aggresions.append((zodiac, avg_aggr, department))
    return aggresions


def average_zodiac_aggression(zodiacs: list):
    aggression = {
        'Козерог': [0, 0],
        'Водолей': [0, 0],
        'Рыбы': [0, 0],
        'Овен': [0, 0],
        'Телец': [0, 0],
        'Близнецы': [0, 0],
        'Рак': [0, 0],
        'Лев': [0, 0],
        'Дева': [0, 0],
        'Весы': [0, 0],
        'Скорпион': [0, 0],
        'Стрелец': [0, 0]
    }

    for zodiac, aggr, _ in zodiacs:
        zodiac_aggr = aggression[zodiac]
        zodiac_aggr[0] += aggr
        zodiac_aggr[1] += 1

    # we basically count average but I add a very small number to avoid division by zero
    # (for cases when we don't have data for particilar sign)
    return [(k, round(v[0] / (v[1] + 0.0000001), 2)) for k, v in aggression.items()]

def repr_aggression(avg_aggression):
    zodiacs = ['[']
    levels = ['[']
    for i in range(len(avg_aggression)):
        sign, aggr = avg_aggression[i]
        zodiacs.append(f"'{sign}'")
        levels.append(str(aggr))
        if i != len(avg_aggression) - 1:
            zodiacs.append(', ')
            levels.append(', ')
    zodiacs.append(']')
    levels.append(']')
    return f"zodiac_signs = {''.join(zodiacs)}\nzodiac_agr = {''.join(levels)}"

if __name__ == '__main__':
    zodiacs = convert_to_zodiac('агрессия.csv')
    print('***Общая агрессия***')
    avg_aggression = average_zodiac_aggression(zodiacs)
    print(repr_aggression(avg_aggression))
    print('***Агрессия ГИ***')
    gi_only = [record for record in zodiacs if record[2] == 'ги']
    avg_gi_aggression = average_zodiac_aggression(gi_only)
    print(repr_aggression(avg_gi_aggression))
    print('***Агрессия ФИТ***')
    fit_only = [record for record in zodiacs if record[2] == 'фит']
    avg_fit_aggression = average_zodiac_aggression(fit_only)
    print(repr_aggression(avg_fit_aggression))
