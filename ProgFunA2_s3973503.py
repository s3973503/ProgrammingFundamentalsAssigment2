import os.path
import sys

# Creating a class customer with  approriate getters(id,name, discount) and setters 
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

# Creating a class customer with  approriate getters and setters 
# We are overriding customer class to get the name and id of the customers in reward 
# also using inhertitence to inherit the customer class to Reward Flat customer.
class RewardFlatCustomer(Customer):
    discount_rate=0.2
    
    def __init__(self,id, name):
        super().__init__(id, name)

    def get_discount(self,cost):
        return cost * RewardFlatCustomer.discount_rate
    
    def get_display_info(self):
        print(self.id, self.name, self.discount_rate)

    def get_discount_rate(self):
        return RewardFlatCustomer.discount_rate

    def set_discount_rate(self,discount_rate):
        RewardFlatCustomer.discount_rate=discount_rate 

# Creating a class customer with  approriate getters and setters 
# We are overriding customer class to get the name and id of the customers in reward step 
# also using inhertitence to inherit the customer class to Reward Step customer.
class RewardStepCustomer(Customer):
    threshold=50

    def __init__(self,id,name,discount_rate=0.3):
        super().__init__(id,name)
        self.discount_rate=discount_rate

    def get_discount(self,cost):
        if cost >= RewardStepCustomer.threshold:
            return cost*self.discount_rate
        return 0
    

    def display_info(self):
        print(self.id, self.name, self.discount_rate)

    
    def get_discount_rate(self):
        return self.discount_rate
    
    def set_discount_rate(self,discount_rate):
        self.discount_rate=discount_rate


    def get_threshold(self):
        return RewardStepCustomer.threshold
    
    def set_threshold(self,threshold):
        RewardStepCustomer.threshold=threshold

#Creating a class movie with approriate getters(moviename,id,seat available) and setters (seat available)
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

# creating a class ticket with approriate getter(id,name,price)
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
        return round(self.price,2)
    
    def display_info(self):
        print(self.id,self.name,self.price)

# Creating a class group ticket and inheriting the class ticket in Group ticket because we already have id ,name of the ticket in ticket
class GroupTicket(Ticket):
    def __init__(self,id,group_name,group_ticket_price,group_ticket_type_dic):
        super().__init__(id,group_name,group_ticket_price)
        self.group_ticket_type_dic = group_ticket_type_dic
    
    def display_info(self):
        print(self.id,self.name,self.price)

# Create a class booking with customer details ,movie details,ticket type details and total cost
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
    
    # To compute the total cost of the booking of a customer.
    def compute_cost(self):
        result = []
        for index in range(0, len(self.ticket)):
            result.append(self.ticket[index].get_price() * self.quantity[index])
        
        return [round(sum(result),2), self.customer.get_booking_fee(sum(self.quantity)), round(self.customer.get_discount(sum(result)),2)]

