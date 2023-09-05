def  padel_court_cost(court_type):
    if court_type == "indoor" :
       return 30
    
    
    elif court_type == "outdoor":
         return 20




def rackets_cost(racket_brand):
    if racket_brand == "bullpade":
       return 100
    
    elif rackets_cost == "Nox" :
        return 140
    
    elif  rackets_cost == "Siux" :
       return 200




def padel_ball_cost(ball_boxes):
    if ball_boxes == 1 :
        cost = 2
    
    elif ball_boxes == 2:
       
       cost = 3.5
    
    elif ball_boxes == 3:
        
        cost =  5 
    
   
def padel_game_cost():
    
     court_type = input("court type indoor / outdoor")
     rackets_brand = input("racket_brand : nox / sulux / bullpade")
     ball_boxes = int(input("number of ball boxes: 1 / 2 / 3"))
     print = padel_court_cost(court_type) + rackets_cost(rackets_brand) + padel_ball_cost(ball_boxes)
     return print

print(padel_game_cost())


   


