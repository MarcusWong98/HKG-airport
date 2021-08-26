class HK_flights:

    def __init__(self, arrival = bool, cargo = bool, date = str, flights = list):
        self.arrival = arrival
        self.cargo = cargo
        self.date = date
        self.flights = flights


    def pagination(self, maximum = int, page = 1):

        first_page = maximum * page

        last_page = first_page + maximum

        self.flights = self.flights[first_page:last_page]

        return self

    def to_json(self):

        return {
            'arrival' : self.arrival,
            'cargo' : self.cargo,
            'date' : self.date,
            'flights': self.flights
        }