# Create a class records
class Records:
    # Creating a empty list for storing exisiting customers,existing movies,existing ticket_types,exisiting bookings
    list_of_existing_customers=[]
    list_of_existing_movies=[]
    list_of_existing_ticket_types=[]
    list_of_existing_booking=[]

    # Function to read the customer from the customer.txt file
    def read_customers(self,customer_details_path):
        f = open(customer_details_path, 'r')
        for line in f.readlines():
            customer_details = line.split(",")
            # Checking the length of customers to append the proper details because customer has only 2 values while reward customers has 3 attributes and Step customers has 4 attributes 
            if len(customer_details)==2:
                customer= Customer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==3:
                customer=RewardFlatCustomer(customer_details[0].strip(),customer_details[1].strip())
            elif len(customer_details)==4:
                customer=RewardStepCustomer(customer_details[0].strip(),customer_details[1].strip(),float(customer_details[2].strip()))
            Records.list_of_existing_customers.append(customer)
        f.close()

    # Function to read the movies from the movies.txt file   
    def read_movies(self,movie_details_path):
        f = open(movie_details_path, 'r')
        for line in f.readlines():
            movie_details = line.split(",")
            movie=Movie(movie_details[0].strip(),movie_details[1].strip(),movie_details[2].strip())
            Records.list_of_existing_movies.append(movie)
        f.close()

    # Function to read the tickets from the tickets.txt file 
    def read_tickets(self,ticket_details_path):
        f = open(ticket_details_path, 'r')
        for line in f.readlines():
            ticket_details = line.split(",")
            if "T" in ticket_details[0]:
                ticket=Ticket(ticket_details[0].strip(),ticket_details[1].strip(),float(ticket_details[2].strip()))
                Records.list_of_existing_ticket_types.append(ticket)
            elif "G" in ticket_details[0]:
                group_ticket_type=ticket_details[2:]
                # 1. itterate over the list of group_ticket_type
                # 2. itteration -> group_ticket_type[0] 
                # 3. check if this ticket_type exsits in that ticket_type list
                # 4. if present then get me the object of ticket_type
                # 5. if not present throw error and continue the program
                # 6. when present -> append to dic -> key will be the object of ticket_type and value will quantity i.e group_ticket_type[1]
                group_ticket_dict={}
                for index in range(len(group_ticket_type)):
                    if index % 2 == 0:
                        ticket_object = self.find_ticket(group_ticket_type[index].strip())
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
                    group_ticket_list.append(key.get_price() * value)
                if (sum(group_ticket_list)*0.8)>=50:
                    group_ticket=GroupTicket(ticket_details[0].strip(), ticket_details[1].strip(),(sum(group_ticket_list)*0.8), group_ticket_dict)
                    Records.list_of_existing_ticket_types.append(group_ticket)
                else:
                    print("Something wrong with the group ticket")
        f.close()

    # Function to read booking from bookings.txt
    def read_booking(self,booking_details_path):
        try:
            f = open(booking_details_path, 'r')
            for line in f.readlines():
                list_of_ticktet_type_booking=[]
                list_of_ticket_quantity_booking=[]
                booking_details = line.split(",")
                for index in range(2,len(booking_details)):
                    if (index%2==0):
                        details=self.find_ticket(booking_details[index].strip())
                        if details!=None:
                            list_of_ticktet_type_booking.append(details)
                            list_of_ticket_quantity_booking.append(int(booking_details[index +1].strip()))
                        else:
                            break
                customer = self.find_customer(booking_details[0].strip())
                movie = self.find_movie(booking_details[1].strip())
                booking = Booking(customer,movie,list_of_ticktet_type_booking,list_of_ticket_quantity_booking)
                Records.list_of_existing_booking.append(booking)
            f.close()
        except:
            print("Cannot load the booking file,run as if there is no previous booking file")
            Records.list_of_existing_booking = []

    # Function to check if the inputted customers is in already exisiting customers list
    def find_customer(self,customer_search_keyword):
        for customer in Records.list_of_existing_customers:
            if customer.get_id() == customer_search_keyword or customer.get_name()==customer_search_keyword:
                return customer
        return None
    
    # Function to check if the inputted movies is in already exisiting movies list           
    def find_movie(self,movie_search_keyword):
        for movie in Records.list_of_existing_movies:
            if movie.get_id()==movie_search_keyword or movie.get_name()==movie_search_keyword:
                return movie
        return None
    # Function to check if the inputted ticket type is in already exisiting ticket type list           
    def find_ticket(self,ticket_search_keyword):
        for ticket in Records.list_of_existing_ticket_types:
            if ticket.get_id()==ticket_search_keyword or ticket.get_name()==ticket_search_keyword:
                return ticket
        return None
    
    # Function to display existing customer infromation   
    def display_customers(self):
        print("{:<10} {:<10} {:<10} {:<10} ".format( 'id', 'name', 'discount_rate','threshold')) 
        for customer in Records.list_of_existing_customers:
            if isinstance(customer,RewardStepCustomer):
                print("{:<10} {:<15} {:<10} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount_rate(),customer.get_threshold())) 
            elif isinstance(customer,RewardFlatCustomer):
                print("{:<10} {:<15} {:<10} ".format( customer.get_id(),customer.get_name(),customer.get_discount_rate()))   
            else:
                print("{:<10} {:<15} ".format( customer.get_id(),customer.get_name()))

    # Function to display exisiting movies information
    def display_movies(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'seat_available'))
        for movie in Records.list_of_existing_movies:
            print("{:<10} {:<14} {:<14} ".format( movie.get_id(), movie.get_name(),movie.get_seat_available()))

    # Function to display exisiting ticketypes information.
    def display_tickets(self):
        print("{:<10} {:<10} {:<10} ".format( 'id', 'name', 'unit_price'))
        for ticket in Records.list_of_existing_ticket_types:
            print("{:<10} {:<14} {:<14} ".format( ticket.get_id(), ticket.get_name(),ticket.get_price()))

    # Function to display exisiting booking information.
    def display_booking(self):
        if True != os.path.isfile("booking.txt"):
            print('No Booking yet')
            return

        f = open('booking.txt', 'r')
        for line in f.readlines():
            print("********************************************************************")
            booking_details = line.split(",")
            print("Customer_name:", booking_details[0])
            print("Movie:",booking_details[1])
            for index in range(2,len(booking_details)):
                if index%2==0:
                    details=self.find_ticket(booking_details[index].strip())
                    if details!=None:
                        print("Ticket Type:",booking_details[index])
                        print("Ticket Quantity:",booking_details[index +1])
                    else:
                        print("Discount:",booking_details[index]) 
                        print("Booking Fee:",booking_details[index+1])
                        print("Total Cost:",booking_details[index+2])
                        break
        f.close()
     
                                          
