# Задание № 1 Должен получить словарь книга рецептов


cook_book = {}
with open('book_of_recipes.txt', encoding='utf8') as reciepes:
    for line in reciepes:
        dishes_name = line.strip()
        quanity_count = reciepes.readline()
        dishes = []
        for i in range(int(quanity_count)):
            ingrid = reciepes.readline()
            ingridient, quanity, measure = ingrid.split(' | ')
            all_ingridients = {"ingridient_name": ingridient, "quanity" : quanity, "measure" : measure.strip()}
            dishes.append(all_ingridients)
            cook_book[dishes_name] = dishes
        reciepes.readline()
        
    # print(cook_book)
    
  # Задание № 2   написать функцию, которая на вход принимает список блюд из cook_book 
  # и количество персон для кого мы будем готовить

def shop_list_by_dishes():
    shop_list_dishes = {}
    print("Я помогу посчитать сколько нужно купить продуктов:)")
    dishes = input("Введите название блюда(блюд) через запятую: ").split(', ')
    person_count =  int(input("Введите количество человек: "))
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_dict = dict(ingridient)
            new_dict.pop('ingridient_name')
            new_dict['quanity'] = int(new_dict['quanity']) * person_count
            shop_list_dishes = {ingridient['ingridient_name'] : new_dict}
            print(shop_list_dishes)


# shop_list_by_dishes()


#Задание № 3 
with open('1.txt', encoding='utf8') as text1:
    text1_read = text1.read() 
    text1_name = '1.txt' 
    text1.seek(0)
    text1_full = text1.readlines()
    text1_len = str(len(text1_full))

with open('2.txt', encoding='utf8') as text2:
    text2_read = text2.read()
    text2_name = '2.txt'
    text2.seek(0)
    text2_full = text2.readlines()
    text2_len = str(len(text2_full))
    


with open('3.txt', encoding='utf8') as text3:
    text3_read = text3.read()
    text3_name = '3.txt'
    text3.seek(0)
    text3_full = text3.readlines()
    text3_len = str(len(text3_full))
   
   
with open('result.txt','w', encoding='utf8') as result_text:
    if min(text1_len,text2_len,text3_len) == text1_len:
        result_text.write(text1_name + '\n'  + text1_len + '\n')
        result_text.write(text1_read + '\n')
        if min(text2_len,text3_len) == text2_len:
            result_text.write(text2_name + '\n'  + text2_len + '\n')
            result_text.write(text2_read + '\n')
            result_text.write(text3_name + '\n'  + text3_len + '\n')
            result_text.write(text3_read + '\n')
        else:
            result_text.write(text3_name + '\n'  + text3_len + '\n')
            result_text.write(text3_read + '\n')
            result_text.write(text2_name + '\n'  + text2_len + '\n')
            result_text.write(text2_read + '\n')
    elif  min(text1_len,text2_len,text3_len) == text2_len: 
        result_text.write(text2_name + '\n'  + text2_len + '\n')
        result_text.write(text2_read + '\n')
        if min(text1_len,text3_len) == text1_len:
            result_text.write(text1_name + '\n'  + text1_len + '\n')
            result_text.write(text1_read + '\n')
            result_text.write(text3_name + '\n'  + text3_len + '\n')
            result_text.write(text3_read + '\n')
        else:
            result_text.write(text3_name + '\n'  + text3_len + '\n')
            result_text.write(text3_read + '\n')
            result_text.write(text1_name + '\n'  + text1_len + '\n')
            result_text.write(text1_read + '\n')
    else:
        result_text.write(text3_name + '\n'  + text3_len + '\n')
        result_text.write(text3_read + '\n')
        if min(text1_len,text2_len) == text1_len:
            result_text.write(text1_name + '\n'  + text1_len + '\n')
            result_text.write(text1_read + '\n')
            result_text.write(text2_name + '\n'  + text2_len + '\n')
            result_text.write(text2_read + '\n')
        else:
            result_text.write(text2_name + '\n'  + text2_len + '\n')
            result_text.write(text2_read + '\n')
            result_text.write(text1_name + '\n'  + text1_len + '\n')
            result_text.write(text1_read + '\n')
       