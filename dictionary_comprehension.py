# print 字典推導式

# dictionary =
# {key: expression for key, value in iterable}

# 運算

# cities_in_f = {'LA': 120, 'Naw Yorks': 65, 'Chiceago': 50, "Miami": 150}
# cities_in_c = {key: (value - 32) * 5/9 for key, value in cities_in_f.items()}
# print(cities_in_f)
# print(cities_in_c)

# e×2 條件判斷

weather = {
    '台北': '大晴天', '台中': '大晴天', '宜蘭': '下雨', "台東": "下雨"
}

sunny_weather = {key: value for key, value in weather.items() if value == '大晴天'}
# print(sunny_weather)

# e×3 條件判斷 + 函式

cities_in_f = {'LA': 120, 'Naw Yorks': 65, 'Chiceago': 50, "Miami": 150}

def check_temp(value): 
    if value >= 70:
        return '熱'
    elif value >= 40:
        return '溫暖'
    else:
        return '冷'

description_cities = { key: check_temp(value) for key, value in cities_in_f.items()}
print(description_cities)