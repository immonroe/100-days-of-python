print('''
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,'                         ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'  spb                          ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
''')
print("Welcome to the Island of Fate.")
print("Your goal is to pass judgement and escape!") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇



one = input("You wake up on an island and there are demons coming from portals in the sky trying to kill you.\nAs you are run into the woods to hide, you see two hidden doors behind some trees. Which door do you open?\nType 'left' or 'right'\n")
if one == "left" or "Left":
  two = input("You get to the second room and you see a giant behemoth. What do you do? Type 'fight' or 'hide'\n")
  if two == "hide" or "Hide":
    three = input("The behemoth slowly walks away and you sneak into the third room. You see two women fighting, who do you help? Type 'madam' or 'dame'\n")
    if three == "dame" or "Dame":
      four = input("Dame thanks you and provides you with wisdom on how to escape the island. She says 'You will win this fight but not on your own strength.'\nYou enter the final room with Dame and there are no demons but you see a shadowy figure staring at you. What do you do? Type 'reason' or 'fight'\n")
      if four == "reason" or "Reason":
        five = input("As you walk closer to the creature you see that it is a direct reflection of you. It is a manifestation of all of the anger you hold within yourself.\nThe evil you prepares for a final battle. You are prompted to choose a weapon to decide your fate. Which weapon do you choose? Type 'scythe', 'sword', 'crossbow', or '?'\n")
        if five == '?':
          print("You choose to walk towards the shadowy figure without a weapon at all. The figure is startld by your faith. It lunges to attack you but a strong beam of light begins to radiate from you.\n'You finally understand. Violence won't end this cruel cycle. There is enough suffereing in this world. Sometimes the best way to fight is by laying your arms down' says Dame.\nYou grab the shadowy figure and it slowly dissolves as the light continues illuminating from you. You completed the trial and the island returns to normal. You win!")
        else:
          print("You grab a weapon and the shadowy figure lets out a loud laugh. 'You learned nothing. Only repeating an endless cycle that will last for eternity. HAHAHAHA'.\nThe shadowy figure turns your weapon in to shackles and says 'You will always be my slave.' He tosses you into a pool of lava and you come out as a demon.\nYou spend eternity wandering and taking your anger out on others who visit the island. Game over.")
      else:
        print("Madam puts her head down knowing your fate. The shadowy figure lunges at you and kills you. Game over.")
    else:
      print("Madam thanks you and offers you stale bread and a place to lie your head after a long journey. While you are resting, she beheads you and takes all of your belongings. Game over.")
  else:
    print("You taunt the beast and expect a very intense battle, you suddenly remember that you have no idea how to fight. You get trampled and die instantly. Game over.")
    
else:
  print("You enter the door and a demon by the name of Leigon awaits you. He gives a slight smirks and proceeds to kill you swiftly. Game over.")