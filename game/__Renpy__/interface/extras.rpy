label gallery_ht:
    #play music galm fadeout 1
    scene title2
    with flashbb


    label after_cam:
    menu:
        "-Music room-":
            jump music_room

        "-Outskirts of Hogwarts-":
            jump out_hog

        "{color=#858585}-Ending 01-{/color}" if not persistent.ending_01:
            jump after_cam
        "-Ending 01-" if persistent.ending_01:
            label end_01_men:
            menu:
                "-First act-":
                    jump end01_01
                "-The speech-":
                    jump end01_02
                "-Finishing act-":
                    jump end01_03
                "-Cancel-":
                    jump after_cam

        "{color=#858585}-Ending 02-{/color}" if not persistent.ending_02:
            jump after_cam
        "-Ending 02-" if persistent.ending_02:
            label end_02_men:
            menu:
                "-First act-":
                    jump end02_01
                "-The speech-":
                    jump end02_02
                "-Finishing act-":
                    jump end02_03
                "-Cancel-":
                    jump after_cam


        "-Commentaries ([commentaries])-":
            $ commentaries = not commentaries # In the GALLERY turns commentaries ON and OFF.
            jump after_cam

        "-Cancel-":
            return





### OUTSKIRTS OF HOGWARTS CGs ###
label out_hog:
    show image  "images/yule_ball/171.png" with d3
    show screen ctc
    pause

    show image  "images/yule_ball/172.png" with d3
    show screen ctc
    pause



    show image  "images/yule_ball/173.png"
    with d3
    pause

    hide image  "images/yule_ball/173.png"
    hide image  "images/yule_ball/172.png"
    show image  "images/yule_ball/174.png"
    with d3
    pause

    hide image  "images/yule_ball/174.png"
    show image  "images/yule_ball/175.png"
    with d3
    pause


    hide image  "images/yule_ball/175.png" with d3

    pause

    hide image  "images/yule_ball/171.png"
    hide screen ctc
    with fade

    jump after_cam



    ### ENDING 01_01
