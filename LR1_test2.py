# TODO Найдите количество книг, которое можно разместить на дискете

disk_mb = 1.44 # Мб
pages = 100
strok_page = 50
sim_strok = 25
one_sim_b = 4 # Байт

disk_b = disk_mb * 1024 * 1024 # Перевели Мб в байты

book_b = sim_strok * strok_page * pages * one_sim_b # Размер книги в байтах

books = disk_b // book_b

print("Количество книг, помещающихся на дискету:", int(books))
