#TODO: Remeber to move code into the out comment code
label __init_variables:
    python:
        selectcard = -1
        selectenemycard = -1
        currentpage = 0

        if not hasattr(renpy.store,'playercolor_r'):
            playercolor_r = 51.0/255.0
            playercolor_g = 92.0/255.0
            playercolor_b = 147.0/255.0
            enemycolor_r = 116.0/255.0
            enemycolor_g = 0
            enemycolor_b = 0
            geniecard_level = 1

        table_cards = [[None for x in range(0,3)] for y in range(0,3)]

        card_width = get_width("images/cardgame/border.png")
        card_height = get_height("images/cardgame/border.png")

        playerborder = playerTint("images/cardgame/border.png")
        enemyborder = enemyTint("images/cardgame/border.png")

        #Special Cards

        genie = card_new( imagepath="images/cardgame/t1/special/genie_v1.png",
                                    topvalue = 5,
                                    bottomvalue = 4,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Genie")

        santa = card_new( imagepath="images/cardgame/t1/special/santa_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="Santa Genie")

        snape = card_new( imagepath="images/cardgame/t1/special/snape_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 1,
                                    rightvalue = 4,
                                    leftvalue = 5,
                                    title="Severus Snape")

        dumbledore = card_new( imagepath="images/cardgame/t1/special/dumbledore_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="Albus Dumbledore")

        fred = card_new( imagepath="images/cardgame/t1/special/fred_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="Fred Weasley")

        george = card_new( imagepath="images/cardgame/t1/special/george_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="George Weasley")

        #Tier 1 cards

        her_schoolgirl = card_new( imagepath="images/cardgame/t1/hermione/her_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 4,
                                    bottomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 1,
                                    title="Hermione Granger (schoolgirl)")

        sus_schoolgirl = card_new( imagepath="images/cardgame/t1/susan/sus_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 3,
                                    bottomvalue = 4,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Susan Bones (schoolgirl)")

        cho_schoolgirl = card_new( imagepath="images/cardgame/t1/cho/cho_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 3,
                                    bottomvalue = 1,
                                    rightvalue = 2,
                                    leftvalue = 4,
                                    title="Cho Chang (schoolgirl)")

        lun_schoolgirl = card_new( imagepath="images/cardgame/t1/luna/lun_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 3,
                                    bottomvalue = 1,
                                    rightvalue = 2,
                                    leftvalue = 4,
                                    title="Luna Lovegood (schoolgirl)")

        #Item cards

        item_badge = card_new( imagepath="images/cardgame/t1/other/badge_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="SPEW Badge")

        item_barbell = card_new( imagepath="images/cardgame/t1/other/barbell_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Barbell piercing")

        item_beads = card_new( imagepath="images/cardgame/t1/other/beads_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Anal beads")

        item_bird = card_new( imagepath="images/cardgame/t1/other/bird_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Phoenix")

        item_bookchairs = card_new( imagepath="images/cardgame/t1/other/bookchairs_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Book of Chairs")

        item_bookgala = card_new( imagepath="images/cardgame/t1/other/bookgala_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Book of Galadrier (Light ED)")

        item_bookgala2 = card_new( imagepath="images/cardgame/t1/other/bookgala2_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Book of Galadriel (Hardcore ED)")

        item_bookwaifu = card_new( imagepath="images/cardgame/t1/other/bookwaifu_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Waifu Book")

        item_broom = card_new( imagepath="images/cardgame/t1/other/broom_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Modified Nimbus 2000")

        item_bdsm = card_new( imagepath="images/cardgame/t1/other/bdsm_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="BDSM Kit")

        item_condoms = card_new( imagepath="images/cardgame/t1/other/condoms_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Pack of condoms")

        item_desk = card_new( imagepath="images/cardgame/t1/other/desk_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Office desk")

        item_dildo = card_new( imagepath="images/cardgame/t1/other/dildo_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Magical Dildo")

        item_doll = card_new( imagepath="images/cardgame/t1/other/doll_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Sex Doll")

        item_elf = card_new( imagepath="images/cardgame/t1/other/elf_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="House-Elf")

        item_eromag = card_new( imagepath="images/cardgame/t1/other/eromag_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Erotic Magazine")

        item_girlmag = card_new( imagepath="images/cardgame/t1/other/girlmag_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Girly Magazine")

        item_hat = card_new( imagepath="images/cardgame/t1/other/hat_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Sorting Hat")

        item_lingerie = card_new( imagepath="images/cardgame/t1/other/lingerie_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Lingerie")

        item_lipstick = card_new( imagepath="images/cardgame/t1/other/lipstick_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Lipstick (Red)")

        item_lube = card_new( imagepath="images/cardgame/t1/other/lube_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Jar of lubricant")

        item_owl = card_new( imagepath="images/cardgame/t1/other/owl_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Stuffed Owl")

        item_plugs = card_new( imagepath="images/cardgame/t1/other/plugs_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Set of anal plugs")

        item_pornmag = card_new( imagepath="images/cardgame/t1/other/pornmag_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Porno Magazine")

        item_potions = card_new( imagepath="images/cardgame/t1/other/potions_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Batch of Potions")

        item_scroll = card_new( imagepath="images/cardgame/t1/other/scroll_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Forbidden Scroll")

        item_stockings = card_new( imagepath="images/cardgame/t1/other/stockings_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Pair of stockings")

        item_strapon = card_new( imagepath="images/cardgame/t1/other/strapon_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Thestral Strapon")

        item_sweets = card_new( imagepath="images/cardgame/t1/other/sweets_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Pack of Sweets")

        item_wine = card_new( imagepath="images/cardgame/t1/other/wine_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Bottle of wine")

        if not hasattr(renpy.store,'deck_unlocked'):
            deck_unlocked = False
            deck_mail_send = False
            enemy_deck = []
            duel_win_label = ""
            duel_loss_label = ""

        if not hasattr(renpy.store,'snape_know_cards'):
            #Snape
            snape_know_cards = False
            snape_first_win = False
            snape_second_win = False
            snape_third_win = False
            #Hermione
        if not hasattr(renpy.store, 'her_know_cards'):
            her_know_cards = False
            her_first_win = False
            her_second_win = False
            her_third_win = False
            #Twins
        if not hasattr(renpy.store, 'twins_know_cards'):
            twins_know_cards = False
            twins_first_win = False
            twins_second_win = False
            twins_third_win = False
            twins_cards_delay = 7
            twins_cards_stocked = False

        if not hasattr(renpy.store,'unlocked_cards'):
            unlocked_cards = [genie, her_schoolgirl, sus_schoolgirl, lun_schoolgirl, dumbledore]

        if not hasattr(renpy.store,'playerdeck'):
            playerdeck = [genie, her_schoolgirl, sus_schoolgirl, lun_schoolgirl, dumbledore]

        if not hasattr(renpy.store,'snape_first_deck'):
            snape_first_deck = [snape.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]
            snape_second_deck = [snape.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]
            snape_third_deck = [snape.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]

        if not hasattr(renpy.store,'twins_first_deck'):
            twins_first_deck = [fred.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]
            twins_second_deck = [george.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]
            twins_third_deck = [fred.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]

        if not hasattr(renpy.store,'her_first_deck'):
            her_first_deck = [her_schoolgirl.clone(), item_dildo.clone(), item_doll.clone(), item_condoms.clone(), item_strapon.clone()]
            her_second_deck = [george.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]
            her_third_deck = [fred.clone(), item_wine.clone(), item_elf.clone(), item_sweets.clone(), item_lipstick.clone()]

        card_non_spec_char = [ "I see you've been practicing... so have I!", "You've activated my trap card... wait... it's in my other deck!", "You think you're so good, but this school has never seen a player of the likes of me! In this particular office...", "Aha, you've walked right into my trap. Take this!", "You'll never beat me! I will give you the reward though... in your dreams!", "Thats impossible... that card is legendary... wait, it doesn't have a shimmering effect, never mind.", "I was sure my cards used to be good...", "Wait, you've got that card... I've been such a fool! This is a witchmasters deck!", "We're playing reverse rules right? Lowest amount of cards win?", "If only slight of hand was taught at Hogwarts...", "Wait, this can't be right. I must have put my good cards in my other robes.", "You should be happy that they banned one of the cards that came in a cereal box promotion... that one was overpowered.", "This one's a board sweeper!", "I'll just burn this card... oh yeah, I got better cards coming.", "This is a control deck. I'll win in the end don't you worry.", "Maybe I should have made less of a filler deck... I'll get you in the end.", "Your loss is inevitable. It's all in the heart of the cards.", "Have you been Netdecking? Did those damn spiders in the forest tell you what cards to play?", "I've been metagaming the crap out of you... I know exactly what cards you're going to play...except for that last one.", "Oh, it's my turn? I was just thinking about how I'm going to celebrate after your inevitable loss.", "I've been slowrolling you this whole time. My last card is a mega ultimate legendary.", "What kind of deck is this... don't you even care about synergy?", "I see what kind of player you are now... perhaps a more offensive approach is in order.", "I was born to play card games... you merely adopted your liking of them.", "Hahah, you don't even know that I have a card with powers that has been locked away for centuries... unfortunately I lost the key...", "Prepare for a total wipe... your tears when I beat you that is.", "You want to know what's shown on my cards? What do I like the most? Winning, which is why this card is going to guarantee my victory.", "Life is like a game of Wizard Cards. If you don't win... you lose.", "Quitters never win, winners never quit, but those who never win and never quit are idiots... I'm not sure which I am.", "Go fish...", "Do you have any spells to make you better at Wizard Cards? Didn't think so...", "You can smell the roses as much as you want, while I smell the aroma of victory", "Do you see any stars yet, because you're getting beaten pretty badly.", "Well, your performance in this round is certainly a divine comedy.", "The forecast today is calling for my victory, so I'm not worried.", "Are you out of juice already?", "Couldn't you see from your own fortune that you're bound to lose?", "Looks like you fell right into your own trap... now look at this!! KAPOW", "I don't need luck potion to beat you. That's how confident I am in my deck.", "I know my deck like the back of my hand... wait, when did that mole get there?", "Fool, you'll soon see my finishing move... but before that, UNO!", "I'm so confident in my card collection I just shuffled and picked some at random before this game.", "Great cards doesn’t ensure a win. Right moves do.", "The game balance of this game has been broken for centuries... and I have the winning cards.", "The ministry of magic considered banning this game as they thought it all mattered what cards you had... something about gambling for children.", "If I said that I picked my cards blindfolded would you believe me? Yes, they're all that good.", "I tried to use transfiguration on one of my cards but it burnt up instead... I probably wasn't the first one who tried that.", "Wait! Isn't that card banned? No, the stats aren't the same...phew", "Why does that card of yours look so sticky?", "Oh nice a shiny... wait, why has it stuck to the board?", "That's nowhere near the best move you could've done. Check this out!", "Even a troll would play better than you at this point... no offense.", "Some people are half blood and some pure blood. But I'm purely a Card playing genius.", "That must be a new card. Why haven't I seen that one before?", "Wait, my numbers must have changed. Did you put a spell on my cards?", "Hit me... I mean, give me another card.", "Ah, that one. To bad I have the perfect counter.", "So, when do I get to draw a card again?", "Someone replaced one of my cards with a joker... I bet it was peeves.", "I was told that face cards was the best ones to get... but they were talking about poker.", "By Merlins beard, where did you get that card?", "Next time you should let me use the cards I drew. Their numbers are a lot better than these ones."]

        snape_speach_card = ["You may have lived for hundreds of years but my superior intellect will outweigh your otherworldly powers.", "When this is over I think I'll celebrate my victory with one of your nice bottles of alcohol.", "You should stick to charming women... wizard cards is my game.", "You said you were from a different world, another reality? Maybe in that reality you'd beat me at cards. But not this one!", "We don't stop playing because we grow old, we grow old because we stop playing.", "Where did you even find your trash cards? In a promotional pamphlet?", "Why are my cards so much greasier than yours?"] + card_non_spec_char


init python:

    def playerTint(image):
        return im.MatrixColor( image, im.matrix.tint(playercolor_r, playercolor_g, playercolor_b))
    def enemyTint(image):
        return im.MatrixColor( image, im.matrix.tint(enemycolor_r, enemycolor_g, enemycolor_b))

    def get_image_size(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        return (x,y)

    def get_hex_string(red, green, blue):
        red = str(hex( int( math.ceil( red*255))))[2:]
        if not len(red) == 2:
            red = "0"+red
        green = str(hex(int(math.ceil( green * 255))))[2:]
        if not len(green) == 2:
            green = "0"+green
        blue = str(hex(int(math.ceil( blue * 255))))[2:]
        if not len(blue) == 2:
            blue = "0"+blue
        return "#" + red + green + blue

    def get_width(image):
        return get_image_size(image)[0]

    def get_height(image):
        return get_image_size(image)[1]

    def reset_table_cards():
        for y in range(0,3):
            for x in range(0,3):
                table_cards[x][y] = None
        return

    def check_winner():
        playerpoints = len(player_deck)

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y].playercard:
                    playerpoints += 1
        return playerpoints > 5


    def update_table(new_card_x, new_card_y):
        if  not new_card_y == 0 and not table_cards[x][y-1] == None and table_cards[x][y].topvalue > table_cards[x][y-1].bottomvalue:
            table_cards[x][y-1].playercard = table_cards[x][y].playercard

        if not new_card_y == 2 and not table_cards[x][y+1] == None and table_cards[x][y].bottomvalue > table_cards[x][y+1].topvalue:
            table_cards[x][y+1].playercard = table_cards[x][y].playercard

        if  not new_card_x == 0 and not table_cards[x-1][y] == None and table_cards[x][y].leftvalue > table_cards[x-1][y].rightvalue:
            table_cards[x-1][y].playercard = table_cards[x][y].playercard

        if not new_card_x == 2 and not table_cards[x+1][y] == None and table_cards[x][y].rightvalue > table_cards[x+1][y].leftvalue:
            table_cards[x+1][y].playercard = table_cards[x][y].playercard

    def add_card_to_deck(title):
            for card in unlocked_cards:
                if title == card.title:
                    card.copies += 1

    class card_new(object):
        playercard = True
        textcolor = "{color=#ffffff}"
        copies = 0
        description = "She will cheer for you all the way up the wand"
        title = "Cheerleader BaseCard"
        imagepath = "images/cardgame/h_lewd_cheer.png"

        topvalue = 0
        bottomvalue = 1
        rightvalue = 2
        leftvalue = 3

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_card_image(self, zoom=0.5):
            return im.Scale(self.imagepath, card_width*zoom, card_height*zoom)
        def get_card_hover(self, zoom=0.5):
            return im.MatrixColor(im.Scale(self.imagepath, card_width*zoom, card_height*zoom),im.matrix.brightness(0.12))

        def get_title(self):
            return self.textcolor+self.title+"{/color}"
        def get_amount(self):
            return self.textcolor+"amount: " + str(self.copies)+"{/color}"
        def get_totalvalue(self):
            return self.textcolor+str(self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue)+"{/color}"
        def get_description(self):
            return self.textcolor+self.description+"{/color}"

        def clone(self):
            return card_new(title = self.title,imagepath=self.imagepath, topvalue=self.topvalue, bottomvalue=self.bottomvalue, rightvalue=self.rightvalue, leftvalue=self.leftvalue)

        def getAIScore(self, table_of_cards):
            high_score = 0
            position = 0
            wallscore = 2
            getcardscore = 9
            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if  not y == 0:
                            if not table_cards[x][y-1] == None and self.topvalue > table_cards[x][y-1].bottomvalue:
                                score += getcardscore
                            else:
                                score += self.topvalue
                        else:
                            score += wallscore
                        if not y == 2:
                            if not table_cards[x][y+1] == None and self.bottomvalue > table_cards[x][y+1].topvalue:
                                score += getcardscore
                            else:
                                score += self.bottomvalue
                        else:
                            score += wallscore
                        if  not x == 0:
                            if not table_cards[x-1][y] == None and self.leftvalue > table_cards[x-1][y].rightvalue:
                                score += getcardscore
                            else:
                                score += self.leftvalue
                        else:
                            score += wallscore
                        if not x == 2:
                            if not table_cards[x+1][y] == None and self.rightvalue > table_cards[x+1][y].leftvalue:
                                score += getcardscore
                            else:
                                score += self.rightvalue
                        else:
                            score += wallscore

                        if score > high_score:
                            high_score = score
                            position = x + y * 3
            return [high_score, position]
