class PhoneBook:

    def __init__(self):
        self.entries =  {"1":["Gordon","Yana","310-985-9661","Aliso Viejo"],
                         "2":["Gordon","Iour","310-593-3117","Aliso Viejo"],
                         "3":["Gordon","Julia","310-985-0521","Aliso Viejo"],
                         "4":["Gordon","Yakov","416-564-2442","Toronto"],
                         "5":["Gordon","Marina","647-278-2442","Toronto"],
                         "6":["Goldentuller","Anna","416-704-2781","Toronto"],
                         "7":["Goldentuller","Edik","416-738-8525","Torotno"],
                         "8":["Faynberg","Alex","705-984-5587","Orillia"],
                         "9":["Faynberg","Elena","705-955-4587","Orillia"]}
        self.next_key = 10

    def list_all_entries(self):
        out_string  = ''
        for key, value in self.entries.items():
            out_string += key + ' ' + ' '.join([str(elem) for elem in value]) + '\n'
        return out_string

    def delete_entry(self, key):
        removed_value = self.entries.pop(key,"No Value Found")
        if removed_value is None :
            return "Not found"
        else:
            return str(removed_value)

    def add_entry(self, entry):
        new_elem = {str(++self.next_key):entry}
        self.entries.update(new_elem)

    def list_sorted_by_last_name(self):
        out_string = ''
        new_list = sorted(self.entries.items(), key = lambda kv:(kv[1][0]))
        for index, tuple in enumerate(new_list):
            out_string += str(tuple[0]) + ' ' + ' '.join([str(elem) for elem in tuple[1]]) + '\n'
        return out_string

    def list_sorted_by_first_name(self):
        out_string = ''
        new_list = sorted(self.entries.items(), key = lambda kv:(kv[1][1]))
        for index, tuple in enumerate(new_list):
            out_string += str(tuple[0]) + ' ' + ' '.join([str(elem) for elem in tuple[1]]) + '\n'
        return out_string

    def list_entries_by_city(self, city):
        out_string = ''
        new_dict = {k:v for k,v in self.entries.items() if v[3] == city}
        for key, value in new_dict.items():
            out_string += key + ' ' + ' '.join([str(elem) for elem in value]) + '\n'
        return out_string

    def list_entries_by_last_name(self, last_name):
        out_string = ''
        new_dict = {k:v for k,v in self.entries.items() if v[0] == last_name}
        for key, value in new_dict.items():
            out_string += key + ' ' + ' '.join([str(elem) for elem in value]) + '\n'
        return out_string

    def list_entries_by_first_name(self, first_name):
        out_string = ''
        new_dict = {k:v for k,v in self.entries.items() if v[1] == first_name}
        for key, value in new_dict.items():
            out_string += key + ' ' + ' '.join([str(elem) for elem in value]) + '\n'
        return out_string
