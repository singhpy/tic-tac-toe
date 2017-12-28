"""
Player Package to manage Player Information.

This module contains player class and related methods to manage
player and employee.

This will by default creates __name__,  __doc__ , __package__, __loader__
__spec__, __file__, __cached__, __builtins__  -- use __dict__ to see this

"""
import file_actions
import json
import dir1.classtools
__version__ = "1.0.0"

customer_file = open(r"..\database\foxy_customer.txt", "r")


class Player(dir1.classtools.AttrDisplay):

    """ Customer Class to create customers

    Class name should normally use the CapWords convention.
    This class defines method to initalize customer record
    It can be extended to create Employee.

    This will by default creates __dict__ , __module__, __doc__ & __weakref__

    """
    class_variable = "Class Variable"

    def __init__(self, **kwargs):
        """Initalize Customer File Name """

        self._customer_file_name = "foxy_customer"
        print("customer : Customer : __init__ called Customer File is  " + self._customer_file_name)
        print("Class Variable is accessible in method using self " + self.class_variable)

        """ Initialize Customer Fields """
        if len(kwargs) == 0:
            pass
        else:
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.sex = kwargs["sex"]
            self.address = kwargs["address"]

    def __add__(self):
        pass

    # def __str__(self):  # when a instance calls str() or print()
    #    return "STR: CUSTOMER MANAGEMENT - Customer " + self.name

    # def __repr__(self):  # when a instance calls str() or print()
    #   return "REPR: CUSTOMER MANAGEMENT - Customer " + self.name

    def get_customer_id(self):
        return 1111

    def __iter__(self):
        return self

    def __next__(self):
        print(" read output " + customer_file.readline())
        if customer_file.readline() == "":
            raise StopIteration
        return customer_file.readline()

    def read_customer(self):
        pass


    def add_customer(self):
        """
        Function to add new customers.
        :return:
        """
        print("-------- Validating Data   ------" + self.name + " " + str(self.age) +
              " " + self.sex + " " + str(self.address))
        if not isinstance(self.age, int):
            print("Invalid Age : Must enter a number")
            return 1,"Customer Creation : Failed!"
        if str(self.sex).upper() not in ["F", "M"]:
            print("Invalid Sex : Must enter F or M")
            return 1,"Customer Creation : Failed!"
        if len(self.address) != 3:
            print("Invalid Address : Must enter Street, City, State")
            return 1,"Customer Creation : Failed!"

        print("--------Adding Customer ------")
        _cust_id = Customer.get_customer_id(self)
        customer_record = json.dumps({'Customer Id': _cust_id, 'Name': self.name,
                                      'Age': self.age, 'Sex': self.sex, 'Address': self.address})
        file_actions.FileAction().fa_openw(self._customer_file_name, customer_record)
        print("--------Customer Created------" + str(_cust_id))
        return 0, "Customer Created Successfully!"


class Employee(Customer):
    """
    Employee Class extends customer and implements new fields
    to define employees
    """
    def __init__(self, **kwargs):
        super(Employee, self).__init__(**kwargs)
        self.empid = kwargs["empid"]

    def __str__(self):  # when a instance calls str() or print()
        return "STR: CUSTOMER MANAGEMENT - Customer " + self.name + "  " + self.empid


if __name__ == "__main__":
    print("Customer is called Directly")
    c1 = Customer(name='vinay', age=40, sex='M', address=["631 E Royal Lane", "Irving", "Texas"])
    c1.add_customer()
