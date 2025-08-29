print("HOSPITAL MANAGMENT SYSTEM".center(80))

class Person:
    def __init__(self):
        pass 

class Doctor(Person):
    def __init__(self,name,specilization,doctorID,avalibility,schedule):
        self.name = name
        self.specilization  = specilization
        self.doctorID = doctorID
        self.avalibility = avalibility
     
        self.patients = []
        self.schedule = []

    def assignPatient(self,Patientname):
        self.Patientname = Patientname
        self.patients.append(self.Patientname)
        print(f"Patients {self.patients} is assigned to Dr.{self.name}.")


    def addAppointment(self,Patientname,date,time):
        self.schedule.append((Patientname,date,time))
        print(f"New Schedule is {Patientname} on date {date} at {time} for Dr.{self.name}")


    def ViewSchedule(self):
        if not  self.schedule:
            print(f"Dr.{self.name} has no appointment yet")
        else:
            print(f"Schedule of Dr.{self.name} is:")
            for p,d,t in self.schedule:
              print(f"Patient {p}  has appointment on date {d} at time {t}")

    def display(self):
        print(f"{self.patients} is  the Patients of Dr.{self.name}.New patients that took appointment are:\n {self.schedule}")


class Patients(Person):
    def __init__(self,Drname):
        self.Drname = Drname
        self.appointment = []
        self.prescription = []
        

    def book_appointment(self,name,contactNo):
        self.appointment.append((name,contactNo))
        print(f"New Patient that Book Appointment is {self.appointment}")
    def checkAppointment(self):
        if not self.appointment:
            print("Not Appointment Yet")
        else:
            print("Your Appointment is here:")
            for n,co in self.appointment:
                print(f"Patient Name is {n} and Contact Number is {co}")
    def show(self):
        print(f"Dr.{self.Drname} has appointments {self.appointment}.")

    def Prescription(self,name,medicines):
        self.name = name
        self.prescription.append((name,medicines))
        print(f"Patient:{name},Medicine:{medicines}")
    def viewPrescription(self):
        if not self.prescription:
            print("No Prescription Added")
        else:
            print(f"Prescription For {self.name}:")
            
            for med in self.prescription:
                print("Medicine is:",med)



class Appointment:
    def __init__(self,name):
        self.name = name
        self.patients = []   #
        self.schedule = []   
    def appoint(self,pname,date,time):
        self.schedule.append((pname,date,time))
        if pname not in self.patients:
           self.patients.append(pname)

        print(f"New Appointment Schedule.Patient Name {pname} on {date} at {time}")

    def viewAppoint(self):
        if not self.schedule:
            print(f"Dr.{self.name} has not Scheduled yet.")
        else:
            print(f"Schedule of Dr.{self.name} is:")
            for p,d,t in self.schedule:
              print(f"Patient {p}  has appointment on date {d} at time {t}")

    def CancelAppoint(self,pt):
        if pt in self.patients:
            self.patients.remove(pt)
            self.schedule = [s for s in self.schedule if s[0] != pt]
            print(f"Patient {pt} has been removed from Dr.{self.name} appointment list")
        else:
            print("No Patient Found")

print("::Testing Starts::".center(80))

dr = Doctor("Taha","Pyscologist",8823,"8 AM","No")
dr.assignPatient("ABC")
dr.addAppointment("XYZ","22 February","10 AM")
dr.ViewSchedule()
dr.display()
print("-----------------")

pat = Patients("Seerat")
pat.book_appointment("Sehar","03216692132")
pat.checkAppointment()
pat.show()
# pat.Prescription("Sehar","\n1.Panadol\n2.Calpol")
pat.Prescription("Sehar","Panadol,Calpol")
pat.viewPrescription()
print("-----------------")

appoin = Appointment("Ishrat")
appoin.appoint("Seerat","9 July","8 PM")
appoin.appoint("Taha","12 October","10 AM")
appoin.CancelAppoint("ABC")
appoin.CancelAppoint("Seerat")
print("-----------------")

print("Programm Ended")
