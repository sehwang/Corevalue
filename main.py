import operator

def make_db():

    source = []
    f = open("Coval.txt", 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split(", ")
        source.append(words)
    f.close()

    DB = []
    c_name = 1
    for row in source:
        if c_name == 1:
            c_name = 0
            continue
        i = 0
        co_val = []
        corp = []
        for word in row:
            if i == 0:
                name = word
            if i == 2:
                cnt = word
            elif i >= 3:
                if word[-1] != '\n':
                    co_val.append(word)
                else:
                    co_val.append(word[:-1])
            i += 1
        if cnt == len(co_val):
            print("you put wrong number of cores")
        corp.append(name)
        corp.append(cnt)
        corp.append(co_val)
        DB.append(corp)
    return DB

def disp_DB(DB):
    for corp in DB:
        print("Name: " + corp[0], end=" ")
        print("\tCnt: " + corp[1])
        for core in corp[2]:
            print(core, end=", ")
        print()

def core_word_dic(DB):
    core_dic = {}
    ex = 0
    exclude_word = ["and", "the", "to", "on", "for"]
    for corp in DB:
        for core in corp[2]:
            words = core.split()
            for word in words:
                data_dic = {'Fre': 0, 'Point': 0}
                if word in exclude_word:
                    ex += 1
                if word not in exclude_word:
                    if word not in core_dic.keys():
                        data_dic['Fre'] = 1
                        data_dic['Point'] = 1 / (int(corp[1]) * len(words) + ex)
                        core_dic[word] = data_dic
                    else:
                        core_dic[word]['Fre'] += 1
                        core_dic[word]['Point'] += 1 / int(corp[1])
    return core_dic

def report1(dict):

    file = open("first_A.txt", 'w')
    for key, val in dict.items():
        name = "%s:  " % key
        fre = "%d   " % val["Fre"]
        pnt = "%.3f\n" % val["Point"]

        file.write(name)
        file.write(fre)
        file.write(pnt)
    file.close()

def report2


DB = make_db()
disp_DB(DB)
core_words = core_word_dic(DB)
report1(core_words)
print(core_words)



print("\ndone")
