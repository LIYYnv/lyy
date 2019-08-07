import yaml


def data(file_name, data_file):
    with open("./data/" + file_name, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        dict_data = data[data_file]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
        return list_data

def data_txt(file_name, data_file):
    with open("../data/" + file_name, "r", encoding="utf-8") as f:
        data = f.read()
        data_list = data.split("\n")
        result_list = []
        for i in data_list:
            result_list.append(tuple(i.split(",")))
        print(result_list)

if __name__ == '__main__':
    data_txt("contacts_data.txt", 123)