label end01_01:
    show image  "images/yule_ball/01.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/01.png"
    show image  "images/yule_ball/02.png"
    with d3
    pause

    hide image  "images/yule_ball/02.png"
    show image  "images/yule_ball/03.png"
    with d3
    pause

    hide image  "images/yule_ball/03.png"
    show image  "images/yule_ball/04.png"
    with d3
    pause

    hide image  "images/yule_ball/04.png"
    show image  "images/yule_ball/05.png"
    with d3
    pause

    hide image  "images/yule_ball/05.png"
    show image  "images/yule_ball/06.png"
    with d3
    pause

    hide image  "images/yule_ball/06.png"
    show image  "images/yule_ball/07.png"
    with d3
    pause

    hide image  "images/yule_ball/07.png"
    show image  "images/yule_ball/08.png"
    with d3
    pause

    hide image  "images/yule_ball/08.png"
    show image  "images/yule_ball/09.png"
    with d3
    pause

    hide image  "images/yule_ball/09.png"
    show image  "images/yule_ball/10.png"
    with d3
    pause

    hide image  "images/yule_ball/10.png"
    show image  "images/yule_ball/11.png"
    with d3
    pause

    hide image  "images/yule_ball/11.png"
    show image  "images/yule_ball/12.png"
    with d3
    pause

    hide image  "images/yule_ball/12.png"
    show image  "images/yule_ball/13.png"
    with d3
    pause

    hide image  "images/yule_ball/13.png"
    show image  "images/yule_ball/14.png"
    with d3
    pause

    hide image  "images/yule_ball/14.png"
    show image  "images/yule_ball/15.png"
    with d3
    pause

    hide image  "images/yule_ball/15.png"
    show image  "images/yule_ball/16.png"
    with d3
    pause

    hide image  "images/yule_ball/16.png"
    show image  "images/yule_ball/17.png"
    with d3
    pause

    hide image  "images/yule_ball/17.png"
    show image  "images/yule_ball/18.png"
    with d3
    pause

    hide image  "images/yule_ball/18.png"
    show image  "images/yule_ball/19.png"
    with d3
    pause

    hide image  "images/yule_ball/19.png"
    show image  "images/yule_ball/20.png"
    with d3
    pause

    hide image  "images/yule_ball/20.png"
    show image  "images/yule_ball/21.png"
    with d3
    pause

    hide image  "images/yule_ball/21.png"
    show image  "images/yule_ball/22.png"
    with d3
    pause

    hide image  "images/yule_ball/22.png"
    show image  "images/yule_ball/23.png"
    with d3
    pause

    hide image  "images/yule_ball/23.png"
    show image  "images/yule_ball/24.png"
    with d3
    pause

    hide image  "images/yule_ball/24.png"
    show image  "images/yule_ball/25.png"
    with d3
    pause

    hide image  "images/yule_ball/25.png"
    show image  "images/yule_ball/26.png"
    with d3
    pause

    hide image  "images/yule_ball/26.png"
    show image  "images/yule_ball/27.png"
    with d3
    pause

    hide image  "images/yule_ball/27.png"
    show image  "images/yule_ball/28.png"
    with d3
    pause

    hide image  "images/yule_ball/28.png"
    show image  "images/yule_ball/29.png"
    with d3
    pause

    hide image  "images/yule_ball/29.png"
    show image  "images/yule_ball/30.png"
    with d3
    pause

    hide image  "images/yule_ball/30.png"
    show image  "images/yule_ball/31.png"
    with d3
    pause

    hide image  "images/yule_ball/31.png"
    show image  "images/yule_ball/32.png"
    with d3
    pause

    hide image  "images/yule_ball/32.png"
    show image  "images/yule_ball/33.png"
    with d3
    pause

    hide image  "images/yule_ball/33.png"
    show image  "images/yule_ball/34.png"
    with d3
    pause

    hide image  "images/yule_ball/34.png"
    show image  "images/yule_ball/35.png"
    with d3
    pause

    hide image  "images/yule_ball/35.png"
    show image  "images/yule_ball/36.png"
    with d3
    pause

    hide image  "images/yule_ball/36.png"
    with fade
    jump end_01_men


    ### ENDING 01_02
label end01_02:
    show image  "images/yule_ball/37.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/37.png"
    show image  "images/yule_ball/38.png"
    with d3
    pause

    hide image  "images/yule_ball/38.png"
    show image  "images/yule_ball/39.png"
    with d3
    pause

    hide image  "images/yule_ball/39.png"
    show image  "images/yule_ball/40.png"
    with d3
    pause

    hide image  "images/yule_ball/40.png"
    show image  "images/yule_ball/41.png"
    with d3
    pause

    hide image  "images/yule_ball/41.png"
    show image  "images/yule_ball/42.png"
    with d3
    pause

    hide image  "images/yule_ball/42.png"
    show image  "images/yule_ball/43.png"
    with d3
    pause

    hide image  "images/yule_ball/43.png"
    show image  "images/yule_ball/44.png"
    with d3
    pause

    hide image  "images/yule_ball/44.png"
    show image  "images/yule_ball/45.png"
    with d3
    pause

    hide image  "images/yule_ball/45.png"
    with fade
    jump end_01_men




   ### ENDING 01_03
