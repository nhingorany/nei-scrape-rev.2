import pickle

favorite_color = pickle.load( open( "save.p", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }

print (favorite_color)
