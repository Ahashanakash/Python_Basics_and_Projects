class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list =  []
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, date, time):
        __show = (id, movie_name, date, time)
        self.__show_list.append(__show)

        self.__seats[id] = [[0] * self.__cols for _ in range(self.__rows)]

    def book_seat(self, id, row, col):
        if id not in self.__seats:
            print("Show ID doesn't exist.")
            return
        if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
            print(f"Seat ({row}, {col}) is out of range.")
            return

        if self.__seats[id][row][col] == 0:
            self.__seats[id][row][col] = 1
            print(f"Seat ({row}, {col}) successfully booked for show ID {id}.")
        else:
            print(f"Seat ({row}, {col}) is already booked.")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Show ID doesn't exist.")
            return

        print(f"Available seats for show ID {id}:")
        for row in self.__seats[id]:
            for seat in row:
                print(seat, end=" ")
            print()

    def view_show_list(self):
        print(f"Hall - {self.__hall_no} Show Details:")
        for show in self.__show_list:
            print(f" Movie name: {show[1]}({show[0]}) -- Show ID: {show[0]} -- Date: {show[2]} -- Time: {show[3]}")


hall1 = Hall(rows=5, cols=5, hall_no="101")
hall2 = Hall(rows=10, cols=10, hall_no="201")
hall3 = Hall(rows=8, cols=8, hall_no="303")

hall1.entry_show(id="11", movie_name="Hawa", date="17/11/2024", time="6:00 PM")
hall2.entry_show(id="22", movie_name="Poran", date="17/11/2024", time="8:00 PM")
hall3.entry_show(id="33", movie_name="Joker", date="17/11/2024", time="10:00 PM")

while True:
    print("\n1. View All show today.")
    print("2. View Available seats.")
    print("3. Book Ticket.")
    print("4. Exit")

    choice = int(input("Enter Option - "))

    if choice == 1:
        print("----------------------------------")
        hall1.view_show_list()
        hall2.view_show_list()
        hall3.view_show_list()
        print("----------------------------------")
    if choice == 2:
        id = input("Enter ID - ")
        if id == "11":
            hall1.view_available_seats(id)
        elif id == "22":
            hall2.view_available_seats(id)
        elif id == "33":
            hall3.view_available_seats(id)
        else:
            print("This show is not running.")
    if choice == 3:
        number_of_ticket = int(input("Number of ticket - "))
        while number_of_ticket:
            id = input("Enter show ID - ")
            if id == "11":
                row = int(input("Enter seat row - "))
                col = int(input("Enter seat column - "))
                hall1.book_seat(id, row, col)
            elif id == "22":
                row = int(input("Enter seat row - "))
                col = int(input("Enter seat column - "))
                hall2.book_seat(id, row, col)
            elif id == "33":
                row = int(input("Enter seat row - "))
                col = int(input("Enter seat column - "))
                hall3.book_seat(id, row, col)
            else:
                print("This show is not running.")
            number_of_ticket -= 1
    if choice == 4:
        print("Exiting......")
        break
