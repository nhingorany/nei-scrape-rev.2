# Function definition is here
def suma( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Now you can call sum function
total = suma( 10, 20 )
print ("Outside the function : ", total )


def bouy (weight, area):
    buyreq = weight * area
    print ('1000 tank :' , buyreq)
    return buyreq

buyreq = bouy ( 1000, 50)
print ('1500 tank:' , buyreq)


buyreq = bouy ( 1100, 40)
print ('1600 tank:' , buyreq)