label end01_03:
    show image  "images/yule_ball/46.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/46.png"
    show image  "images/yule_ball/47.png"
    with d3
    pause

    hide image  "images/yule_ball/47.png"
    show image  "images/yule_ball/48.png"
    with d3
    pause

    hide image  "images/yule_ball/48.png"
    show image  "images/yule_ball/49.png"
    with d3
    pause

    hide image  "images/yule_ball/49.png"
    show image  "images/yule_ball/50.png"
    with d3
    pause

    hide image  "images/yule_ball/50.png"
    show image  "images/yule_ball/51.png"
    with d3
    pause

    hide image  "images/yule_ball/51.png"
    show image  "images/yule_ball/52.png"
    with d3
    pause

    hide image  "images/yule_ball/52.png"
    show image  "images/yule_ball/53.png"
    with d3
    pause

    hide image  "images/yule_ball/53.png"
    show image  "images/yule_ball/54.png"
    with d3
    pause

    hide image  "images/yule_ball/54.png"
    show image  "images/yule_ball/55.png"
    with d3
    pause

    hide image  "images/yule_ball/55.png"
    show image  "images/yule_ball/56.png"
    with d3
    pause

    hide image  "images/yule_ball/56.png"
    show image  "images/yule_ball/57.png"
    with d3
    pause

    hide image  "images/yule_ball/57.png"
    show image  "images/yule_ball/58.png"
    with d3
    pause
    hide image  "images/yule_ball/58.png"
    show image  "images/yule_ball/59.png"
    with d3
    pause
    hide image  "images/yule_ball/59.png"
    show image  "images/yule_ball/60.png"
    with d3
    pause

    hide image  "images/yule_ball/60.png"
    show image  "images/yule_ball/61.png"
    with d3
    pause

    hide image  "images/yule_ball/61.png"
    show image  "images/yule_ball/62.png"
    with d3
    pause

    hide image  "images/yule_ball/62.png"
    show image  "images/yule_ball/63.png"
    with d3
    pause

    hide image  "images/yule_ball/63.png"
    show image  "images/yule_ball/64.png"
    with d3
    pause

    hide image  "images/yule_ball/64.png"
    show image  "images/yule_ball/65.png"
    with d3
    pause

    hide image  "images/yule_ball/65.png"
    show image  "images/yule_ball/66.png"
    with d3
    pause


    hide image  "images/yule_ball/66.png"
    show image  "images/yule_ball/67.png"
    with d3
    pause

    hide image  "images/yule_ball/67.png"
    show image  "images/yule_ball/68.png"
    with d3
    pause

    hide image  "images/yule_ball/68.png"
    show image  "images/yule_ball/69.png"
    with d3
    pause

    hide image  "images/yule_ball/69.png"
    show image  "images/yule_ball/70.png"
    with d3
    pause

    hide image  "images/yule_ball/70.png"
    show image  "images/yule_ball/71.png"
    with d3
    pause

    hide image  "images/yule_ball/71.png"
    show image  "images/yule_ball/72.png"
    with d3
    pause

    hide image  "images/yule_ball/72.png"
    show image  "images/yule_ball/73.png"
    with d3
    pause

    hide image  "images/yule_ball/73.png"
    show image  "images/yule_ball/74.png"
    with d3
    pause

    hide image  "images/yule_ball/74.png"
    show image  "images/yule_ball/75.png"
    with d3
    pause

    hide image  "images/yule_ball/75.png"
    show image  "images/yule_ball/76.png"
    with d3
    pause

    hide image  "images/yule_ball/76.png"
    show image  "images/yule_ball/77.png"
    with d3
    pause

    hide image  "images/yule_ball/77.png"
    show image  "images/yule_ball/78.png"
    with d3
    pause

    hide image  "images/yule_ball/78.png"
    show image  "images/yule_ball/79.png"
    with d3
    pause

    hide image  "images/yule_ball/79.png"
    show image  "images/yule_ball/80.png"
    with d3
    pause

    hide image  "images/yule_ball/80.png"
    show image  "images/yule_ball/81.png"
    with d3
    pause

    hide image  "images/yule_ball/81.png"
    show image  "images/yule_ball/82.png"
    with d3
    pause

    hide image  "images/yule_ball/82.png"
    show image  "images/yule_ball/83.png"
    with d3
    pause

    hide image  "images/yule_ball/83.png"
    show image  "images/yule_ball/84.png"
    with d3
    pause

    hide image  "images/yule_ball/84.png"
    show image  "images/yule_ball/85.png"
    with d3
    pause

    hide image  "images/yule_ball/85.png"
    show image  "images/yule_ball/86.png"
    with d3
    pause

    hide image  "images/yule_ball/86.png"
    show image  "images/yule_ball/87.png"
    with d3
    pause

    hide image  "images/yule_ball/87.png"
    show image  "images/yule_ball/88.png"
    with d3
    pause

    hide image  "images/yule_ball/88.png"
    show image  "images/yule_ball/89.png"
    with d3
    pause

    hide image  "images/yule_ball/89.png"
    with fade
    jump end_01_men


      ### ENDING 02_01
