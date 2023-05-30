import os.path
import sys
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
    
    #TODO: update this to print right customer information details
    def get_display_info(self):
        print(self.discount_rate)

    def get_discount_rate(self):
        return RewardFlatCustomer.discount_rate

    def set_discount_rate(self,discount_rate):
        RewardFlatCustomer.discount_rate=discount_rate 


class RewardStepCustomer(Customer):
    threshold=50

    def __init__(self,id,name,discount_rate=0.3):
        super().__init__(id,name)
        self.discount_rate=discount_rate

    def get_discount(self,cost):
        print(type(cost))
        print(type(self.discount_rate))
        if cost >= RewardStepCustomer.threshold:
            return cost*self.discount_rate
        return 0
    
    #TODO: update this method with right attributes
    def display_info(self):
        print(self.discount_rate)
    
    def get_discount_rate(self):
        return self.discount_rate
    
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

class GroupTicket(Ticket):
    def __init__(self,id,group_name,group_ticket_price,group_ticket_type_dic):
        super().__init__(id,group_name,group_ticket_price)
        self.group_ticket_type_dic = group_ticket_type_dic
    
    def display_info(self):
        print(self.id,self.name,self.price)

class Booking:
    def __init__(self,customer,movie,ticket,quantity):
        self.customer=customer
        self.movie=movie
        self.ticket=ticket
        self.quantity=quantity

    def get_customer(self):
        return self.customer
    
    def get_movie(self):
        return self.movie
    
    def get_ticket(self):
        return self.ticket
    
    def get_quantity(self):
        return self.quantity

    def compute_cost(self):
        result = []
        print(self.ticket)
        print(self.quantity)
        for index in range(0, len(self.ticket)):
            result.append(self.ticket[index].get_price() * self.quantity[index])

        return [sum(result), self.customer.get_booking_fee(sum(self.quantity)), self.customer.get_discount(sum(result))]

