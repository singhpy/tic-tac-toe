class Customer:
    COMPANY="GENERATIONV"

    def __init__(self, name, age):
        self.name=name
        self.age=age

    @classmethod
    def customer_func(cls):
        print("This is Customer Func")
        cust_func="Customer Function"

    def customer_full(self):
        self.cust_full = self.name + Customer.COMPANY
        return self.cust_full


"""
run this first
then create c1 instance and 

with open("save.pkl","ab") as sp:
	pickle.dump(Customer,sp)
	
with open("save.pkl","ab") as sp:
	pickle.dump(c1,sp)
	
		
			
restart the shell

and create the Customer again

	with open("save.pkl","rb") as rp:
	print(pickle.load(rp))
	print(pickle.load(rp))
	print(pickle.load(rp))
	c1 = pickle.load(rp)
	
	you can access
	
	c1.customer_full()
	
	
	


"""