class Passenger:  # creating the passenger class
    def __init__(self, name, origin, destination, flight_number, date):  # initiating the class and its attributes
        self.name = name
        self.origin = origin
        self.destination = destination
        self.flight_number = flight_number
        self.date = date

    # Setter and getter methods for Passenger attributes
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_origin(self, origin):
        self.origin = origin

    def get_origin(self):
        return self.origin

    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_flight_number(self):
        return self.flight_number

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date


class Flight:  # creating the flight class
    def __init__(self, number, gate, departure_time):  # initiating the flight class and its attributes
        self.number = number
        self.gate = gate
        self.departure_time = departure_time

    # Setter and getter methods for Flight attributes
    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_gate(self, gate):
        self.gate = gate

    def get_gate(self):
        return self.gate

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_departure_time(self):
        return self.departure_time


class BoardingPass:  # creating boarding pass class
    def __init__(self, seat, boarding_till, e_ticket_number):  # initiating the class and its attributes
        self.seat = seat
        self.boarding_till = boarding_till
        self.e_ticket_number = e_ticket_number

    # Setter and getter methods for BoardingPass attributes
    def set_seat(self, seat):
        self.seat = seat

    def get_seat(self):
        return self.seat

    def set_boarding_till(self, boarding_till):
        self.boarding_till = boarding_till

    def get_boarding_till(self):
        return self.boarding_till

    def set_e_ticket_number(self, e_ticket_number):
        self.e_ticket_number = e_ticket_number

    def get_e_ticket_number(self):
        return self.e_ticket_number


class Ticket:
    def __init__(self, passenger, flight, boarding_pass):
        self.passenger = passenger
        self.flight = flight
        self.boarding_pass = boarding_pass

    # Setter and getter methods for Ticket attributes
    def set_passenger(self, passenger):
        self.passenger = passenger

    def get_passenger(self):
        return self.passenger

    def set_flight(self, flight):
        self.flight = flight

    def get_flight(self):
        return self.flight

    def set_boarding_pass(self, boarding_pass):
        self.boarding_pass = boarding_pass

    def get_boarding_pass(self):
        return self.boarding_pass


# Creating objects
passenger = Passenger("Mohammed Ali", "Abu Dhabi", "London", "BA123", "2024-02-23")
flight = Flight("BA123", "Gate 10", "10:00")
boarding_pass = BoardingPass("23A", "09:30", "ET12345678")
ticket = Ticket(passenger, flight, boarding_pass)

# Displaying boarding pass details
print("Passenger Name:", ticket.passenger.get_name())
print("From:", ticket.passenger.origin)
print("To:", ticket.passenger.destination)
print("Flight Number:", ticket.passenger.flight_number)
print("Date:", ticket.passenger.date)
print("Gate:", ticket.flight.gate)
print("Departure Time:", ticket.flight.departure_time)
print("Seat:", ticket.boarding_pass.get_seat())
print("Boarding Till:", ticket.boarding_pass.boarding_till)
print("Electronic Ticket Number:", ticket.boarding_pass.e_ticket_number)
