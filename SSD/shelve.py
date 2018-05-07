import shelve

import shelve



s = shelve.open("mydata.dat") 
s["name"]= ["Mohit", "Ravi","Bhaskar"] 
s["skill"]= ["Python", "Java","java"] 
s["age"]= [27,25,25] 
s.close() 


