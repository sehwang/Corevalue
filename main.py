def make_db():

    source = []
    f = open("cor.csv", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        words = line.split(",")
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
                if word != '':
                    if word != "\n":
                        if word[-1] == '\n':
                            co_val.append(word[:-1])
                        else:
                            co_val.append(word)
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
    exclude_word = ["striving", "strive", "cultivating", "operation", "solution", "way", "priority",
                    "move", "take", "value", "centered", "behavior", "emphasis", "continuous", "focus",
                    "spirit", "we", "all", "other", "each", "is", "are", "have", "what", "in", "who",
                    "with","of", "our", "and", "work", "view", "take", "pursue", "free", "centric",
                    "daily", "thing", "always", "activities", "supply", "chain",
                    "the", "to", "on", "for", "&", "do", "it", "a", "as", "about", "through", "one"]
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
                        if (len(words) - ex) <= 0:
                            t = len(words)
                        else:
                            t = (len(words) - ex)
                        data_dic['Point'] = 1 / (int(corp[1]) * t)
                        core_dic[word] = data_dic
                    else:
                        core_dic[word]['Fre'] += 1
                        core_dic[word]['Point'] += 1 / int(corp[1])
    return core_dic

def report1(dict):

    file = open("first_A.txt", 'w', encoding='UTF8')
    for key, val in dict.items():
        name = "%s:  " % key
        fre = "%d   " % val["Fre"]
        pnt = "%.3f\n" % val["Point"]

        file.write(name)
        file.write(fre)
        file.write(pnt)
    file.close()

def report_csv(dict):

    file = open("report.csv", 'w', encoding='UTF8')
    file.write("Name,")
    file.write("Frequency,")
    file.write("Power\n")
    for key, val in dict.items():
        name = "%s," % key
        fre = "%d," % val["Fre"]
        pnt = "%.3f\n" % val["Point"]

        file.write(name)
        file.write(fre)
        file.write(pnt)
    file.close()

DB = make_db()
disp_DB(DB)
core_words = core_word_dic(DB)
report1(core_words)
report_csv(core_words)
print(core_words)

print("\ndone")