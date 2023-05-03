class Customer:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_discount(self,cost):
        return 0
    
    def get_booking_fee(self,ticket_qunatity):
        return ticket_qunatity * 2
    
    def display_info(self):
        print(self.id, self.name)

class RewardFlatCustomer(Customer):
    discount_rate=0.2
    
    def __init__(self,id, name):
        super().__init__(id, name)

    def get_discount(self,cost):
        return cost * RewardFlatCustomer.discount_rate
    
    def get_display_info(self):
        print(self.discount_rate)

    def get_discount_rate(self):
        return RewardFlatCustomer.discount_rate

    def set_discount_rate(self,discount_rate):
        RewardFlatCustomer.discount_rate=discount_rate 

class RewardStepCustomer(Customer):
    threshold=50

    def __init__(self,id,name,discount_rate):
        super().__init__(id,name)
        self.discount_rate=discount_rate

    def get_discount(self,cost):
        if cost >= RewardStepCustomer.threshold:
            return cost*self.discount_rate
        return 0
    
    def display_info(self):
        print(self.discount_rate)
    
    def set_discount_rate(self,discount_rate):
        self.discount_rate=discount_rate

    def get_threshold(self):
        return RewardStepCustomer.threshold
    
    def set_threshold(self,threshold):
        RewardStepCustomer.threshold=threshold

class Movie:
    def __init__(self,id,name,seat_available):
         self.id=id
         self.name=name
         self.seat_available=seat_available
    
    def display_info(self):
        print(self.id,self.name,self.seat_available)
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_seat_available(self):
        return self.seat_available
    
    def set_seat_available(self,seat_available):
        self.seat_available =seat_available

class Ticket:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def  get_price(self):
        return self.price
    
    def display_info(self):
        print(self.id,self.name,self.price)

class Booking:
    def __init__(self,customer,movie,ticket,quantity):
        self.customer=customer
        self.movie=movie
        self.ticket=ticket
        self.quantity=quantity

    def compute_cost(self):
        return [self.ticket.get_price()* self.quanity, self.customer.get_booking_fee(), self.customer.get_discount()]

class Records:
    list_of_existing_customers=[]
    list_of_existing_movies=[]
    list_of_existing_ticket_types=[]

    def read_customers():
        f = open('customers.txt', 'r')
        for line in f.readlines():
            customer_details = line.split(",")
            print(customer_details)
            if len(customer_details)==2:
                customer= Customer(customer_details[0],customer_details[1])
            elif len(customer_details)==3:
                customer=RewardFlatCustomer(customer_details[0],customer_details[1])
            elif len(customer_details)==4:
                customer=RewardFlatCustomer(customer_details[0],customer_details[1,customer_details[2]])
            Records.list_of_existing_customers.append(customer)
        f.close()   
        
    def read_movies():
        f = open('movies.txt', 'r')
        for line in f.readlines():
            movie_details = line.split(",")
            print(movie_details)
            movie=Movie(movie_details[0],movie_details[1],movie_details[2])
            Records.list_of_existing_movies.append(movie)
        f.close()

    def read_tickets():
        f = open('tickets.txt', 'r')
        for line in f.readlines():
            ticket_details = line.split(",")
            print(ticket_details)
            ticket=Ticket(ticket_details[0],ticket_details[1],ticket_details[2])
            Records.list_of_existing_ticket_types.append(ticket)
        f.close()

    def display_customers(self):
        print("{:<10} {:<10} {:<10} {:<10} ".format( 'id', 'name', 'discount','threshold')) 
        for customer in Records.list_of_existing_customers:
            if isinstance(customer,RewardStepCustomer):
                print("{:<10} {:<10} {:<10} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount(),customer.get_threshold())) 
            elif isinstance(customer,RewardFlatCustomer):
                print("{:<10} {:<10} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount()))   
            else:
                print("{:<10} {:<10} ".format( customer.get_id(),customer.get_name()))
    
    def display_movies(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'seat_available'))
        for movie in Records.list_of_existing_movies:
            print("{:<10} {:<10} {:<10} ".format( movie.get_id(), movie.get_name(),movie.get_seat_available()))

    def display_tickets(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'unit_price'))
        for ticket in Records.list_of_existing_ticket_types:
            print("{:<10} {:<10} {:<10} ".format( ticket.get_id(), ticket.get_name(),ticket.get_price()))


        