label end02_01:
    show image  "images/yule_ball/01.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/01.png"
    show image  "images/yule_ball/02.png"
    with d3
    pause

    hide image  "images/yule_ball/02.png"
    show image  "images/yule_ball/03.png"
    with d3
    pause

    hide image  "images/yule_ball/03.png"
    show image  "images/yule_ball/91.png"
    with d3
    pause

    hide image  "images/yule_ball/91.png"
    show image  "images/yule_ball/92.png"
    with d3
    pause

    hide image  "images/yule_ball/92.png"
    show image  "images/yule_ball/93.png"
    with d3
    pause

    hide image  "images/yule_ball/93.png"
    show image  "images/yule_ball/94.png"
    with d3
    pause

    hide image  "images/yule_ball/94.png"
    show image  "images/yule_ball/95.png"
    with d3
    pause

    hide image  "images/yule_ball/95.png"
    show image  "images/yule_ball/96.png"
    with d3
    pause

    hide image  "images/yule_ball/96.png"
    show image  "images/yule_ball/97.png"
    with d3
    pause

    hide image  "images/yule_ball/97.png"
    show image  "images/yule_ball/98.png"
    with d3
    pause

    hide image  "images/yule_ball/98.png"
    show image  "images/yule_ball/99.png"
    with d3
    pause

    hide image  "images/yule_ball/99.png"
    show image  "images/yule_ball/100.png"
    with d3
    pause

    hide image  "images/yule_ball/100.png"
    show image  "images/yule_ball/101.png"
    with d3
    pause

    hide image  "images/yule_ball/101.png"
    show image  "images/yule_ball/102.png"
    with d3
    pause

    hide image  "images/yule_ball/102.png"
    show image  "images/yule_ball/103.png"
    with d3
    pause

    hide image  "images/yule_ball/103.png"
    show image  "images/yule_ball/104.png"
    with d3
    pause

    hide image  "images/yule_ball/104.png"
    show image  "images/yule_ball/105.png"
    with d3
    pause

    hide image  "images/yule_ball/105.png"
    show image  "images/yule_ball/106.png"
    with d3
    pause

    hide image  "images/yule_ball/106.png"
    show image  "images/yule_ball/107.png"
    with d3
    pause

    hide image  "images/yule_ball/107.png"
    with fade
    jump end_02_men



      ### ENDING 02_02
label end02_02:
    show image  "images/yule_ball/108.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/108.png"
    show image  "images/yule_ball/109.png"
    with d3
    pause

    hide image  "images/yule_ball/109.png"
    show image  "images/yule_ball/110.png"
    with d3
    pause

    hide image  "images/yule_ball/110.png"
    show image  "images/yule_ball/111.png"
    with d3
    pause

    hide image  "images/yule_ball/111.png"
    show image  "images/yule_ball/112.png"
    with d3
    pause

    hide image  "images/yule_ball/112.png"
    show image  "images/yule_ball/113.png"
    with d3
    pause

    hide image  "images/yule_ball/113.png"
    show image  "images/yule_ball/114.png"
    with d3
    pause

    hide image  "images/yule_ball/114.png"
    show image  "images/yule_ball/115.png"
    with d3
    pause

    hide image  "images/yule_ball/115.png"
    show image  "images/yule_ball/116.png"
    with d3
    pause

    hide image  "images/yule_ball/116.png"
    show image  "images/yule_ball/117.png"
    with d3
    pause

    hide image  "images/yule_ball/117.png"
    show image  "images/yule_ball/118.png"
    with d3
    pause

    hide image  "images/yule_ball/118.png"
    show image  "images/yule_ball/119.png"
    with d3
    pause

    hide image  "images/yule_ball/119.png"
    show image  "images/yule_ball/120.png"
    with d3
    pause
    hide image  "images/yule_ball/120.png"
    show image  "images/yule_ball/121.png"
    with d3
    pause

    hide image  "images/yule_ball/121.png"
    show image  "images/yule_ball/122.png"
    with d3
    pause

    hide image  "images/yule_ball/122.png"
    show image  "images/yule_ball/123.png"
    with d3
    pause

    hide image  "images/yule_ball/123.png"
    with fade
    jump end_02_men


         ### ENDING 02_03
