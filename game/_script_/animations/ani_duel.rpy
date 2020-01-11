
# Animation that shows a broken glass effect when the duel starts.
image glass:

    contains:
        "images/dueling/snape/glass/gradient.png"
    
    contains:
        pause 1.3
        "images/dueling/snape/glass/01.png"
        pause.1
        "images/dueling/snape/glass/02.png"
        pause.1
        "images/dueling/snape/glass/03.png"
        pause.1
        "images/dueling/snape/glass/04.png"
        pause.1
        "images/dueling/snape/glass/05.png"
        pause.1
        "images/dueling/snape/glass/06.png"
        pause.1
        "images/dueling/snape/glass/07.png"
        pause.1
        "images/dueling/snape/glass/08.png"
        pause.1
        "images/dueling/snape/glass/09.png"
        pause.1
        "images/dueling/snape/glass/10.png"
        
    contains:
        "images/dueling/snape/glass/crack.png"

image duel_table:
    zoom 0.5
    "images/rooms/main_room/desk_with_shadow.png"

image smoke:
    zoom 0.5
    alpha 1.0
    "images/animation/smoke_01.png"
    pause.1
    "images/animation/smoke_02.png"
    pause.1
    "images/animation/smoke_03.png"
    pause.1
    alpha 0.0
    pause.1

image teleport_ani:
    "magic/magic4.png"
    pause.05
    "magic/magic5.png"
    pause.1
    "magic/magic1.png"
    pause.05
    "magic/magic2.png"
    pause.3

image heal_ani:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06

image heal_02: # Smaller version of heal. 40% of the original size.
    "magic/heal_02/heal01.png"
    pause.06
    "magic/heal_02/heal02.png"
    pause.06
    "magic/heal_02/heal03.png"
    pause.06
    "magic/heal_02/heal04.png"
    pause.06
    "magic/heal_02/heal05.png"
    pause.06
    "magic/heal_02/heal06.png"
    pause.06
    "magic/heal_02/heal07.png"
    pause.06
    "magic/heal_02/heal08.png"
    pause.06
    "magic/heal_02/heal09.png"
    pause.06
    "magic/heal_02/heal10.png"
    pause.06
    "magic/heal_02/heal11.png"
    pause.06
    "magic/heal_02/heal12.png"
    pause.06
    "magic/heal_02/heal13.png"
    pause.06
    "magic/heal_02/heal14.png"
    pause.06
    "magic/heal_02/heal15.png"
    pause.06
    "magic/heal_02/heal16.png"
    pause.06
    "magic/heal_02/heal17.png"
    pause.06
    "magic/heal_02/heal18.png"
    pause.06


### GENIE SPELL ANIMATION ###
image spell_ani:
    "images/animation/spell01.png"
    pause.1
    "images/animation/spell02.png"
    pause.1
    "images/animation/spell03.png"
    pause.1
    "images/animation/spell04.png"
    pause.1
    "images/animation/spell05.png"
    pause.1
    "images/animation/spell06.png"
    pause.1
    "images/animation/spell07.png"
    pause.1
    "images/animation/spell08.png"
    pause.1
    "images/animation/spell09.png"
    pause.1
    "images/animation/spell10.png"
    pause.1
    "images/animation/spell11.png"
    pause.1
    "images/animation/spell12.png"
    pause.1
    "images/animation/spell13.png"
    pause.1
    "images/animation/spell14.png"
    pause.1
    "images/animation/spell15.png"
    pause.1
    "images/animation/spell16.png"
    pause.1
    "images/animation/spell17.png"
    pause.1

image ch_sna duel_01:
    zoom 0.5
    "images/dueling/snape/snape_01.png"
    pause.1
    "images/dueling/snape/snape_02.png"
    pause.1
    "images/dueling/snape/snape_03.png"
    pause.1
    "images/dueling/snape/snape_02.png"
    pause.1
    repeat

image ch_gen duel_01:
    zoom 0.5
    "images/dueling/snape/gen_01.png"
    pause.1
    "images/dueling/snape/gen_02.png"
    pause.1
    "images/dueling/snape/gen_03.png"
    pause.1
    "images/dueling/snape/gen_02.png"
    pause.1
    repeat

image ch_gen guard:
    zoom 0.5
    "images/dueling/snape/guard_01.png"
    pause.1
    "images/dueling/snape/guard_02.png"
    pause.1
    "images/dueling/snape/guard_03.png"
    pause.1
    "images/dueling/snape/guard_02.png"
    pause.1
    repeat

image ch_gen barb:
    zoom 0.5
    "images/dueling/snape/barb_01.png"
    pause.15
    "images/dueling/snape/barb_02.png"
    pause.15
    repeat

