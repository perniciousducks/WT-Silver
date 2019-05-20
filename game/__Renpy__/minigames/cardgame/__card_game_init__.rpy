label __init_variables:
    python:
        selectcard = -1
        selectenemycard = -1
        currentpage = 0
        #Shown Cards is a interger for how many cards should be hidden
        #
        #Sudden Death is where when there is draw then a new round will begin
        #Where you take all card of you color up in you hand
        #
        #Reverse is where the take over is reverse so instead of > it is <
        #
        #Dobelt_number
        # Rules(Shown Cards, Sudden Death, Reverse, Dobelt_number)
        standard_rules = [0, False, False, False]
        
        if not hasattr(renpy.store,'playercolor_rgb'):
            playercolor_rgb = [51.0, 92.0, 147.0, 255.0]
            enemycolor_rgb = [116.0, 0, 0, 255.0]
        
        if not hasattr(renpy.store, 'geniecard_level'):
            geniecard_level = 1
            geniecard_tokens = 0
            cardgame_eoc = False # End of content flag
        
        table_cards = [[None for x in range(0,3)] for y in range(0,3)] 
        
        card_width = get_width("images/cardgame/border.png")
        card_height = get_height("images/cardgame/border.png")
        
        playerborder = playerTint("images/cardgame/border.png")
        enemyborder = enemyTint("images/cardgame/border.png")
        
        # Used in deckbuilder, DONT DELETE!
        card_empty = card_new( imagepath="images/cardgame/border.png",
                                    topvalue = 0,
                                    bottomvalue = 0,
                                    rightvalue = 0,
                                    leftvalue = 0,
                                    title="Dummy",
                                    description="Dummy")
        
        #Special Cards
        
        card_genie = card_new( imagepath="images/cardgame/t1/special/genie_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 3,
                                    title="Genie",
                                    description = "It's you, looking sexy as fuck. As always.")
          
        card_snape = card_new( imagepath="images/cardgame/t1/special/snape_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 1,
                                    rightvalue = 4,
                                    leftvalue = 2,
                                    title="Severus Snape",
                                    description = "The potions master at Hogwarts. Known to many by his slithering walk and greasy appearance.")
                                    
        card_dumbledore = card_new( imagepath="images/cardgame/t1/special/dumbledore_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 1,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="Albus Dumbledore",
                                    description = "Some old dude, you have no idea who this is.")
                                    
        card_fred = card_new( imagepath="images/cardgame/t1/special/fred_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 4,
                                    leftvalue = 1,
                                    title="Fred Weasley",
                                    description = "One of the Weasley twins, I think it might be George.")
                                    
        card_george = card_new( imagepath="images/cardgame/t1/special/george_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 4,
                                    title="George Weasley",
                                    description = "One of the Weasley twins, I think it might be Fred.")

        #Special Cards - Alternative
                                    
        card_jasmine = card_new( imagepath="images/cardgame/t1/genie_realm/jas_v%s.png" % str(geniecard_level),
                                    topvalue = 2,
                                    bottomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 4,
                                    title="Princess Jasmine",
                                    description = "One of your favourite sluts, I mean, princesses.")
                                    
        card_iris = card_new( imagepath="images/cardgame/t1/genie_realm/iri_v%s.png" % str(geniecard_level),
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 4,
                                    leftvalue = 2,
                                    title="Iris",
                                    description = "Your most devoted fangirl.")
                                    
        card_azalea = card_new( imagepath="images/cardgame/t1/genie_realm/azalea_v%s.png" % str(geniecard_level),
                                    topvalue = 4,
                                    bottomvalue = 2,
                                    rightvalue = 2,
                                    leftvalue = 3,
                                    title="Azalea",
                                    description = "Your dreamgirl.")
                                    
        card_dahlia = card_new( imagepath="images/cardgame/t1/genie_realm/dahlia_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Dahlia",
                                    description = "She's very (s)experienced.")
                                    
        card_aladdin = card_new( imagepath="images/cardgame/t1/genie_realm/aladdin_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 4,
                                    title="Aladdin",
                                    description = "The biggest cuck in the whole multiverse.")
                                    
        card_lilly = card_new( imagepath="images/cardgame/t1/genie_realm/lilly_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 5,
                                    rightvalue = 5,
                                    leftvalue = 5,
                                    title="Lilly",
                                    description = "Whos your momma?")
                                    
        card_maslab = card_new( imagepath="images/cardgame/t1/genie_realm/maslab_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 3,
                                    rightvalue = 4,
                                    leftvalue = 4,
                                    title="Maslab",
                                    description = "\"If you hurt my precious daughter I'll find you!\"")
                                    
        card_rasul = card_new( imagepath="images/cardgame/t1/genie_realm/rasul_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 2,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="Rasul",
                                    description = "Loyalty has its price.")
                                    
        card_jafar = card_new( imagepath="images/cardgame/t1/genie_realm/jafar_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 1,
                                    rightvalue = 4,
                                    leftvalue = 2,
                                    title="Jafar",
                                    description = "That silvertongued motherfucker..")
                                    
        card_santa = card_new( imagepath="images/cardgame/t1/special/santa_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 2,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="Santa",
                                    description = "Some guy that's been stealing your style. I'll put him on my naughty list.")
                                    
        #Tier 1 cards
                                    
        card_her_schoolgirl = card_new( imagepath="images/cardgame/t1/hermione/her_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 4,
                                    bottomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 1,
                                    title="Hermione Granger",
                                    description = "The Granger girl wearing her normal school uniform.")
                                    
        card_her_librarian = card_new( imagepath="images/cardgame/t1/hermione/her_librarian_v%s.png" % str(geniecard_level),
                                    topvalue = 5,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 4,
                                    title="Hermione Granger",
                                    description = "The Granger girl clutching a real page turner")
                                    
        card_sus_schoolgirl = card_new( imagepath="images/cardgame/t1/susan/sus_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 3,
                                    bottomvalue = 4,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Susan Bones",
                                    description = "Miss Bones, barely contained within her school uniform.")
                                    
        card_cho_schoolgirl = card_new( imagepath="images/cardgame/t1/cho/cho_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 2,
                                    bottomvalue = 4,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="Cho Chang",
                                    description = "Miss Chang, sporting her school uniform.")
                                    
        card_lun_schoolgirl = card_new( imagepath="images/cardgame/t1/luna/lun_schoolgirl_v%s.png" % str(geniecard_level),
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 4,
                                    leftvalue = 3,
                                    title="Luna Lovegood",
                                    description = "Miss Lovegood, wearing her normal school uniform.")
                                    
        #Item cards
        
        card_item_badge = card_new( imagepath="images/cardgame/t1/other/badge_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 1,
                                    rightvalue = 1,
                                    leftvalue = 3,
                                    title="SPEW Badge",
                                    description="The S.P.E.W Badge, I think it might stand for Sluts for the Pleasuring of Excited Wizards...")
                                    
        card_item_barbell = card_new( imagepath="images/cardgame/t1/other/barbell_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Barbell piercing",
                                    description="A nipple piercing a female student might wear... after some convincing.")
                                    
        card_item_beads = card_new( imagepath="images/cardgame/t1/other/beads_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 4,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Anal beads",
                                    description="Some beads, I'm sure you already know where these go... Hogwarts express to brown town.")
                                    
        card_item_bird = card_new( imagepath="images/cardgame/t1/other/bird_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Phoenix",
                                    description="A bird that was here when I arrived. It doesn't say or do much... I like it.")
                                    
        card_item_bookchairs = card_new( imagepath="images/cardgame/t1/other/bookchairs_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="Book of Chairs",
                                    description="A book with seemingly sharp pages. I've not dared to open it.")
                                    
        card_item_bookgala = card_new( imagepath="images/cardgame/t1/other/bookgala_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="Book of Galadrier (Light ED)",
                                    description="One of the books, waste of printing paper.")
                                    
        card_item_bookgala2 = card_new( imagepath="images/cardgame/t1/other/bookgala2_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 4,
                                    rightvalue = 2,
                                    leftvalue = 1,
                                    title="Book of Galadriel (Hardcore ED)",
                                    description="One of the books, a culture shock and a half.")
                                    
        card_item_bookwaifu = card_new( imagepath="images/cardgame/t1/other/bookwaifu_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Waifu Book",
                                    description="One of the books, a culture shock and a half.")
                                    
        card_item_broom = card_new( imagepath="images/cardgame/t1/other/broom_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 4,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="Modified Nimbus 2000",
                                    description="Highly modified broom. I'd call it, \"The Thundersnatch.\"")
                                    
        card_item_bdsm = card_new( imagepath="images/cardgame/t1/other/bdsm_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="BDSM Kit",
                                    description="Fetish gear, I like it for the peace and quiet.")
                                    
        card_item_condoms = card_new( imagepath="images/cardgame/t1/other/condoms_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 3,
                                    title="Pack of condoms",
                                    description="Some condoms, I don't need them.")
                                    
        card_item_desk = card_new( imagepath="images/cardgame/t1/other/desk_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 3,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="Office desk",
                                    description="My desk, with an underside way more glazed than before I arrived.")
                                    
        card_item_dildo = card_new( imagepath="images/cardgame/t1/other/dildo_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Magical Dildo",
                                    description="A Dildo, the perfect gift for any female student.")
                                    
        card_item_doll = card_new( imagepath="images/cardgame/t1/other/doll_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="Sex Doll",
                                    description="A sex doll. Wished I had one of these in my lamp...")
                                    
        card_item_elf = card_new( imagepath="images/cardgame/t1/other/elf_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="House-Elf",
                                    description="Disgusting creature... Apparently they clean underneath my desk though.")
                                    
        card_item_eromag = card_new( imagepath="images/cardgame/t1/other/eromag_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Erotic Magazine",
                                    description="Perfect way to teach any girl about the more important things in life.")
                                    
        card_item_girlmag = card_new( imagepath="images/cardgame/t1/other/girlmag_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Girly Magazine",
                                    description="A good gift to make you seem hip. Whatever that means.")
                                    
        card_item_hat = card_new( imagepath="images/cardgame/t1/other/hat_v1.png",
                                    topvalue = 6,
                                    bottomvalue = 1,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Sorting Hat",
                                    description="One of the weird items in my office. I swear it talked to me once.")
                                    
        card_item_lingerie = card_new( imagepath="images/cardgame/t1/other/lingerie_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 4,
                                    rightvalue = 2,
                                    leftvalue = 2,
                                    title="Lingerie",
                                    description="If a girl needs to wear any undergarments at all these would be my preferred choice.")
                                    
        card_item_lipstick = card_new( imagepath="images/cardgame/t1/other/lipstick_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Lipstick (Red)",
                                    description="For when a girl wants to feel less naked. Comes in a variety of unnatural colours.")
                                    
        card_item_lube = card_new( imagepath="images/cardgame/t1/other/lube_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 5,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Jar of lubricant",
                                    description="A Jar full of lube, I should get a subscription for these.")
                                    
        card_item_owl = card_new( imagepath="images/cardgame/t1/other/owl_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Stuffed Owl",
                                    description="An Owl plush, very popular among the girls.")
                                    
        card_item_plugs = card_new( imagepath="images/cardgame/t1/other/plugs_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 3,
                                    title="Set of anal plugs",
                                    description="A selection of plugs... Bit weird, even for me. ")
                                    
        card_item_pornmag = card_new( imagepath="images/cardgame/t1/other/pornmag_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 1,
                                    title="Porno Magazine",
                                    description="Some porn mags. Perfect gift for the more sophisticated lady. ")
                                    
        card_item_potions = card_new( imagepath="images/cardgame/t1/other/potions_v1.png",
                                    topvalue = 3,
                                    bottomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 2,
                                    title="Batch of Potions",
                                    description="A set of potions. None of my favorites...")      

        card_item_scroll = card_new( imagepath="images/cardgame/t1/other/scroll_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 4,
                                    rightvalue = 2,
                                    leftvalue = 3,
                                    title="Forbidden Scroll",
                                    description="One of the scrolls from the Weasley's shop.")
                                    
        card_item_stockings = card_new( imagepath="images/cardgame/t1/other/stockings_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 3,
                                    title="Pair of stockings",
                                    description="Pair of stockings, looks great with a short skirt.")
                                    
        card_item_strapon = card_new( imagepath="images/cardgame/t1/other/strapon_v1.png",
                                    topvalue = 2,
                                    bottomvalue = 3,
                                    rightvalue = 1,
                                    leftvalue = 4,
                                    title="Thestral Strapon",
                                    description="Don't have any use for these but they're great practice for the ladies.")
                                    
        card_item_sweets = card_new( imagepath="images/cardgame/t1/other/sweets_v1.png",
                                    topvalue = 1,
                                    bottomvalue = 1,
                                    rightvalue = 2,
                                    leftvalue = 3,
                                    title="Pack of Sweets",
                                    description="Some of the most popular sweets. Including Butter beer, not alcoholic enough in my opinion.")
                                    
        card_item_wine = card_new( imagepath="images/cardgame/t1/other/wine_v1.png",
                                    topvalue = 4,
                                    bottomvalue = 2,
                                    rightvalue = 1,
                                    leftvalue = 2,
                                    title="Bottle of wine",
                                    description="That wine I keep finding in this cupboard. Not sure if the wine is magically infused or the cupboard.")
            
        if not hasattr(renpy.store,'deck_unlocked'):
            deck_unlocked = False
            deck_mail_send = False
            enemy_deck = []
            duel_win_label = ""
            duel_loss_label = ""
        
        if not hasattr(renpy.store,'snape_know_cards'):
            snape_know_cards = False
            snape_first_win = False
            snape_second_win = False
            snape_third_win = False
            snape_wager_talk = False
            random_snape_win = False

        if not hasattr(renpy.store, 'her_know_cards'):
            her_know_cards = False
            her_cards_stocked_talk = False
            her_first_win = False
            her_second_win = False
            her_third_win = False
            her_random_win = False
            cardgame_work = False
            first_time_cardgame_work = True
            
        if not hasattr(renpy.store, 'twins_know_cards'):
            twins_know_cards = False
            twins_first_win = False
            twins_second_win = False
            twins_cards_delay = 7
            twins_cards_stocked = False
            twins_cards_stocked_talk = False
            twins_interest = False
            first_random_twins = True
            twins_random_win = True
            twins_profit = 1.0
        
        if not hasattr(renpy.store,'unlocked_cards'):
            card_rand_realm = renpy.random.choice([card_iris, card_jasmine, card_azalea])
            card_rand_girl = renpy.random.choice([card_her_schoolgirl, card_sus_schoolgirl, card_cho_schoolgirl, card_lun_schoolgirl])
            card_rand_item1 = renpy.random.choice([card_item_desk, card_item_bird])
            card_rand_item2 = renpy.random.choice([card_item_beads, card_item_dildo, card_item_doll, card_item_condoms, card_item_plugs])
            card_rand_item3 = renpy.random.choice([card_item_barbell, card_item_lingerie, card_item_stockings, card_item_badge, card_item_bdsm, card_item_lipstick])
            card_rand_item4 = renpy.random.choice([card_item_bookchairs, card_item_bookgala, card_item_bookgala2, card_item_bookwaifu, card_item_hat])
            card_rand_item5 = renpy.random.choice([card_item_eromag, card_item_pornmag, card_item_girlmag, card_item_scroll, card_item_sweets])
            unlocked_cards = [card_genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2, card_rand_item3, card_rand_item4, card_rand_item5]
            playerdeck = [card_genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2]
            # Delete copies of playerdeck cards
            for i in range(0,5):
                playerdeck[i].copies = 0
                
            card_rule_reverse = cardgame_rules(name="Reverse", description="Instead of a higher number, you need to have the lowest number to take over a card.", icon="images/cardgame/rule_reverse.png")
            card_rule_hidden = cardgame_rules(name="Hidden", description="The hidden rule means that a certain amount of cards in your enemies deck will be hidden.", icon="images/cardgame/rule_hidden.png")
            card_rule_death = cardgame_rules(name="Death", description="If your game ends in a draw you pick up the cards that are shown in your colour and play again.", icon="images/cardgame/rule_death.png")
            card_rule_double = cardgame_rules(name="Double", description="If the card you put down has the same number facing at least 2 other cards (Rather than higher/lower) you'll take over those cards.", icon="images/cardgame/rule_double.png")
            card_rule_random = cardgame_rules(name="Random", description="Your deck is selected randomly from the available cards.", icon="images/cardgame/rule_random.png")
                
        cards_realm = [card_genie, card_iris, card_jasmine, card_azalea, card_dahlia, card_maslab, card_aladdin, card_lilly, card_rasul, card_jafar]
        cards_hogwarts = [card_her_schoolgirl, card_her_librarian, card_lun_schoolgirl, card_sus_schoolgirl, card_cho_schoolgirl, card_fred, card_george, card_snape, card_dumbledore]
        cards_other = [card_santa]
        cards_items = [card_item_badge, card_item_barbell, card_item_beads, card_item_bird, card_item_bookchairs, card_item_bookgala, card_item_bookgala2, card_item_bookwaifu, card_item_broom, card_item_bdsm, card_item_condoms, card_item_desk, card_item_dildo, card_item_doll, card_item_elf, card_item_eromag, card_item_girlmag, card_item_hat, card_item_lingerie, card_item_lipstick, card_item_lube, card_item_owl, card_item_plugs, card_item_pornmag, card_item_potions, card_item_scroll, card_item_stockings, card_item_strapon, card_item_sweets, card_item_wine]
        cards_all = cards_realm
        cards_all += cards_hogwarts
        cards_all += cards_other
        cards_all += cards_items
        
        cards_dynamic = [card_iris, card_jasmine, card_azalea, card_her_schoolgirl, card_her_librarian, card_lun_schoolgirl, card_sus_schoolgirl, card_cho_schoolgirl]
        
        if not hasattr(renpy.store,'snape_first_deck'):
            snape_first_deck = [card_snape.clone(), card_item_potions.clone(), card_item_elf.clone(), card_item_wine.clone(), card_item_lipstick.clone()]
            snape_second_deck = [card_snape.clone(), card_item_potions.clone(), card_item_elf.clone(), card_item_elf.clone(), card_item_eromag.clone()]
            snape_third_deck = [card_snape.clone(), card_item_potions.clone(), card_item_elf.clone(), card_item_elf.clone(), card_item_elf.clone()]
            
        if not hasattr(renpy.store,'twins_first_deck'):
            twins_first_deck = [card_fred.clone(), card_item_sweets.clone(), card_item_beads.clone(), card_item_sweets.clone(), card_item_condoms.clone()]
            twins_second_deck = [card_george.clone(), card_fred.clone(), card_item_doll.clone(), card_item_sweets.clone(), card_item_broom.clone()]
            
        if not hasattr(renpy.store,'her_first_deck'):
            her_first_deck = [card_her_schoolgirl.clone(), card_item_girlmag.clone(), card_item_bookgala.clone(), card_item_bookgala2.clone(), card_item_bookchairs.clone()]
            her_second_deck = [card_her_schoolgirl.clone(), card_item_eromag.clone(), card_item_bookgala.clone(), card_item_bookgala2.clone(), card_item_bookchairs.clone()]
            her_third_deck = [card_her_librarian.clone(), card_item_pornmag.clone(), card_item_bookgala.clone(), card_item_bookgala2.clone(), card_item_bookchairs.clone()]

        card_non_spec_char = [ "I see you've been practicing... so have I!", "You've activated my trap card... wait... it's in my other deck!", "You think you're so good, but this school has never seen a player of the likes of me! In this particular office...", "Aha, you've walked right into my trap. Take this!", "You'll never beat me! I will give you the reward though... in your dreams!", "Thats impossible... that card is legendary... wait, it doesn't have a shimmering effect, never mind.", "I was sure my cards used to be good...", "Wait, you've got that card... I've been such a fool! This is a witchmasters deck!", "We're playing reverse rules right? Lowest amount of cards win?", "If only slight of hand was taught at Hogwarts...", "Wait, this can't be right. I must have put my good cards in my other robes.", "You should be happy that they banned one of the cards that came in a cereal box promotion... that one was overpowered.", "This one's a board sweeper!", "I'll just burn this card... oh yeah, I got better cards coming.", "This is a control deck. I'll win in the end don't you worry.", "Maybe I should have made less of a filler deck... I'll get you in the end.", "Your loss is inevitable. It's all in the heart of the cards.", "Have you been Netdecking? Did those damn spiders in the forest tell you what cards to play?", "I've been metagaming the crap out of you... I know exactly what cards you're going to play...except for that last one.", "Oh, it's my turn? I was just thinking about how I'm going to celebrate after your inevitable loss.", "I've been slowrolling you this whole time. My last card is a mega ultimate legendary.", "What kind of deck is this... don't you even care about synergy?", "I see what kind of player you are now... perhaps a more offensive approach is in order.", "I was born to play card games... you merely adopted your liking of them.", "Hahah, you don't even know that I have a card with powers that has been locked away for centuries... unfortunately I lost the key...", "Prepare for a total wipe... your tears when I beat you that is.", "You want to know what's shown on my cards? What do I like the most? Winning, which is why this card is going to guarantee my victory.", "Life is like a game of Wizard Cards. If you don't win... you lose.", "Quitters never win, winners never quit, but those who never win and never quit are idiots... I'm not sure which I am.", "Go fish...", "Do you have any spells to make you better at Wizard Cards? Didn't think so...", "You can smell the roses as much as you want, while I smell the aroma of victory", "Do you see any stars yet, because you're getting beaten pretty badly.", "Well, your performance in this round is certainly a divine comedy.", "The forecast today is calling for my victory, so I'm not worried.", "Are you out of juice already?", "Couldn't you see from your own fortune that you're bound to lose?", "Looks like you fell right into your own trap... now look at this!! KAPOW", "I don't need luck potion to beat you. That's how confident I am in my deck.", "I know my deck like the back of my hand... wait, when did that mole get there?", "Fool, you'll soon see my finishing move... but before that, UNO!", "I'm so confident in my card collection I just shuffled and picked some at random before this game.", "Great cards doesn’t ensure a win. Right moves do.", "The game balance of this game has been broken for centuries... and I have the winning cards.", "The ministry of magic considered banning this game as they thought it all mattered what cards you had... something about gambling for children.", "If I said that I picked my cards blindfolded would you believe me? Yes, they're all that good.", "I tried to use transfiguration on one of my cards but it burnt up instead... I probably wasn't the first one who tried that.", "Wait! Isn't that card banned? No, the stats aren't the same...phew", "Why does that card of yours look so sticky?", "Oh nice a shiny... wait, why has it stuck to the board?", "That's nowhere near the best move you could've done. Check this out!", "Even a troll would play better than you at this point... no offense.", "Some people are half blood and some pure blood. But I'm purely a Card playing genius.", "That must be a new card. Why haven't I seen that one before?", "Wait, my numbers must have changed. Did you put a spell on my cards?", "Hit me... I mean, give me another card.", "Ah, that one. To bad I have the perfect counter.", "So, when do I get to draw a card again?", "Someone replaced one of my cards with a joker... I bet it was peeves.", "I was told that face cards was the best ones to get... but they were talking about poker.", "By Merlins beard, where did you get that card?", "Next time you should let me use the cards I drew. Their numbers are a lot better than these ones."]
        
        snape_speech_card = ["You may have lived for hundreds of years but my superior intellect will outweigh your otherworldly powers.", "When this is over I think I'll celebrate my victory with one of your nice bottles of alcohol.", "You should stick to charming women... wizard cards is my game.", "You said you were from a different world, another reality? Maybe in that reality you'd beat me at cards. But not this one!", "We don't stop playing because we grow old, we grow old because we stop playing.", "Where did you even find your trash cards? In a promotional pamphlet?", "Why are my cards so much greasier than yours?"] + card_non_spec_char
        
        twins_speech_card = ["Our cards are fresher than fresh. They were printed last night so they must be good.", "Giving you a percentage of our profit was an easy bet, because we know you'll never win.", "We weighed our packs before opening them so our cards must be rare.", "Activate twin psychic link.", "Some people wouldn't duel a duo because they can't maintain eye contact during play... or eye to card contact.", "We're a two player team, so we get double the cards to chose from right?", "We're not going easy on you just so you wont shut our shop down.", "What's on our cards? Sweet, sweet profit of course.", "Hey, that percentage we promised you... you mind lowering it a bit? I mean, a deal is a deal...but still.", "You better open up the trade routes a bit more if you beat us. We don't want to deal with Filtch if he finds where these cards came from.", "We probably should have opened a few of our boosters but where's the fun without a bit of risk?"] + card_non_spec_char
        
        her_speech_card = ["You should double the points you give me if I win... or at least consider it.", "I'm great at wizards chess so beating you at this shouldn't be a problem...", "I should have asked for house points if I beat you... oh well, too late now.", "Have you been looking at my deck? That's cheating, you better whip yours out..."] + card_non_spec_char
        
        
