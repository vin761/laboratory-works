import laba_1
import laba_2
import laba_3
import laba_4
import laba_5

print('''
Эта программа позволяет обращаться ко всем лабораторным за семестр!
Для выхода из программы введите слово exit
''')
labs = {"laba_1": ["bubble_sort", "selection_sort", "insertion_sort"],
        "laba_2": ["sort_hoara", "sort_slil", "binar_poisk"],
        "laba_3": ["scobki", "polskay_zapis"],
        "laba_4": ["poisc_v_glub", "dijkstra"],
        "laba_5": ["piramid_sort_1", "piramid_sort_2"]}

x = input("Введите номер лабораторной работы, которую хотите запустить:")
while x != "exit":
    l = "laba_" + x
    print("Лабораторная работа " + x + " имеет следующие команды: " + str(labs[l]))
    komanda = input("Введите выбраную команду:")
    if komanda == "bubble_sort":
        laba_1.bubble_sort()
    elif komanda == "selection_sort":
        laba_1.selection_sort()
    elif komanda == "insertion_sort":
        laba_1.insertion_sort()
    elif komanda == "sort_hoara":
        laba_2.sort_hoara()
    elif komanda == "sort_slil":
        laba_2.sort_slil()
    elif komanda == "binar_poisk":
        laba_2.binar_poisk()
    elif komanda == "scobki":
        laba_3.scobki()
    elif komanda == "polskay_zapis":
        laba_3.polskay_zapis()
    elif komanda == "poisc_v_glub":
        laba_4.poisc_v_glub()
    elif komanda == "poisc_v_glub":
        laba_4.poisc_v_glub()
    elif komanda == "dijkstra":
        laba_4.dijkstra()
    elif komanda == "piramid_sort_1":
        laba_5.piramid_sort_1()
    elif komanda == "piramid_sort_2":
        laba_5.piramid_sort_2()
    x = input("Введите номер лабораторной работы, которую хотите запустить:")