class Records:
    list_of_existing_customers=[]
    list_of_existing_movies=[]
    list_of_existing_ticket_types=[]
    list_of_existing_booking=[]

    def read_customers(self,customer_details_path):
        if customer_details_path=="":
            customer_details_path="customers.txt"
        f = open(customer_details_path, 'r')
        for line in f.readlines():
            customer_details = line.split(",")
            if len(customer_details)==2:
                customer= Customer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==3:
                customer=RewardFlatCustomer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==4:
                customer=RewardStepCustomer(customer_details[0].strip(),customer_details[1].strip(),float(customer_details[2].strip()))
            Records.list_of_existing_customers.append(customer)
        f.close()   
        
    def read_movies(self,movie_details_path):
        if movie_details_path=="":
            movie_details_path="movies.txt"
        f = open(movie_details_path, 'r')
        for line in f.readlines():
            movie_details = line.split(",")
            movie=Movie(movie_details[0].strip(),movie_details[1].strip(),movie_details[2].strip())
            Records.list_of_existing_movies.append(movie)
        f.close()

    def read_tickets(self,ticket_details_path):
        if ticket_details_path=="":
            ticket_details_path="tickets.txt"
        f = open(ticket_details_path, 'r')
        for line in f.readlines():
            ticket_details = line.split(",")
            if "T" in ticket_details[0]:
                ticket=Ticket(ticket_details[0].strip(),ticket_details[1].strip(),float(ticket_details[2].strip()))
                Records.list_of_existing_ticket_types.append(ticket)
            elif "G" in ticket_details[0]:
                group_ticket_type=ticket_details[2:]
                # print(group_ticket_type)
                # 1. itterate over the list of group_ticket_type
                # 2. itteration -> group_ticket_type[0] 
                # 3. check if this ticket_type exsits in that ticket_type list
                # 4. if present then get me the object of ticket_type
                # 5. if not present throw error and continue the program
                # 6. when present -> append to dic -> key will be the object of ticket_type and value will quantity i.e group_ticket_type[1]
                group_ticket_dict={}
                for index in range(len(group_ticket_type)):
                    if index % 2 == 0:
                        # print("printing:", group_ticket_type[index])
                        ticket_object = self.find_ticket(group_ticket_type[index].strip())
                        print(ticket_object)
                        # print(ticket_object.get_name())
                        if ticket_object==None:
                            print("The ticket does not exists")
                            group_ticket_dict = {}
                            break
                        else:
                            group_ticket_dict[ticket_object]=int(group_ticket_type[index + 1 ].strip())
                # 7. loop throw dic and check if the sum of ticket_price is greater than 50 if not throw an error and don't create an object of GroupTicket
                # 8. if price greater than 50 create an object of Group Ticket. 
                group_ticket_list=[]
                for key,value in group_ticket_dict.items():
                    # print(type(value))
                    # print(key.get_price())
                    group_ticket_list.append(key.get_price() * value)
                if (sum(group_ticket_list)*0.8)>=50:
                    group_ticket=GroupTicket(ticket_details[0].strip(), ticket_details[1].strip(),(sum(group_ticket_list)*0.8), group_ticket_dict)
                    Records.list_of_existing_ticket_types.append(group_ticket)
        f.close()
    def read_booking(self,booking_details_path):
        f = open(booking_details_path, 'r')
        for line in f.readlines():
            list_of_ticktet_type_booking=[]
            list_of_ticket_quantity_booking=[]
            booking_details = line.split(",")
            for index in range(2,len(booking_details)):
                if (index%2==0):
                    details=self.find_ticket(booking_details[index])
                    if details!=None:
                        list_of_ticktet_type_booking.append(booking_details[index])
                        list_of_ticket_quantity_booking.append(booking_details[index +1])
                    else:
                         break
            customer = self.find_customer(booking_details[0].strip())
            movie = self.find_movie(booking_details[1])
            booking = Booking(customer,movie,list_of_ticktet_type_booking,list_of_ticket_quantity_booking)
            Records.list_of_existing_booking.append(booking)
        f.close()

    def find_customer(self,customer_search_keyword):
        for customer in Records.list_of_existing_customers:
            if customer.get_id() == customer_search_keyword or customer.get_name()==customer_search_keyword:
                return customer
        return None
            
    def find_movie(self,movie_search_keyword):
        for movie in Records.list_of_existing_movies:
            if movie.get_id()==movie_search_keyword or movie.get_name()==movie_search_keyword:
                return movie
        return None
            
    def find_ticket(self,ticket_search_keyword):
        for ticket in Records.list_of_existing_ticket_types:
            if ticket.get_id()==ticket_search_keyword or ticket.get_name()==ticket_search_keyword:
                return ticket
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

    def display_booking(self):
        # print("{:<10} {:<10} {:<10} ".format( 'customerName/id', 'MovieName/id', ))
        # for index in range(0, len(self.ticket_type_list)):
        #         print("{}, {}, ".format("ticketType", 'TicketQuantity'))
        # print("{}, {}, {}\n".format('discount', 'bookingFee','TotalCost'))
        f = open('booking.txt', 'r')
        for line in f.readlines():
            
            list_of_ticktet_type_booking=[]
            list_of_ticket_quantity_booking=[]
            booking_details = line.split(",")

            for index in range(2,len(booking_details)):
                if (index%2==0):
                    details=self.find_ticket(booking_details[index])
                    if details!=None:
                        list_of_ticktet_type_booking.append(booking_details[index])
                        list_of_ticket_quantity_booking.append(booking_details[index +1])
                    else:
                         break                              

