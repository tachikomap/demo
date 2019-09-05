chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input ('输入年份'))
if (chinese_zodiac[year % 12]) == '羊':
print ('羊年运势')