# creating a class operations
class Operations():

    def __init__(self,customer_details_path,movie_details_path,ticket_details_path,booking_details_path):
        self.check_file(customer_details_path,movie_details_path,ticket_details_path)
        self.customer_details_path=customer_details_path
        self.movie_details_path=movie_details_path
        self.ticket_details_path=ticket_details_path
        self.booking_details_path=booking_details_path
        self.record = Records()
        self.record.read_customers(customer_details_path)
        self.record.read_movies(movie_details_path)
        self.record.read_tickets(ticket_details_path)
        if booking_details_path !='':
            self.record.read_booking(booking_details_path)

    def check_file(self,customer_details_path,movie_details_path,ticket_details_path ):  
        if True != os.path.isfile(customer_details_path):
            print('customers.txt file not found')
            quit()   
        if True != os.path.isfile(movie_details_path):
            print('movies.txt file not found')
            quit()   
        if True != os.path.isfile(ticket_details_path):
            print('tickets.txt file not found')
            quit()   

    # Printing the menu option to choose from the following:
    def menu(self):
        print("welcome to RMIT Ticketing sysytem!")
        print("####################################################################")
        print("""You can choose from the following option\n
            1:Purchase a ticket
            2:Display existing customer's information 
            3:Display exisiting movie's information
            4:Display existing ticket's  information
            5:Add movies
            6.Adjust discount rate of all Reward flat customers
            7.Adjust discount rate of a Reward Step customers
            8.Display all booking 
            9.Display the most Popular movie
            10.Display All movie record
            0: Exit the program""")
        print("####################################################################")
        operation_input_type = input("choose one option")
        return operation_input_type
    
    # Function to handle error inputs for quantity  
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
# Function to purchase ticket
    def ticket_purchase(self):
        # Asking the input from customers
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
            #1. take the input of movie  as string
            ticket_type=input("Enter the ticket type [enter a valid type only e.g. adult,child,senior,]:")
            #2. split the list by comma
            ticket_type=ticket_type.strip().split(',')
            self.ticket_type_list = []
            for individual_ticket_type in ticket_type:
                returned_value = self.record.find_ticket(ticket_search_keyword=individual_ticket_type)
                if returned_value == None:
                    break
                self.ticket_type_list.append(returned_value)

            if len(self.ticket_type_list) == len(ticket_type):
                break
            else:
                print("Please enter the valid ticket type")