image genie_no_magic:
    zoom 0.5
    "images/dueling/snape/no_magic.png"

image ch_sna defend:
    zoom 0.5
    "images/dueling/snape/snape_defend_01.png"
    pause.1
    "images/dueling/snape/snape_defend_02.png"
    pause.1
    "images/dueling/snape/snape_defend_03.png"
    pause.1
    "images/dueling/snape/snape_defend_02.png"
    pause.1
    repeat

image snape_attack:
    zoom 0.5
    "images/dueling/snape/sna_attack_01.png"
    pause.08
    "images/dueling/snape/sna_attack_02.png"
    pause.08
    "images/dueling/snape/sna_attack_03.png"
    pause.08
    "images/dueling/snape/sna_attack_04.png"
    pause.08
    "images/dueling/snape/sna_attack_05.png"
    pause.08
    "images/dueling/snape/sna_attack_06.png"
    pause.08
    "images/dueling/snape/sna_attack_07.png"
    pause.08
    "images/dueling/snape/sna_attack_08.png"
    pause.08
    "images/dueling/snape/sna_attack_09.png"
    pause.08
    "images/dueling/snape/sna_attack_10.png"
    pause.08
    repeat

image snape_attack_guard:
    zoom 0.5
    "images/dueling/snape/sna_attack_guard_01.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_02.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_03.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_04.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_05.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_06.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_07.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_08.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_09.png"
    pause.08
    "images/dueling/snape/sna_attack_guard_10.png"
    pause.08
    repeat

image genie_attack:
    zoom 0.5
    "images/dueling/snape/genie_attack_01.png"
    pause.15
    "images/dueling/snape/genie_attack_02.png"
    pause.15
    "images/dueling/snape/genie_attack_01.png"
    pause.15
    "images/dueling/snape/genie_attack_02.png"
    pause.15
    "images/dueling/snape/genie_attack_01.png"
    pause.15
    "images/dueling/snape/genie_attack_02.png"
    pause.15
    "images/dueling/snape/genie_attack_03.png"
    pause.15
    "images/dueling/snape/genie_attack_04.png"
    pause.15
    "images/dueling/snape/genie_attack_05.png"
    pause.15
    "images/dueling/snape/genie_attack_06.png"
    pause.15
    "images/dueling/snape/genie_attack_07.png"
    pause.15
    "images/dueling/snape/genie_attack_08.png"
    pause.15
    "images/dueling/snape/genie_attack_09.png"
    pause.15
    "images/dueling/snape/genie_attack_10.png"
    pause.15
    "images/dueling/snape/genie_attack_11.png"
    pause.15
    "images/dueling/snape/genie_attack_12.png"
    pause.15
    "images/dueling/snape/genie_attack_13.png"
    pause.15
    "images/dueling/snape/genie_attack_14.png"
    pause.15
    "images/dueling/snape/genie_attack_15.png"
    pause.15
    "images/dueling/snape/genie_attack_14.png"
    pause.15
    "images/dueling/snape/genie_attack_15.png"
    pause.15
    repeat

# Snape is in defense stance. Barbarian throws axes at him.
image snape_defend:
    zoom 0.5
    "images/dueling/snape/sna_block_01.png"
    pause.15
    "images/dueling/snape/sna_block_02.png"
    pause.15
    "images/dueling/snape/sna_block_01.png"
    pause.15
    "images/dueling/snape/sna_block_02.png"
    pause.15
    "images/dueling/snape/sna_block_01.png"
    pause.15
    "images/dueling/snape/sna_block_02.png"
    pause.15
    "images/dueling/snape/sna_block_03.png"
    pause.15
    "images/dueling/snape/sna_block_04.png"
    pause.15
    "images/dueling/snape/sna_block_05.png"
    pause.15
    "images/dueling/snape/sna_block_06.png"
    pause.15
    "images/dueling/snape/sna_block_07.png"
    pause.15
    "images/dueling/snape/sna_block_08.png"
    pause.15
    "images/dueling/snape/sna_block_09.png"
    pause.15
    "images/dueling/snape/sna_block_10.png"
    pause.15
    "images/dueling/snape/sna_block_11.png"
    pause.15
    "images/dueling/snape/sna_block_12.png"
    pause.15
    "images/dueling/snape/sna_block_13.png"
    pause.15
    repeat

image snape_summon:
    zoom 0.5
    "images/dueling/snape/snape_casting_01.png"

image snape_lost:
    zoom 0.5
    "images/dueling/snape/snape.png"

image pentogram:
    zoom 0.5
    alpha 0.0
    linear .5 alpha 1.0
    "images/dueling/snape/pen_01.png"
    linear .5 alpha 0.0
    repeat

