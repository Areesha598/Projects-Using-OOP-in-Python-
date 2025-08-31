print("Cinema Ticket Booking System".center(80))

class Movie:
    def __init__(self,title,genre,duration,rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
    def showDetails(self):
        print(f"Movie {self.title} has genre {self.genre}.Movie Duration is {self.duration} and rating is {self.rating}")

class ShowTime:
    def __init__(self,movie,time,seatsAvailable):
        self.movie = movie 
        self.time = time 
        self.seatsAvailable = seatsAvailable
        self.seats = []

    def BookSeats(self,name,contactNo,seat,seatNo):
        self.seats.append((name,contactNo,seat,seatNo))
        print(f"{name} has contactNo {contactNo}.{name} get a  {seat} seat having seatNo is {seatNo}.\nYour seat Has book")
        print(self.seats)

    def cancelSeat(self,name):
       for seat in self.seats:
            if seat[0]== name:
               self.seats.remove(seat)
               print(f"{name} has cancelled their booking")
               print("Updated List is",self.seats)
            else:
               print("User is not booked seat yet")


    def ShowAvailabilty(self,Seat):
        if Seat <= 15:
            print("Seat is Available")
        else:
            print("Sorry! Seat is not Available now")


class Customer:
    def __init__(self,name,phone,email,ticketId):
        self.name = name
        self.phone = phone
        self.email = email
        self.ticketId = ticketId
        self.customr = []
    def viewProfile(self):
        print(f"{self.name} contact number is {self.phone},email is {self.email} and ticket i {self.ticketId}")
    
    def booktickt(self,name,contactNo,seat,seatNo):
        self.customr.append((name,contactNo,seat,seatNo))
        print(f"{name} has contactNo {contactNo}.{name} get a  {seat} seat having seatNo is {seatNo}.\nYour seat Has book")
        print(self.customr)
    def canceltickt(self,ticketId):
        for Id in self.customr:
            if Id[3] == ticketId:
                self.customr.remove(Id)
                print(f"Ticket {ticketId} has cancelled their booking")
                print("Updated List is",self.customr)
            else:
               print("User has not booked ticket yet")

class Admin(Customer):
    def __init__(self,name,phone,email,ticketId):
        super().__init__(name,phone,email,ticketId)
        self.Movie = []

    def addMovie(self,movie):
        
        if movie not in self.Movie:
            self.Movie.append(movie)
            print(f"{movie} Movie Added",self.Movie)
        else:
            print("Movie is Already Added")

    def removeMovie(self,movee):
        self.movee = movee
        if movee in self.Movie:
            self.Movie.remove(movee)
            print(f"{movee} has been removed from Movie List")
            print("Updated List is",self.Movie)
        else:
            print("Movie is not included in Movie List")


##TEST

admin = Admin("Saim","xxxxx","xyz@gmail.com","9975")
admin.addMovie("Dreams")
admin.addMovie("Aim")
admin.removeMovie("Aim")

print("--------------------")

st = ShowTime("Mehmood","6 PM","2")
st.BookSeats("Sehar","04236892231","MiddleSeat",8854)
st.BookSeats("Sana","04238973311","Front Seat",9976)
st.cancelSeat("EYe")
st.cancelSeat("Sana")
st.ShowAvailabilty(6)
st.ShowAvailabilty(23)

print("--------------------")

cust = Customer("Taha","09964278568","abc@gmail.com","4")
cust.booktickt("Taha","09964278568","abc@gmail.com","4")
cust.booktickt("Wahaj","09964278568","abc@gmail.com","66")
cust.canceltickt("99")
cust.canceltickt("4")
