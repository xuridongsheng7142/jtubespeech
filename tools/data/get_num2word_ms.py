import re
from num2words import num2words

lang = 'id'

month_dict = {'januari':1, 'februari':1, 'mac':1, 'april':1, 'mei':1, 'jun':1, 'julai':1, 'ogos':1, 'september':1, 'oktober':1, 'november':1, 'disember':1}

def convert_number_to_words(sentence):
    patterns = {
        r'\b\d+(?:[,.]\d+)+(?!\w|%)': lambda match: convert_number(match),  # 普通数字和小数
        #r'\d+/\d+/\d+': lambda match: convert_date_to_text(match),  # 日期
        #r'\d+-\d+-\d+': lambda match: ' '.join([convert_number_to_words(digit) for digit in match.group().split('-')]),  # 电话号码
        #r'\d+/\d+': lambda match: convert_number_to_fraction(match),  # 分数
        r'\d+(?:[,.]\d+)?%': lambda match: convert_percent_to_text(match),  # 百分数
        #r'\d+%': lambda match: convert_percent_to_text(match),  # 百分数
        #r'\d+:\d+': lambda match: convert_time(match),  # 时间
        r'\d+': lambda match: convert_number(match),  # 普通数字
    }

    # 匹配句子中的数字部分并进行转换
    for pattern, convert_func in patterns.items():
        matches = re.findall(pattern, sentence)
        for match in matches:
            #print(match, pattern)
            word_before = re.search(r'(\b\w+\b)\s*' + re.escape(match) + r'\b', sentence)
            word_after = re.search(re.escape(match) + r'\b\s*(\b\w+\b)', sentence)

            fix_words = ' ' + convert_func(match) + ' '

            if str(match).startswith('0') and '.' not in str(match):
                fix_list = []
                for each_num in str(match):
                    fix_list.append(num2words(int(each_num), lang=lang))
                fix_words = ' ' + ' '.join(fix_list) + ' '
            if '0' in str(match) and 'nol' in fix_words:
                fix_words = fix_words.replace('nol', 'kosong')
            if '8' in str(match) and 'delapan' in fix_words:
                fix_words = fix_words.replace('delapan', 'lapan')
            # 打印数字前后的单词
            if word_before:
                word_before_word = word_before.group(1)
                #print("前一个单词:", word_before_word)
                pass

            if word_after:
                word_after_word = word_after.group(1)
                if word_after_word.isdigit():
                    break
                if word_after_word in month_dict:
                    fix_words += 'haribulan '
                #print("后一个单词:", word_after.group(1))
            match = '(^| )' + match + '( |$)'
            sentence = re.sub(match, fix_words, sentence, count=1)
            sentence = re.sub(' +', ' ', sentence.strip())

            #sentence = sentence.replace(match, convert_func(match))

    return sentence

def convert_number(number):
    if '.' in number:
        parts = number.split('.')
        assert len(parts) == 2
        return num2words(float(number.replace(',', '')), lang=lang)
    elif ',' in number:
        assert len(number.split(',')[-1]) == 3
        return num2words(int(number.replace(',', '')), lang=lang)
    else:
        #if int(number) >= 1500 and int(number) <= 2099: # 年份和数字歧义
        #    return number
        #else:
            return num2words(int(number), lang=lang)

def convert_date_to_text(date):
    #TODO
    day, month, year = date.split('/')
    # 将日期转换为越南语文字形式
    day_text = num2words(int(day), lang=lang)
    month_text = num2words(int(month), lang=lang, to='ordinal')
    year_text = num2words(int(year), lang=lang)
    
    # 构建越南语文字形式的日期
    date_text = f'{day_text} {month_text} {year_text}'

    return date_text

def convert_number_to_fraction(number):
    numerator, denominator = number.split('/')
    # 将分子和分母转换为越南语文字形式
    numerator_text = num2words(int(numerator), lang=lang)
    denominator_text = num2words(int(denominator), lang=lang)
    # 构建越南语文字形式的分数
    fraction_text = f'{numerator_text} per {denominator_text}'
    return fraction_text

def convert_percent_to_text(percent):
    percent = percent.rstrip('%')
    # 将百分数转换为越南语文字形式
    if '.' in percent:
        percent_text = num2words(float(percent), lang=lang)
    else:
        percent_text = num2words(int(percent), lang=lang)
    # 构建越南语文字形式的百分数
    percent_text = f'{percent_text} persen'
    
    return percent_text

def convert_time(time):
    parts = time.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])

    if len(parts) > 2:
        seconds = int(parts[2])
        hours_word = num2words(hours, lang=lang)
        minutes_word = num2words(minutes, lang=lang)
        seconds_word = num2words(seconds, lang=lang)
        return f'{hours_word} jam {minutes_word} menit {seconds_word} saat'
    else:
        hours_word = num2words(hours, lang=lang)
        minutes_word = num2words(minutes, lang=lang)
        return f'{hours_word} jam {minutes_word} menit'

if __name__ == '__main__':
    import sys, os
    text, text_fix = sys.argv[1:3]

    count = ''
    with open(text, 'r') as f:
        for line in f:
            utt, ref = line.strip().split(' ', 1)
            ref = ref.lower()
            try:
                ref_fix = convert_number_to_words(ref)
                count += utt + ' ' + ref_fix + '\n'
                #print(utt, ref_fix)
            except: 
                print('bad line', line.strip())
    with open(text_fix, 'w') as f:
        f.write(count)

#sentence = '23/12/2020'
#words = convert_number_to_words(sentence)
#print(words)