# Take the input of quantity from the user
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
            # Asking the new customers if they want to join to rewards program 
        if self.customer == None:
            while True:
                y_or_n= input("The customer is not in the rewards program. Do you want to register for rewards program[enter y or n]")
                # Asking the new customers if they want to join to rewards program as step customer or flat customer 
                customer_index_value=len(Records.list_of_existing_customers)+1
                f = open(self.customer_details_path, 'a')
                if y_or_n=="y":
                    while True:
                        f_or_s=input("What kind of rewards the customer wants?[enter F or S]")
                        if f_or_s=="F":
                            self.customer=RewardFlatCustomer("F{}".format(customer_index_value),customer_name)
                            Records.list_of_existing_customers.append(self.customer)
                            f.write("\nF{}, {}, {}".format(customer_index_value,customer_name,RewardFlatCustomer.discount_rate))
                            f.close()
                            break
                        elif f_or_s=="S": 
                            self.customer=RewardStepCustomer("S{}".format(customer_index_value),customer_name,0.3)
                            Records.list_of_existing_customers.append(self.customer)
                            f.write("\nS{}, {}, {}, {}".format(customer_index_value,customer_name,self.customer.get_discount_rate(),RewardStepCustomer.threshold))
                            f.close()
                            break
                        else:
                            print("Enther the valid type")
                    break
                elif y_or_n=="n":
                    self.customer=Customer("C{}".format(customer_index_value),customer_name)
                    Records.list_of_existing_customers.append(self.customer)
                    f.write("\nC{}, {}".format(customer_index_value,customer_name))
                    f.close()
                    break
                else:
                    print("Enter the valid type")
        else:
            if isinstance(self.customer,RewardFlatCustomer):
                print(self.customer.get_name() ,"is already a RewardFlat Customer")
            elif isinstance(self.customer,RewardStepCustomer):
                print(self.customer.get_name() ,"is already a RewardStep Customer")
            elif isinstance(self.customer,Customer):
                print(self.customer.get_name(),"is already a standard customer")
            
        # print(self.customer,self.movie,self.ticket_type_list,self.ticket_quantity_list)
        booking=Booking(self.customer,self.movie,self.ticket_type_list,self.ticket_quantity_list)
        Records.list_of_existing_booking.append(booking)
        self.total_cost_list=booking.compute_cost()
        discount=round(self.total_cost_list[2],2)
        cost = self.total_cost_list[0]+self.total_cost_list[1]-discount
        self.total_cost=round(cost,2)
        self.seats=self.movie.set_seat_available(int(self.movie.get_seat_available()) - sum(self.ticket_quantity_list))
        self.add_to_booking()
        self.print_reciept()

# Function to add all the bookings made by the customers to booking.txt
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
            if os.path.getsize('booking.txt') == 0:
                f.write("{}, {}, ".format(self.customer.get_name(), self.movie.get_name()))
                for index in range(0, len(self.ticket_type_list)):
                    f.write("{}, {}, ".format(self.ticket_type_list[index].get_name(), self.ticket_quantity_list[index]))
                f.write("{}, {}, {}".format(round(self.total_cost_list[2],2), 
                                            self.customer.get_booking_fee(sum(self.ticket_quantity_list)), 
                                            self.total_cost))
                f.close()
            else:
                f.write("\n{}, {}, ".format(self.customer.get_name(), self.movie.get_name()))
                for index in range(0, len(self.ticket_type_list)):
                    f.write("{}, {}, ".format(self.ticket_type_list[index].get_name(), self.ticket_quantity_list[index]))
                f.write("{}, {}, {}".format(round(self.total_cost_list[2],2), 
                                            self.customer.get_booking_fee(sum(self.ticket_quantity_list)), 
                                            self.total_cost))
                f.close()

        except:
            print('error occured')
            