init python:
    #For card randomization
    import random
    
    def clamp(n, smallest, largest): 
        return max(smallest, min(n, largest))
        
    def card_exist(unlockedlist, cardobj):
        for elm in unlockedlist:
                if cardobj.title == elm.title:
                    return True
        return False
    replace_index = 0
    new_deck = []
    def create_random_deck(min, max, card_pool):
        new_deck = []
        smalles_func = lambda elm1, elm2 : elm1.get_total_value() > elm2.get_total_value()
        gretest_func = lambda elm1, elm2 : elm1.get_total_value() < elm2.get_total_value()
        temp_pool = []
        temp_pool.extend(card_pool)
        for card in range(0,5):
            random_choice = renpy.random.choice(temp_pool)
                    
            new_deck.append(random_choice)
            del temp_pool[temp_pool.index(random_choice)]
            
        while min > get_deck_score(new_deck) or max < get_deck_score(new_deck):
            replace_index = 0
            if new_deck < min:
                replace_index = find_index_func(temp_pool, smalles_func)
            else:
                replace_index = find_index_func(temp_pool, gretest_func)

                
            replace_index = clamp(replace_index,0,4)   
            random_choice = renpy.random.choice(temp_pool)
            
            temp_pool.append(new_deck[replace_index])
            new_deck[replace_index] = (random_choice)
            del temp_pool[temp_pool.index(random_choice)]
                
        return new_deck
    def find_index_func(seq, func):
        func_index = 0
        for i in range(0, len(seq)):
            if func(seq[func_index], seq[i]):
                func_index = i
        return func_index
        
    def get_deck_score(deck):
        score = 0
        for card in deck:
            score += card.get_total_value()
        return score
    
    def playerTint(image):
        return im.MatrixColor(image, im.matrix.tint(playercolor_rgb[0]/255.0, playercolor_rgb[1]/255.0, playercolor_rgb[2]/255.0))
    def enemyTint(image):
        return im.MatrixColor(image, im.matrix.tint(enemycolor_rgb[0]/255.0, enemycolor_rgb[1]/255.0, enemycolor_rgb[2]/255.0))
    def grayTint(image):
        return im.MatrixColor(image, im.matrix.desaturate())
      
    def get_image_size(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]
        
        return (x,y)
        
    def get_hex_string(red, green, blue, alpha=1.0):
        red = str(hex( int( math.ceil( red*255))))[2:]
        if not len(red) == 2:
            red = "0"+red
        green = str(hex(int(math.ceil( green * 255))))[2:]
        if not len(green) == 2:
            green = "0"+green
        blue = str(hex(int(math.ceil( blue * 255))))[2:]
        if not len(blue) == 2:
            blue = "0"+blue
        alpha = str(hex(int(math.ceil( alpha * 255))))[2:]
        if not len(alpha) == 2:
            alpha = "0"+alpha    
        
        return "#" + red + green + blue + alpha
        
    def get_hex_string_tuple(color):
        return get_hex_string(color[0], color[1], color[2], color[3])
        
    def get_rgb_tuple(hex):
        hex = hex.lstrip('#')
        hex_len = len(hex)
        rgb = tuple(int(hex[i:i + hex_len // 3], 16) for i in range(0, hex_len, hex_len // 3))
        rgb = rgb + (255,) # Add alpha
        return rgb
        
    def get_rgb_list(hex):
        hex = hex.lstrip('#')
        hex_len = len(hex)
        rgb = list(int(hex[i:i + hex_len // 3], 16) for i in range(0, hex_len, hex_len // 3))
        rgb = rgb + [255] # Add alpha
        return rgb
    
    def get_width(image):   
        return get_image_size(image)[0]
        
    def get_height(image):
        return get_image_size(image)[1]    
    
    def reset_table_cards():
        global table_cards
        
        for y in range(0,3):
            for x in range(0,3):
                table_cards[x][y] = None
        return
        
    def check_winner(player_deck):
        global table_cards
        playerpoints = len(player_deck)

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y].playercard:
                    playerpoints += 1
        if playerpoints > 5:        
            return "win" 
        elif playerpoints == 5:
            return "draw" 
        else:
            return "loss"
           
    def update_table(x, y, reverse, dobelt_number):
        global table_cards
        if reverse:
            take_over = lambda a, b : a < b
        else:
            take_over = lambda a, b : a > b
        

        if not y == 0 and not table_cards[x][y-1] == None and take_over(table_cards[x][y].topvalue, table_cards[x][y-1].bottomvalue):
            table_cards[x][y-1].playercard = table_cards[x][y].playercard
            
        if not y == 2 and not table_cards[x][y+1] == None and take_over(table_cards[x][y].bottomvalue, table_cards[x][y+1].topvalue):
            table_cards[x][y+1].playercard = table_cards[x][y].playercard
            
        if not x == 0 and not table_cards[x-1][y] == None and take_over(table_cards[x][y].leftvalue, table_cards[x-1][y].rightvalue):
            table_cards[x-1][y].playercard = table_cards[x][y].playercard
            
        if not x == 2 and not table_cards[x+1][y] == None and take_over(table_cards[x][y].rightvalue, table_cards[x+1][y].leftvalue):
            table_cards[x+1][y].playercard = table_cards[x][y].playercard
        
        if dobelt_number:
            dobelt_found = []
            if not y == 0 and not table_cards[x][y-1] == None:
                if table_cards[x][y].topvalue == table_cards[x][y-1].bottomvalue:
                    dobelt_found.append([x,y-1])

            if not y == 2 and not table_cards[x][y+1] == None:
                if table_cards[x][y].bottomvalue == table_cards[x][y+1].topvalue:
                    dobelt_found.append([x,y+1])
                
            if not x == 0 and not table_cards[x-1][y] == None:
                if table_cards[x][y].leftvalue == table_cards[x-1][y].rightvalue:
                    dobelt_found.append([x-1,y])

                
            if not x == 2 and not table_cards[x+1][y] == None:
                if table_cards[x][y].rightvalue == table_cards[x+1][y].leftvalue:
                    dobelt_found.append([x+1,y])
                    
            if len(dobelt_found) > 1:
                for card in dobelt_found:
                    table_cards[card[0]][card[1]].playercard = table_cards[x][y].playercard
            
    def add_card_to_deck(title):
            for card in unlocked_cards:
                if title == card.title:
                    card.copies += 1
                    
    class cardgame_rules(object):
        name = None
        description = None
        icon = None
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
                     
    class card_new(object):
        playercard = True
        textcolor = "{color=#ffffff}"
        copies = 0
        description = "Description"
        title = "Title"
        imagepath = "images/cardgame/card.png"
        backside = "images/cardgame/t1/backside/gryffindor.png"
        
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
        
        def get_back_image(self, zoom=0.5):
            return im.Scale(self.backside, card_width*zoom, card_height*zoom)
        def get_back_hover(self, zoom=0.5):
            return im.MatrixColor(im.Scale(self.backside, card_width*zoom, card_height*zoom),im.matrix.brightness(0.12))

        def get_title(self):
            return self.textcolor+self.title+"{/color}"
        def get_amount(self):
            return self.textcolor+"amount: " + str(self.copies+1)+"{/color}"
        def get_totalvalue(self):
            return self.textcolor+str(self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue)+"{/color}"
        def get_total_value(self):
            return self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue    
        
        def get_description(self):
            return self.textcolor+self.description+"{/color}"
            
        def clone(self):
            return card_new(title = self.title,imagepath=self.imagepath, topvalue=self.topvalue, bottomvalue=self.bottomvalue, rightvalue=self.rightvalue, leftvalue=self.leftvalue, playercard = self.playercard)
                    
        def getAIScore(self, table_of_cards, reverse, dobelt_number):
            high_score = 0
            position = 0
            wallscore = 3
            getcardscore = 12
            if reverse:
                score_func = lambda a : 10 - a
                take_over = lambda a, b : a < b
            else:
                score_func = lambda a : a
                take_over = lambda a, b : a > b
                
            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if not y == 0 and not table_cards[x][y-1] == None and table_cards[x][y-1].playercard:
                            if take_over(self.topvalue, table_cards[x][y-1].bottomvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.topvalue)
                        else:
                            score += wallscore
                            
                        if not y == 2 and not table_cards[x][y+1] == None and table_cards[x][y+1].playercard:
                            if take_over(self.bottomvalue, table_cards[x][y+1].topvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.bottomvalue)
                        else:
                            score += wallscore
                            
                        if not x == 0 and not table_cards[x-1][y] == None and table_cards[x-1][y].playercard:
                            if take_over(self.leftvalue, table_cards[x-1][y].rightvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.leftvalue)
                        else:
                            score += wallscore
                            
                        if not x == 2 and not table_cards[x+1][y] == None and table_cards[x+1][y].playercard:
                            if take_over(self.rightvalue, table_cards[x+1][y].leftvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.rightvalue)
                        else:
                            score += wallscore
                            
                        if dobelt_number:
                            dobelt_found = []
                            if not y == 0 and not table_cards[x][y-1] == None:
                                if self.topvalue == table_cards[x][y-1].bottomvalue:
                                    dobelt_found.append(table_cards[x][y-1])
     
                            if not y == 2 and not table_cards[x][y+1] == None:
                                if self.bottomvalue == table_cards[x][y+1].topvalue:
                                    dobelt_found.append(table_cards[x][y+1])
                                
                            if not x == 0 and not table_cards[x-1][y] == None:
                                if self.leftvalue == table_cards[x-1][y].rightvalue:
                                    dobelt_found.append(table_cards[x-1][y])

                                
                            if not x == 2 and not table_cards[x+1][y] == None:
                                if self.rightvalue == table_cards[x+1][y].leftvalue:
                                    dobelt_found.append(table_cards[x+1][y])
                                    
                            if len(dobelt_found) > 1:
                                for card in dobelt_found:
                                    if card.playercard:
                                        high_score += getcardscore
                            
                        if score > high_score:
                            high_score = score
                            position = (x, y)
                            
                            
            return [high_score, position]