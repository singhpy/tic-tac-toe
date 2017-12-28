"""
Player Package to manage Player Information.

This module contains player class and related methods to manage
player

This will by default creates __name__,  __doc__ , __package__, __loader__
__spec__, __file__, __cached__, __builtins__  -- use __dict__ to see this

"""
import sqlite3
__version__ = "1.0.0"

# player_file = open(r"..\database\foxy_player.txt", "r")


class Player():

    """ Player Class to create players

    Class name should normally use the CapWords convention.
    This class defines method to initalize player record
    It can be extended to create Person.

    This will by default creates __dict__ , __module__, __doc__ & __weakref__

    """
    class_variable = "Class Variable"

    def __init__(self, **kwargs):
        """ Initialize Player DB name """

        self._player_db_name = "tictactoe_player"
        print("Player : __init__ called Player DB is  " + self._player_db_name)

        """ Initialize Player Fields """
        if len(kwargs) == 0:
            pass
        else:
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.gender = kwargs["gender"]
            self.address = kwargs["address"]

    def __add__(self):
        pass

    def get_player_id(self):
        return 1111

    def add_player(self):
        """
        Function to add new players.
        :return:
        """
        
        print("-------- Validating Data   ------" + self.name + " " + str(self.age) +
              " " + self.gender + " " + str(self.address))
        if not isinstance(self.age, int):
            print("Invalid Age : Must enter a number")
            return 1,"Player Creation : Failed!"
        if str(self.gender).upper() not in ["F", "M"]:
            print("Invalid Sex : Must enter F or M")
            return 1,"Player Creation : Failed!"
        # if len(self.address) != 3:
        #   print("Invalid Address : Must enter Street, City, State")
        #   return 1,"Player Creation : Failed!"

        print("--------Adding Player ------")
        _cust_id = Player.get_player_id(self)

        conn = sqlite3.connect(r'C:\Users\vinvins\AppData\Local\Programs\Python\Python36-32\player_sql3_db.db')
        cur = conn.cursor()
        player_record = (self.name, self.age, self.gender, self.address,)



        # insert player record
        cur.execute("INSERT INTO player VALUES (?,?,?,?)", player_record)
        # or
        # cur.execute("INSERT INTO player VALUES (:name ,:age ,:gender ,:address)", {'name':self.name, 'age':self.age, 'gender':self.gender, 'address':self.address})

        conn.commit()
        conn.close()


         # player_record = json.dumps({'Player Id': _cust_id, 'Name': self.name,
         #                             'Age': self.age, 'Sex': self.gender, 'Address': self.address})






        print("--------Player Created------" + str(_cust_id))
        return 0, "Player Created Successfully!"

"""
class Employee(Player):
    
    Employee Class extends player and implements new fields
    to define employees
    
    def __init__(self, **kwargs):
        super(Employee, self).__init__(**kwargs)
        self.empid = kwargs["empid"]

    def __str__(self):  # when a instance calls str() or print()
        return "STR: CUSTOMER MANAGEMENT - Player " + self.name + "  " + self.empid
"""

if __name__ == "__main__":
    print("Player is called Directly - Drawing screen to capture details")
    c1 = Player(name='vinay', age=40, gender='M', address="631 E Royal Lane Irving Texas")
    c1.add_player()


"""
    # def __str__(self):  # when a instance calls str() or print()
    #    return "STR: CUSTOMER MANAGEMENT - Player " + self.name

    # def __repr__(self):  # when a instance calls str() or print()
    #   return "REPR: CUSTOMER MANAGEMENT - Player " + self.name

    def get_player_id(self):
        return 1111

    def __iter__(self):
        return self

    def __next__(self):
        print(" read output " + player_file.readline())
        if player_file.readline() == "":
            raise StopIteration
        return player_file.readline()

    def read_player(self):
        pass
"""