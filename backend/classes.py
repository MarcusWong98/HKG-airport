class HK_flights:

    def __init__(self, date = str, destination = str, airline = str, status = str, time = str):
        self.date = date
        self.desination = destination
        self.airline = airline
        self.status = status
        self.time = time


    # def pagination(self, maximum = int, page = 1):

    #     first_page = maximum * (page - 1)

    #     last_page = first_page + maximum

    #     self.flights = self.flights[first_page:last_page]

    #     return self

    def to_object(self):

        return {
            'date' : self.date,
            'destination': self.desination,
            'airline': self.airline,
            'status': self.status,
            'time': self.time
        }