# Function to print the recipet   
    def print_reciept(self):
        print("-------------------------------------------------")
        print("Reciept of  ", self.customer.get_name())
        print("--------------------------------------------------")
        print("Movie:                ",    self.movie.get_name())
        for index in range(0, len(self.ticket_type_list)):
            print("Ticket Type:          ",     self.ticket_type_list[index].get_name())
            print("Ticket Unit Price:    ",     self.ticket_type_list[index].get_price())
            print("Ticket quantity:      ",     self.ticket_quantity_list[index])
            if len(self.ticket_type_list) > 1:
                print("             ------                ")
        print("-----------------------------------------------------")
        print("discount:              ", round(self.customer.get_discount(self.total_cost_list[0]),2))
        print("Booking fee            ", self.customer.get_booking_fee(sum(self.ticket_quantity_list)))
        print("Total cost             ", self.total_cost)

# Function to display the  all customers information
    def display_customers_information(self):
        self.record.display_customers()

# Function to display all  movies information
    def display_movie_information(self):
         self.record.display_movies()

# Function to display all ticket information   
    def display_ticket_information(self):
        self.record.display_tickets() 

# Function which allows the user to add their own movies
  
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
                        movie_index_value=len(Records.list_of_existing_movies)+1
                        movie=Movie("M{}".format(movie_index_value),movies,seat_available=50)
                        Records.list_of_existing_movies.append(movie)
                        f = open(self.movie_details_path, 'a')
                        f.write("\nM{}, {}, {}".format(movie_index_value,movies,50))
                        f.close()
                        
                        print("{} movie added".format(movies))
                    else:
                        print("Movie already exists")        
                break
            elif y_or_n == "n":
                break
            else:
                print("Please enter the valid input")
            
# Function which allows the customer to adjust the disount rate of all the reward flat customers.
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

