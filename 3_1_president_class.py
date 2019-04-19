class President():

    def __init__(self, index):
        self.get_data(index)

    def get_data(self, index):
        
        # Reads data into class.
        filename = "presidents.txt"
        with open(filename,'r') as file:
            for each_line in file:
                each_line_split = each_line.replace('\n','').split(':')

                # Selects data with correct index number.
                if each_line_split[0] == str(index):
                    self.__number = each_line_split[0]
                    self.__last_name = each_line_split[1]
                    self.__first_name = each_line_split[2]
                    self.__birth_date = each_line_split[3]
                    self.__death_date = each_line_split[4]
                    self.__birth_place = each_line_split[5]
                    self.__birth_state = each_line_split[6]
                    self.__term_start_date = each_line_split[7]
                    self.__term_end_date = each_line_split[8]
                    self.__party = each_line_split[9]

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def death_date(self):
        return self.__death_date

    @property
    def birth_place(self):
        return self.__birth_place

    @property
    def birth_state(self):
        return self.__birth_state

    @property
    def term_start_date(self):
        return self.__term_start_date

    @property
    def term_end_date(self):
        return self.__term_end_date

    @property
    def party(self):
        return self.__party
