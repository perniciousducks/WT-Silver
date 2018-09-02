label __init_variables:
    python:
        selectcard = -1
        cardzoom = 0.1
        
        table_cards = [[None for x in range(0,3)] for y in range(0,3)] 
        
        card_width = get_witdh("images/cardgame/cheerl.png")
        card_height = get_height("images/cardgame/cheerl.png")
        
        playerboarder = playerTint("images/cardgame/sides.png")
        enemyboarder = enemyTint("images/cardgame/sides.png")
        
        
        
        hermione_cheer1 = card()
        hermione_cheer2 = card()
        hermione_cheer3 = card()
        hermione_cheer4 = card()
        hermione_cheer5 = card()
        hermione_cheer_en1 = card(playercard=False)
        hermione_cheer_en2 = card(playercard=False)
        hermione_cheer_en3 = card(playercard=False)
        hermione_cheer_en4 = card(playercard=False)
        hermione_cheer_en5 = card(playercard=False)
        
        playerdeck = [hermione_cheer1, hermione_cheer2,hermione_cheer3,hermione_cheer4,hermione_cheer5]
        enemydeck = [hermione_cheer_en1 ,hermione_cheer_en2 ,hermione_cheer_en3,hermione_cheer_en4,hermione_cheer_en5]
        
        
init python:
    
    
    def playerTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0))
    def enemyTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(1, 0.5, 0.5))
        
    def get_witdh(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]
        
        return x
        
    def reset_table_cards():
        table_cards = [[None for x in range(0,2)] for y in range(0,2)] 
        return
    def check_winner():
        playerpoints = 0
        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y].playercard:
                    playerpoints += 1
        return playerpoints > 4
           
    def update_table(new_card_x, new_card_y):
        if  not new_card_y == 0 and not table_cards[x][y-1] == None and table_cards[x][y].topvalue >= table_cards[x][y-1].buttomvalue:
            table_cards[x][y-1].playercard = table_cards[x][y].playercard
            
        if not new_card_y == 2 and not table_cards[x][y+1] == None and table_cards[x][y].buttomvalue >= table_cards[x][y+1].topvalue:
            table_cards[x][y+1].playercard = table_cards[x][y].playercard
            
        if  not new_card_x == 0 and not table_cards[x-1][y] == None and table_cards[x][y].leftvalue >= table_cards[x-1][y].rightvalue:
            table_cards[x-1][y].playercard = table_cards[x][y].playercard
            
        if not new_card_x == 2 and not table_cards[x+1][y] == None and table_cards[x][y].rightvalue >= table_cards[x+1][y].leftvalue:
            table_cards[x+1][y+1].playercard = table_cards[x][y].playercard
            
    def get_height(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]
        
        return y
    
    class card(object):
        playercard = True
        imagepath = "images/cardgame/cheerl.png"
        cardimage = None
        cardimagehover = None
        
        topvalue = 0
        buttomvalue = 1
        rightvalue = 2
        leftvalue = 3
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            self.cardimage = im.Scale(self.imagepath, card_width*cardzoom, card_height*cardzoom)
            self.cardimagehover = im.MatrixColor(self.cardimage,im.matrix.brightness(0.12))
            
        def getAIScore(self, table_of_cards):
            high_score = 0
            position = 0
            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if  not y == 0:
                            score += self.topvalue
                        if not y == 2:
                            score += self.buttomvalue
                        if  not x == 0:
                            score += self.leftvalue
                        if not x == 2:
                            score += self.rightvalue
                            
                        if score > high_score:
                            high_score = score
                            position = x + y * 3
            return [high_score, position]