class Operations():

    def check_file(self):  
        if True != os.path.isfile('./customers.txt'):
            print('customers.txt file not found')    
        if True != os.path.isfile('./movies.txt'):
            print('movies.txt file not found')
        if True != os.path.isfile('./tickets.txt'):
            print('tickets.txt file not found')

    def __init__(self,customer_details_path,movie_details_path,ticket_details_path,booking_details_path):
        self.check_file()
        self.record = Records()
        self.record.read_customers(customer_details_path)
        self.record.read_movies(movie_details_path)
        self.record.read_tickets(ticket_details_path)
        if booking_details_path !='':
            self.record.read_booking(booking_details_path)

    def menu(self):
        print("####################################################################")
        print("""You can choose from the following option\n
                1:Purchase a ticket
                2:Display existing customer information 
                3:Display exisiting movie information
                4:Display existing ticket information
                5:Add new movies
                6.Adjust discount rate for all flat customers
                7.Adjust discount rate for all Step customers
                0: Exit the program""")
        print("####################################################################")
        operation_input_type = input("choose one option")
        return operation_input_type
    
    def check_quantity(self):
        ticket_quantity_list=[]
        if len(self.ticket_quantity) != len(self.ticket_type_list):
            return False
    
        for quantity in self.ticket_quantity:
            try:
                if int(quantity) <= 0:
                    return False
                ticket_quantity_list.append(int(quantity))
                if sum(ticket_quantity_list) > int(self.movie.get_seat_available()):
                    print("The quantity must be less than number of available seats .please enter a smaller ticket quantity")
                    # print("Ticket Available: ", available_movies[movie])
                    return False
            except ValueError:
                return False
        return True

    def ticket_purchase(self):
        
        customer_name=input("Enter the name of the customer[e.g. Huong]:")

        while True:
            movie_name=input("Enter the name of the movie [enter a valid movie only e.g. Avatar]:")
            self.movie=self.record.find_movie(movie_search_keyword=movie_name)
            if self.movie == None:
                print("Please enter the valid name only")
            else:
                if int(self.movie.get_seat_available())<=0:
                    print("There is no available seats for {} please enter a different movie".format(self.movie.get_name()))
                    continue
                break
        
        while True:
            #1. take the input as string
            ticket_type=input("Enter the ticket type [enter a valid type only e.g. adult,child,senior,]:")
            #2. split the list by comma
            ticket_type=ticket_type.strip().split(',')
            self.ticket_type_list = []
            for individual_ticket_type in ticket_type:
                returned_value = self.record.find_ticket(ticket_search_keyword=individual_ticket_type)
                if returned_value == None:
                    # print("Please enter the valid ticket type")
                    break
                self.ticket_type_list.append(returned_value)

            if len(self.ticket_type_list) == len(ticket_type):
                break
            else:
                print("Please enter the valid ticket type")

        while True:
            self.ticket_quantity=input("Enter the ticket quantity[enter a positive integer only e.g 1,2,3]").strip().split(",")
            return_value = self.check_quantity()
            if return_value == True:
                self.ticket_quantity_list = []
                for quantity in self.ticket_quantity:
                    ticket_q = int(quantity.strip())
                    self.ticket_quantity_list.append(ticket_q)
                break
            elif return_value == False:
                print("Please enter a valid ticket quantity")

        self.customer=self.record.find_customer(customer_search_keyword=customer_name)
        
        if self.customer == None:
            while True:
                y_or_n= input("The customer is not in the rewards program. Do you want to register for rewards program[enter y or n]")
                if y_or_n=="y":
                    while True:
                        f_or_s=input("What kind of rewards the customer wants?[enter F or S]")
                        if f_or_s=="F":
                            # TODO: ID is hardcoded - Randamize it
                            self.customer=RewardFlatCustomer("F10",customer_name)
                            Records.list_of_existing_customers.append(self.customer)
                            break
                        elif f_or_s=="S":
                            # TODO: ID is hardcoded - Randamize it
                            self.customer=RewardStepCustomer("S10",customer_name,0.3)
                            Records.list_of_existing_customers.append(self.customer)
                            break
                        else:
                            print("Enther the valid type")
                    break
                elif y_or_n=="n":
                    # TODO: ID is hardcoded - Randamize it
                    self.customer=Customer("c7",customer_name)
                    Records.list_of_existing_customers.append(self.customer)
                    break
                else:
                    print("Enter the valid type")

        # print(self.customer,self.movie,self.ticket_type_list,self.ticket_quantity_list)
        booking=Booking(self.customer,self.movie,self.ticket_type_list,self.ticket_quantity_list)
        self.total_cost_list=booking.compute_cost()
        self.total_cost=self.total_cost_list[0]+self.total_cost_list[1]-self.total_cost_list[2]
        self.seats=self.movie.set_seat_available(int(self.movie.get_seat_available()) - sum(self.ticket_quantity_list))
        self.add_to_booking()
        self.print_reciept()

    def add_to_booking(self):
        # read the file if its not there print ("file not found")
        # check if it empty or not
        # if its empty it return true 
        # append the values 
        # if not empty then \n and append
        try:
            f = open("booking.txt","r")
            f.close()
        except:
            f = open("booking.txt", "x")
            f.close()

        try:
            f = open("booking.txt", "a")
            f.write("{}, {}, ".format(self.customer.get_name(), self.movie.get_name()))
            for index in range(0, len(self.ticket_type_list)):
                f.write("{}, {}, ".format(self.ticket_type_list[index].get_name(), self.ticket_quantity_list[index]))
            f.write("{}, {}, {}\n".format(self.customer.get_discount(self.total_cost_list[0]), 
                                        self.customer.get_booking_fee(sum(self.ticket_quantity_list)), 
                                        self.total_cost))
            f.close()
        except:
            print('error occured')
      
    def print_reciept(self):
        print("-------------------------------------------------")
        print("Reciept of  ", self.customer.get_name())
        print("--------------------------------------------------")
        print("Movie:                   ",      self.movie.get_name())
        for index in range(0, len(self.ticket_type_list)):
            print("Ticket Type:          ",     self.ticket_type_list[index].get_name())
            print("Ticket Unit Price:    ",     self.ticket_type_list[index].get_price())
            print("Ticket quantity:      ",     self.ticket_quantity_list[index])
            if len(self.ticket_type_list) > 1:
                print("             ------                ")
        print("-----------------------------------------------------")
        print("discount:              ", self.customer.get_discount(self.total_cost_list[0]))
        print("Booking fee            ", self.customer.get_booking_fee(sum(self.ticket_quantity_list)))
        print("Total cost             ", self.total_cost)

    def display_customers_information(self):
        self.record.display_customers()

    def display_movie_information(self):
         self.record.display_movies()
    
    def display_ticket_information(self):
        self.record.display_tickets()
     
    def add_new_movies(self):
        while True:
            y_or_n = input("Do you want to add a list of movies  [enter y or n]")
            if y_or_n == "y":
                print("Enter the list of movies")
                movies_input = input().strip()
                movies_list = movies_input.split(",")
                for movies in movies_list:
                    movies = movies.strip()
                    returned_result= self.record.find_movie(movies)
                    if returned_result==None:
                        movie=Movie("M10",movies,seat_available=50)
                        Records.list_of_existing_movies.append(movie)
                        print("{} movie added".format(movies))
                    else:
                        print("Movie already exists")        
            break  

    def adjust_discount_rate_flat(self): 
        while True:
            try:
                rate = float(input("Enter the new discount rate for RewardFlat customers: "))
                if rate <= 0:
                    raise ValueError("Discount rate must be a positive number.")
                else:
                    RewardFlatCustomer.discount_rate = rate
                    break
            except ValueError as e:
                print(e)  

    def adjust_discount_rate_step(self):
        while True:
            name_or_id=input("Enter the name or id of the reward step customer")
            name_or_id=self.record.find_customer(name_or_id)
            if name_or_id!=None:
                if isinstance(name_or_id,RewardStepCustomer):
                    try:
                        rate = float(input("Enter the new discount rate for RewardStep customers: "))
                        if rate <= 0:
                            raise ValueError("Discount rate must be a positive number.")
                        else:
                            name_or_id.set_discount_rate(rate)
                            break
                    except ValueError as e:
                        print(e)  
            elif name_or_id==None:
                print("The customer does not exist please enter the valid customer")




            