# Function which allows the adjust rate for all step customer and before that it checks if the customer is in step customer list and allows to change the discount rate
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

    #Calling a function to display booking info 
    def display_booking_info(self):
        self.record.display_booking()
    
    # Function to display the popular movie
    def display_popular_movie(self):
        highest_purchased_movie_cost = 0
        highest_purchased_movie = ""
        for booking in Records.list_of_existing_booking:
            cost, booking_fee, discount = booking.compute_cost() 
            total_cost = cost + booking_fee - discount
            if total_cost > highest_purchased_movie_cost:
                highest_purchased_movie_cost = total_cost 
                highest_purchased_movie = booking.movie.get_name()
        
        # Displaying totatl cost and movie name of popular movie
        print("Movie Name:", highest_purchased_movie,
            "Total Cost:", highest_purchased_movie_cost)

    # Function to display all the movie records
    def display_all_records(self):
        all_records={}
        list_of_all_movies=[]
        list_of_all_ticket_type=[]
        for movie in Records.list_of_existing_movies:
            list_of_all_movies.append(movie.get_name())
        for ticket in Records.list_of_existing_ticket_types:
            list_of_all_ticket_type.append(ticket.get_name())
        for movie in list_of_all_movies:
            all_records[movie]={}
            for ticket in list_of_all_ticket_type:
                all_records[movie][ticket]=0
            all_records[movie]["Revenue"]=0  

        for booking in Records.list_of_existing_booking:
            tickets=[book.get_name() for book in booking.get_ticket()]
            qunatities = booking.get_quantity()
            for index in range(0,len(tickets)):
                all_records[booking.get_movie().get_name()][tickets[index]] += qunatities[index]
            cost, booking_fee, discount = booking.compute_cost()
            total_cost = cost+booking_fee-discount
            all_records[booking.get_movie().get_name()]["Revenue"] += total_cost
        
        header = "".join("{:<12}".format(value) for value in list_of_all_ticket_type)
        print("{:<12} {} {:<12}".format("", header,"Revenue"))
        for movie in all_records.keys():
            ticket_type_values = "".join("{:<12}".format(all_records[movie][value]) for value in list_of_all_ticket_type)
            print("{:<13} {} {:<15}".format(movie, ticket_type_values, round(all_records[movie]["Revenue"],2)))
    
    # Function to update the three test files after exit 
    def exit_program(self):
        file_c = open(self.customer_details_path, 'w')
        file_m= open(self.movie_details_path,'w')
        file_b= open("booking.txt",'w')
        for customer in Records.list_of_existing_customers:
            if Records.list_of_existing_customers[-1] == customer:
                if isinstance(customer,RewardStepCustomer):
                    file_c.write("{}, {}, {}, {}".format(customer.get_id(),customer.get_name(),customer.get_discount_rate(),customer.get_threshold())) 
                elif isinstance(customer,RewardFlatCustomer):
                    file_c.write("{}, {}, {}".format(customer.get_id(),customer.get_name(),customer.get_discount_rate()))   
                else:
                    file_c.write("{}, {}".format(customer.get_id(),customer.get_name()))
            else:
                if isinstance(customer,RewardStepCustomer):
                    file_c.write("{}, {}, {}, {}\n".format(customer.get_id(),customer.get_name(),customer.get_discount_rate(),customer.get_threshold())) 
                elif isinstance(customer,RewardFlatCustomer):
                    file_c.write("{}, {}, {}\n".format(customer.get_id(),customer.get_name(),customer.get_discount_rate()))   
                else:
                    file_c.write("{}, {}\n".format(customer.get_id(),customer.get_name()))

        for movie in Records.list_of_existing_movies:
            if movie == Records.list_of_existing_movies[-1]:
                file_m.write("{}, {}, {}".format(movie.get_id(), movie.get_name(),movie.get_seat_available()))
            else:
                file_m.write("{}, {}, {}\n".format(movie.get_id(), movie.get_name(),movie.get_seat_available()))


        for booking in Records.list_of_existing_booking:
            quantity_list = booking.get_quantity()
            ticket_list = booking.get_ticket()
            customer = booking.get_customer()
            movie = booking.get_movie()
            if booking == Records.list_of_existing_booking[-1]:
                file_b.write("{}, {}, ".format(customer.get_name(), movie.get_name()))
                for index in range(0, len(ticket_list)):
                    file_b.write("{}, {}, ".format(ticket_list[index].get_name(), quantity_list[index]))
                total_cost, booking_fee, discount = booking.compute_cost()
                file_b.write("{}, {}, {}".format(discount, booking_fee, total_cost))
            else:
                file_b.write("{}, {}, ".format(customer.get_name(), movie.get_name()))
                for index in range(0, len(ticket_list)):
                    file_b.write("{}, {}, ".format(ticket_list[index].get_name(), quantity_list[index]))
                total_cost, booking_fee, discount = booking.compute_cost()
                file_b.write("{}, {}, {}\n".format(discount, booking_fee, total_cost))

        file_c.close()
        file_b.close()
        file_m.close()
        

 # Main function
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
        customer_details_path = 'customers.txt'
        movie_details_path = 'movies.txt'
        ticket_details_path = 'tickets.txt'
        booking_details_path = 'booking.txt'
    
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
        if operation_input_type == "8":
            operation.display_booking_info()
        if operation_input_type == "9":
            operation.display_popular_movie()
        if operation_input_type == "10":
            operation.display_all_records()
        if operation_input_type == "0":
            operation.exit_program()
            break

'''My Analysis/Reflection:
The first step of any program is to read the problem statement ,
understand the requirements say inputs of the program and the expected output.
Then break the problem statement into smaller pices and try to solve it one by one.

After gathering all the requirements I started writing a code part by part .
Initailly i started with Part pass  which was just to create class and basic operations and 
perform some calculations and displaying the output.Likewise I moved on to next part. 
Part credit was initially easy with handling the errorinputs moving on we need to include group tickets for ticket types which took me a lot of time to analyze.
And moving on to distinction part where customers can purchase multiple tickets and set discount rate for all the flat and step reward customers.
I analyzed the logic and then break down into pieces and started writing code on each part which takes me a lot time to do . I used to do one part fro atleast 2 days to make sure I have not missed any specification given in the assignment.
High distinction level is little complicated with reading the files in command line. I have researched how to read the file and mention the paths to the customer object and rthen founf=d out the logic and started writing the code and achieved all the specifications.

Once the program is fully built,I noted down all the values that needs to be tested and tested all the inputs and outputs 
aacordingly.Meanwhile commented the whole program and finally wrote this analysis. '''



