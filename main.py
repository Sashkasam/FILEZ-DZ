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


shop_list_by_dishes()
