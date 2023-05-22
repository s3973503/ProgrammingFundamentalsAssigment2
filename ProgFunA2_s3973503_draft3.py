import os.path
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
    
    def get_discount_rate(self):
        return RewardFlatCustomer.discount_rate
    
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
        return [self.ticket.get_price() * self.quantity, self.customer.get_booking_fee(self.quantity), self.customer.get_discount(self.ticket.get_price()* self.quantity)]

class Records:
    list_of_existing_customers=[]
    list_of_existing_movies=[]
    list_of_existing_ticket_types=[]

    def read_customers(self):
        f = open('customers.txt', 'r')
        for line in f.readlines():
            customer_details = line.split(",")
            # print(customer_details)
            if len(customer_details)==2:
                customer= Customer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==3:
                customer=RewardFlatCustomer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==4:
                customer=RewardStepCustomer(customer_details[0].strip(),customer_details[1].strip(),customer_details[2].strip())
            Records.list_of_existing_customers.append(customer)
        f.close()   
        
    def read_movies(self):
        f = open('movies.txt', 'r')
        for line in f.readlines():
            movie_details = line.split(",")
            # print(movie_details)
            movie=Movie(movie_details[0].strip(),movie_details[1].strip(),movie_details[2].strip())
            Records.list_of_existing_movies.append(movie)
        f.close()

    def read_tickets(self):
        f = open('tickets.txt', 'r')
        for line in f.readlines():
            ticket_details = line.split(",")
            # print(ticket_details)
            ticket=Ticket(ticket_details[0].strip(),ticket_details[1].strip(),float(ticket_details[2].strip()))
            Records.list_of_existing_ticket_types.append(ticket)
        f.close()

    def find_customer(self,customer_search_keyword):
        for customer in Records.list_of_existing_customers:
            if customer.get_id() == customer_search_keyword or customer.get_name()==customer_search_keyword:
                return customer
            else:
                return None
            
    def find_movie(self,movie_search_keyword):
        for movie in Records.list_of_existing_movies:
            print(movie.get_name())
            if movie.get_id()==movie_search_keyword or movie.get_name()==movie_search_keyword:
                return movie
            else:
                return None
            
    def find_ticket(self,ticket_search_keyword):
        for ticket in Records.list_of_existing_ticket_types:
            if ticket.get_id()==ticket_search_keyword or ticket.get_name()==ticket_search_keyword:
                return ticket
            else:
                return None
            
    def display_customers(self):
        print("{:<10} {:<10} {:<10} {:<10} ".format( 'id', 'name', 'discount_rate','threshold')) 
        for customer in Records.list_of_existing_customers:
            if isinstance(customer,RewardStepCustomer):
                print("{:<10} {:<15} {:<10} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount_rate(),customer.get_threshold())) 
            elif isinstance(customer,RewardFlatCustomer):
                print("{:<10} {:<15} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount_rate()))   
            else:
                print("{:<10} {:<15} ".format( customer.get_id(),customer.get_name()))
    
    def display_movies(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'seat_available'))
        for movie in Records.list_of_existing_movies:
            print("{:<10} {:<10} {:<10} ".format( movie.get_id(), movie.get_name(),movie.get_seat_available()))

    def display_tickets(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'unit_price'))
        for ticket in Records.list_of_existing_ticket_types:
            print("{:<10} {:<10} {:<10} ".format( ticket.get_id(), ticket.get_name(),ticket.get_price()))


class Operations():

    def __init__(self):
        self.record = Records()
        self.record.read_customers()
        self.record.read_movies()
        self.record.read_tickets()

    def check_file(self):  
        if True != os.path.isfile('./customers.txt'):
            print('customers.txt file not found')    
        if True != os.path.isfile('./movies.txt'):
            print('movies.txt file not found')
        if True != os.path.isfile('./tickets.txt'):
            print('tickets.txt file not found')

    def ticket_purchase(self):
        # record = Records()
        
        customer_name=input("Enter the name of the customer[e.g. Huong]:")
        self.customer=self.record.find_customer(customer_search_keyword=customer_name)

        while True:
            movie_name=input("Enter the name of the movie [enter a valid movie only e.g. Avatar]:")
            self.movie=self.record.find_movie(movie_search_keyword=movie_name)
            if self.movie == None:
                print("Please enter the valid name only")
            else:
                break
        
        while True:
            ticket_type=input("Enter the ticket type [enter a valid type only e.g. adult,child,senior,]:")
            self.ticket=self.record.find_ticket(ticket_search_keyword=ticket_type)
            if self.ticket == None:
                print("Please enter valid type only")
            else:
                break
        
        self.ticket_quantity=int(input("Enter the ticket quantity[enter a positive integer only e.g 1,2,3]"))
        
        if self.customer == None:
            y_or_n= input("The customer is not in the rewards program. Do you want to register for rewards program[enter y or n]")
            if y_or_n=="y":
                f_or_s=input("What kind of rewards the customer wants?[enter F or S]")
                if f_or_s=="F":
                    # TODO: ID is hardcoded - Randamize it
                    self.customer=RewardFlatCustomer("F10",customer_name)
                    Records.list_of_existing_customers.append(self.customer)
                elif f_or_s=="S":
                    # TODO: ID is hardcoded - Randamize it
                    self.customer=RewardStepCustomer("S10",customer_name,0.3)
                    Records.list_of_existing_customers.append(self.customer)       
            elif y_or_n=="n":
                self.customer=Customer("c7",customer_name)
                Records.list_of_existing_customers.append(self.customer)

        booking=Booking(self.customer,self.movie,self.ticket,self.ticket_quantity)
        self.total_cost_list=booking.compute_cost()
        self.total_cost=self.total_cost_list[0]+self.total_cost_list[1]-self.total_cost_list[2]
        

    def print_reciept(self):
        print("-------------------------------------------------")
        print("Reciept of  ", self.customer.get_name() )
        print("--------------------------------------------------")
        print("movie:                ", self.movie.get_name())
        print("Ticket Type:          ", self.ticket.get_name())
        print("Ticket Unit Price:    ", self.ticket.get_price())
        print("Ticket quantity:      ", self.ticket_quantity)


        print("-----------------------------------------------------")
        print("discount:              ", self.customer.get_discount(self.total_cost_list[0]))
        print("Booking fee            ", self.customer.get_booking_fee(self.ticket_quantity))
        print("Total cost             ", self.total_cost)

    def display_customers_information(self):
        self.record.display_customers()



    # def display_customer_information(self):
         
    # def display_movie_information(self):
       
    # def display_ticket_types_info(self):
     
    
    
if __name__ == "__main__":
    print("welcome to RMIT Ticketing sysytem!")
    operation = Operations()
    operation.check_file()
    value = input("Enter a number")
    # operation.print_reciept()
    while True:
        # operation = menu()
        if value == "1":
            operation.ticket_purchase()
            break
            # ticket_purchase()
        if value == "2":
            operation.display_customers_information()
            break
            # display_customer()
        # if operation == "3":
        #     display_movies()
        # if operation == "4":
        #     display_tickets()
        # if operation == "0":
        #     print("Thank you for visiting RMIT Ticketing system")
        #     exit
        #     break