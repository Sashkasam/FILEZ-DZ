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
        
    print(cook_book)
    