label end02_03:
    show image  "images/yule_ball/124.png" with d3
    show screen ctc
    pause

    hide image  "images/yule_ball/124.png"
    show image  "images/yule_ball/125.png"
    with d3
    pause

    hide image  "images/yule_ball/125.png"
    show image  "images/yule_ball/126.png"
    with d3
    pause

    hide image  "images/yule_ball/126.png"
    show image  "images/yule_ball/127.png"
    with d3
    pause

    hide image  "images/yule_ball/127.png"
    show image  "images/yule_ball/128.png"
    with d3
    pause

    hide image  "images/yule_ball/128.png"
    show image  "images/yule_ball/129.png"
    with d3
    pause

    hide image  "images/yule_ball/129.png"
    show image  "images/yule_ball/130.png"
    with d3
    pause

    hide image  "images/yule_ball/130.png"
    show image  "images/yule_ball/131.png"
    with d3
    pause

    hide image  "images/yule_ball/131.png"
    show image  "images/yule_ball/132.png"
    with d3
    pause

    hide image  "images/yule_ball/132.png"
    show image  "images/yule_ball/133.png"
    with d3
    pause

    hide image  "images/yule_ball/133.png"
    show image  "images/yule_ball/134.png"
    with d3
    pause

    hide image  "images/yule_ball/134.png"
    show image  "images/yule_ball/135.png"
    with d3
    pause

    hide image  "images/yule_ball/135.png"
    show image  "images/yule_ball/136.png"
    with d3
    pause

    hide image  "images/yule_ball/136.png"
    show image  "images/yule_ball/137.png"
    with d3
    pause
    hide image  "images/yule_ball/137.png"
    show image  "images/yule_ball/138.png"
    with d3
    pause

    hide image  "images/yule_ball/138.png"
    show image  "images/yule_ball/139.png"
    with d3
    pause

    hide image  "images/yule_ball/139.png"
    show image  "images/yule_ball/140.png"
    with d3
    pause

    hide image  "images/yule_ball/140.png"
    show image  "images/yule_ball/141.png"
    with d3
    pause

    hide image  "images/yule_ball/141.png"
    show image  "images/yule_ball/142.png"
    with d3
    pause

    hide image  "images/yule_ball/142.png"
    show image  "images/yule_ball/143.png"
    with d3
    pause

    hide image  "images/yule_ball/143.png"
    show image  "images/yule_ball/144.png"
    with d3
    pause

    hide image  "images/yule_ball/144.png"
    show image  "images/yule_ball/145.png"
    with d3
    pause

    hide image  "images/yule_ball/145.png"
    show image  "images/yule_ball/146.png"
    with d3
    pause

    hide image  "images/yule_ball/146.png"
    show image  "images/yule_ball/147.png"
    with d3
    pause

    hide image  "images/yule_ball/147.png"
    show image  "images/yule_ball/148.png"
    with d3
    pause
    hide image  "images/yule_ball/148.png"
    show image  "images/yule_ball/149.png"
    with d3
    pause

    hide image  "images/yule_ball/149.png"
    show image  "images/yule_ball/150.png"
    with d3
    pause

    hide image  "images/yule_ball/150.png"
    show image  "images/yule_ball/151.png"
    with d3
    pause

    hide image  "images/yule_ball/151.png"
    show image  "images/yule_ball/152.png"
    with d3
    pause

    hide image  "images/yule_ball/152.png"
    show image  "images/yule_ball/153.png"
    with d3
    pause

    hide image  "images/yule_ball/153.png"
    show image  "images/yule_ball/154.png"
    with d3
    pause

    hide image  "images/yule_ball/154.png"
    show image  "images/yule_ball/155.png"
    with d3
    pause

    hide image  "images/yule_ball/155.png"
    show image  "images/yule_ball/156.png"
    with d3
    pause

    hide image  "images/yule_ball/156.png"
    show image  "images/yule_ball/157.png"
    with d3
    pause

    hide image  "images/yule_ball/157.png"
    show image  "images/yule_ball/158.png"
    with d3
    pause

    hide image  "images/yule_ball/158.png"
    show image  "images/yule_ball/159.png"
    with d3
    pause

    hide image  "images/yule_ball/159.png"
    show image  "images/yule_ball/160.png"
    with d3
    pause

    hide image  "images/yule_ball/160.png"
    show image  "images/yule_ball/161.png"
    with d3
    pause

    hide image  "images/yule_ball/161.png"
    show image  "images/yule_ball/162.png"
    with d3
    pause

    hide image  "images/yule_ball/162.png"
    show image  "images/yule_ball/163.png"
    with d3
    pause

    hide image  "images/yule_ball/163.png"
    show image  "images/yule_ball/164.png"
    with d3
    pause

    hide image  "images/yule_ball/164.png"
    show image  "images/yule_ball/165.png"
    with d3
    pause

    hide image  "images/yule_ball/165.png"
    show image  "images/yule_ball/166.png"
    with d3
    pause

    hide image  "images/yule_ball/166.png"
    show image  "images/yule_ball/167.png"
    with d3
    pause

    hide image  "images/yule_ball/167.png"
    show image  "images/yule_ball/168.png"
    with d3
    pause

    hide image  "images/yule_ball/168.png"
    show image  "images/yule_ball/169.png"
    with d3
    pause

    hide image  "images/yule_ball/169.png"
    show image  "images/yule_ball/170.png"
    with d3
    pause

    hide image  "images/yule_ball/170.png"
    with fade
    jump end_02_men





