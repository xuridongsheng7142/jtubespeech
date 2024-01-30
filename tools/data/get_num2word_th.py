import re
from num2words import num2words

task='th'

month_dict = {'มกราคม':1, 'กุมภาพันธ์':1, 'มีนาคม':1, 'เมษายน':1, 'พฤษภาคม':1, 'มิถุนายน':1, 'กรกฎาคม':1, 'สิงหาคม':1, 'กันยายน':1, 'ตุลาคม':1, 'พฤศจิกายน':1, 'ธันวาคม':1}

int_num_dict = {'0':'๐', '1':'๑', '2':'๒', '3':'๓', '4':'๔', '5':'๕', '6':'๖', '7':'๗', '8':'๘', '9':'๙'}

def convert_number_to_words(sentence):
    patterns = {
        r'\b\d+(?:[,.]\d+)+(?!\w|%)': lambda match: convert_number(match),  # 普通数字和小数
        #r'\d+/\d+/\d+': lambda match: convert_date_to_text(match),  # 日期
        #r'\d+-\d+-\d+': lambda match: ' '.join([convert_number_to_words(digit) for digit in match.group().split('-')]),  # 电话号码
        #r'\d+/\d+': lambda match: convert_number_to_fraction(match),  # 分数
        r'\d+(?:[,.]\d+)?%': lambda match: convert_percent_to_text(match),  # 百分数
        #r'\d+%': lambda match: convert_percent_to_text(match),  # 百分数
        r'\d+:\d+': lambda match: convert_time(match),  # 时间
        r'\d+': lambda match: convert_number(match),  # 普通数字
    }

    # 匹配句子中的数字部分并进行转换
    for pattern, convert_func in patterns.items():
        matches = re.findall(pattern, sentence)
        for match in matches:
            #print(match, pattern)
           # word_before = re.search(r'(\b\w+\b)\s*' + re.escape(match) + r'\b', sentence)
            word_before = re.search(r'(\s|^)(.*)(?=\s' + re.escape(match) + r')', sentence)

            #word_after = re.search(re.escape(match) + r'\b\s*(\b\w+\b)', sentence)
            word_after = re.search(re.escape(match) + r'(\s*|\b)(.*?)(?=\s|$)', sentence)

            fix_words = ' ' + convert_func(match) + ' '
            # 打印数字前后的单词
            if word_before:
                word_before_word = word_before.group(2)
                if word_before_word[-2:] == 'ปี':
                    num_count = ''
                    for i_index in str(match):
                        num_count += int_num_dict[str(i_index)]
                    fix_words = ' ' + num_count  + ' '
                    
                #print("前一个单词:", word_before_word)
                #pass

            if word_after:
                word_after_word = word_after.group(2)
                if word_after_word.isdigit():
                    break
                if word_after_word in month_dict:
                    num_count = ''
                    for i_index in str(match):
                        num_count += int_num_dict[str(i_index)]
                    fix_words = ' ' + num_count  + ' '
                if word_after_word == 'ปี':
                    fix_words = ' ' + convert_func(match) + ' '
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
        return num2words(float(number), lang=task)
    elif ',' in number:
        assert len(number.split(',')[-1]) == 3
        return num2words(int(number.replace(',', '')), lang=task)
    else:
        pattern = r'5{3,}' 
        match_obj = re.search(pattern, str(number))
        if match_obj:
            return number
        if int(number) >= 1000 and int(number) <= 3000: # 年份和数字歧义
            return number
        else:
            return num2words(int(number), lang=task)

def convert_date_to_text(date):
    day, month, year = date.split('/')
    # 将日期转换为越南语文字形式
    day_text = num2words(int(day), lang=task)
    month_text = num2words(int(month), lang=task)
    year_text = num2words(int(year), lang=task)
    
    # 构建越南语文字形式的日期
    date_text = f'วันที่ {day_text} เดือน {month_text} พศ {year_text}'

    return date_text

def convert_number_to_fraction(number):
    numerator, denominator = number.split('/')
    # 将分子和分母转换为越南语文字形式
    numerator_text = num2words(int(numerator), lang=task)
    denominator_text = num2words(int(denominator), lang=task)
    # 构建越南语文字形式的分数
    fraction_text = f'{numerator_text} หาร {denominator_text}'
    return fraction_text

def convert_percent_to_text(percent):
    percent = percent.rstrip('%')
    # 将百分数转换为越南语文字形式
    percent_text = num2words(float(percent), lang=task)
    # 构建越南语文字形式的百分数
    percent_text = f'{percent_text} เปอร์เซ็นต์'
    
    return percent_text

def convert_time(time):
    parts = time.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])

    if len(parts) > 2:
        seconds = int(parts[2])
        hours_word = num2words(hours, lang=task)
        minutes_word = num2words(minutes, lang=task)
        seconds_word = num2words(seconds, lang=task)
        return f'{hours_word} ชั่วโมง {minutes_word} นาที {seconds_word} วินาที'
    else:
        hours_word = num2words(hours, lang=task)
        minutes_word = num2words(minutes, lang=task)
        if minutes == 0:
            return f'{hours_word} ชั่วโมง'
        return f'{hours_word} ชั่วโมง {minutes_word} นาที'

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