if __name__ == "__main__":
    # Get the file names from the command line arguments
    if len(sys.argv)not in [1,4,5]:
        print("Incorrect usage of arguments. Please provide four file names: customer file, movie file, ticket file, and booking file (optional).")
        sys.exit(1)
    elif len(sys.argv)==4:
        customer_details_path = sys.argv[1]
        movie_details_path = sys.argv[2]
        ticket_details_path = sys.argv[3]
        booking_details_path=''
    elif len(sys.argv)==5:
        customer_details_path = sys.argv[1]
        movie_details_path = sys.argv[2]
        ticket_details_path = sys.argv[3]
        booking_details_path = sys.argv[4]
    else:
        customer_details_path = ''
        movie_details_path = ''
        ticket_details_path = ''
        booking_details_path = ''

    print("welcome to RMIT Ticketing sysytem!")
    operation = Operations(customer_details_path,movie_details_path,ticket_details_path,booking_details_path )
    while True:
        operation_input_type = operation.menu()
        if operation_input_type == "1":
            operation.ticket_purchase()
        if operation_input_type == "2":
            operation.display_customers_information()
        if operation_input_type == "3":
            operation.display_movie_information()
        if operation_input_type == "4":
            operation.display_ticket_information()
        if operation_input_type == "5":
            operation.add_new_movies()
        if operation_input_type == "6":
            operation.adjust_discount_rate_flat()
        if operation_input_type == "7":
            operation.adjust_discount_rate_step()
        if operation_input_type == "0":
            break