init -2:
    $ music_room_playing = ""
    ### MUSIC ROOM ###
label music_room:
    python:
        music_list = [
            ["Playful Tension by Shadow16nh","music/(Orchestral) Playful Tension by Shadow16nh.mp3"],
            ["Shanghai Honey by Orange Range","music/02 - Shanghai Honey.mp3"],
            ["Introducing Colin Harry Potter OST","music/07 Introducing Colin2.mp3"],
            ["Neville's Waltz Harry Potter OST","music/11 Neville's Waltz.mp3"],
            ["The Quidditch Match Harry Potter OST","music/11 The Quidditch Match.mp3"],
            ["Anguish by Kevin MacLeod","music/Anguish.mp3"],
            ["Brittle Rille by Kevin MacLeod","music/Brittle Rille.mp3"],
            ["Chipper Doodle v2 by Kevin MacLeod","music/Chipper Doodle v2.mp3"],
            ["Dark Fog by Kevin MacLeod","music/Dark Fog.mp3"],
            ["Final Fantasy VII Game Over Theme","music/Final Fantasy 7 Game Over Theme.mp3"],
            ["Final Fantasy VII Boss Theme","music/Final Fantasy VII Boss Theme.mp3"],
            ["Hitman by Kevin MacLeod","music/Hitman.mp3"],
            ["Music for Manatees by Kevin MacLeod","music/Music for Manatees.mp3"],
            ["Plaint by Kevin MacLeod","music/Plaint.mp3"],
            ["Under-the-Radar by PhobyAk","music/Under-the-Radar by PhobyAk.mp3"]
        ]
        music_room_menu = []
        for title, file in music_list:
            if music_room_playing == file:
                music_room_menu.append( ("{image=interface/note2.png} "+title+" {image=interface/note2.png}", None) )
            else:
                music_room_menu.append( (title, file) )

        music_room_menu.append(("-No music-", "stop_music"))
        music_room_menu.append(("-Keep the current tune-", "keep"))
        result = renpy.display_menu(music_room_menu)

    if result == "stop_music":
        $ music_room_playing = ""
        stop music fadeout 1.0
        jump music_room
    if result == "keep":
        jump gallery_ht
    if not None:
        $ music_room_playing = result
        play music result fadein 1 fadeout 1

    jump music_room














    ### MESSAGES ###

label gallery_locked_ht:
    $ end_u_2_pic =  "title2.jpg" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    ">Beat the game to unlock the gallery."
    hide screen end_u_2                                             #<---- SCREEN
    show screen extras
    return