image hand: #Hand appears.
    zoom 0.5
    "images/dueling/snape/hand_01.png"
    pause.1
    "images/dueling/snape/hand_02.png"
    pause.1
    "images/dueling/snape/hand_03.png"
    pause.1
    "images/dueling/snape/hand_04.png"
    pause.1
    "images/dueling/snape/hand_05.png"
    pause.1
    "images/dueling/snape/hand_06.png"
    pause.1
    "images/dueling/snape/hand_07.png"
    pause.1
    "images/dueling/snape/hand_08.png"
    pause.1
    "images/dueling/snape/hand_09.png"
    pause.1
    "images/dueling/snape/hand_10.png"
    pause.1
    "images/dueling/snape/hand_11.png"
    pause.1
    "images/dueling/snape/hand_12.png"
    pause.1
    "images/dueling/snape/hand_13.png"
    pause.1
    "images/dueling/snape/hand_14.png"
    pause.1
    "images/dueling/snape/hand_15.png"
    pause.1
    "images/dueling/snape/hand_16.png"
    pause.1
    repeat

image hand_genie: #Hand attacks Genie.
    zoom 0.5
    "images/dueling/snape/hand_genie_01.png"
    pause.1
    "images/dueling/snape/hand_genie_02.png"
    pause.1
    "images/dueling/snape/hand_genie_03.png"
    pause.1
    "images/dueling/snape/hand_genie_04.png"
    pause.1
    "images/dueling/snape/hand_genie_05.png"
    pause.1
    "images/dueling/snape/hand_genie_06.png"
    pause.1
    "images/dueling/snape/hand_genie_07.png"
    pause.1
    "images/dueling/snape/hand_genie_08.png"
    pause.1
    "images/dueling/snape/hand_genie_09.png"
    pause.1
    "images/dueling/snape/hand_genie_10.png"
    pause.1
    "images/dueling/snape/hand_genie_11.png"
    pause.1
    "images/dueling/snape/hand_genie_12.png"
    pause.1
    "images/dueling/snape/hand_genie_13.png"
    pause.1

image hand_guard: #Hand attacks the guard.
    zoom 0.5
    "images/dueling/snape/hand_guard_01.png"
    pause.1
    "images/dueling/snape/hand_guard_02.png"
    pause.1
    "images/dueling/snape/hand_guard_03.png"
    pause.1
    "images/dueling/snape/hand_guard_04.png"
    pause.1
    "images/dueling/snape/hand_guard_05.png"
    pause.1
    "images/dueling/snape/hand_guard_06.png"
    pause.1
    "images/dueling/snape/hand_guard_07.png"
    pause.1
    "images/dueling/snape/hand_guard_08.png"
    pause.1
    "images/dueling/snape/hand_guard_09.png"
    pause.1
    "images/dueling/snape/hand_guard_10.png"
    pause.1
    "images/dueling/snape/hand_guard_11.png"
    pause.1
    "images/dueling/snape/hand_guard_12.png"
    pause.1
    "images/dueling/snape/hand_guard_13.png"
    pause.1
    "images/dueling/snape/hand_guard_14.png"
    pause.1
    "images/dueling/snape/hand_guard_11.png"
    pause.1
    "images/dueling/snape/hand_guard_12.png"
    pause.1
    "images/dueling/snape/hand_guard_13.png"
    pause.1

image bouquet_appear:
    "images/animation/Bouquet0.png"
    pause.1
    "images/animation/Bouquet1.png"
    pause.1
    "images/animation/Bouquet2.png"
    pause.1
    "images/animation/Bouquet3.png"
    pause.1
    "images/animation/Bouquet4.png"
    pause.8

image flower_appear:
    "images/animation/Flower0.png"
    pause.1
    "images/animation/Flower1.png"
    pause.1
    "images/animation/Flower2.png"
    pause.1
    "images/animation/Flower3.png"
    pause.1
    "images/animation/Flower4.png"
    pause.8

# image vanish_effect_bouquet:
    # "images/animation/BouquetPaf.png"
    # pause.1
    # "images/animation/PafAndSmoke.png"
    # pause.1
    # "images/animation/NoPafSmoke.png"
    # pause.1
    # "images/animation/NoPafSmokeTrans1.png"
    # pause.1
    # "images/animation/NoPafSmokeTrans2.png"
    # pause.1

# image vanish_effect_flower:
    # "images/animation/FlowerPaf.png"
    # pause.1
    # "images/animation/PafAndSmoke.png"
    # pause.1
    # "images/animation/NoPafSmoke.png"
    # pause.1
    # "images/animation/NoPafSmokeTrans1.png"
    # pause.1
    # "images/animation/NoPafSmokeTrans2.png"
    # pause.1
