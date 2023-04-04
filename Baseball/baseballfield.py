import math

# Fielding statistics
a =     # A – Assists: number of outs recorded on a play where a fielder touched the ball, except if such touching is the putout
ci =    # CI – Catcher's Interference (e.g., catcher makes contact with bat)
dp =    # DP – Double plays: one for each double play during which the fielder recorded a putout or an assist.
e =     # E – Errors: number of times a fielder fails to make a play he should have made with common effort, and the offense benefits as a result
fp =    # FP – Fielding percentage: total plays (chances minus errors) divided by the number of total chances
inn =   # INN – Innings: number of innings that a player is at one certain position
pb =    # PB – Passed ball: charged to the catcher when the ball is dropped and one or more runners advance
po =    # PO – Putout: number of times the fielder tags, forces, or appeals a runner and he is called out as a result
rf = (9 * (po + a)) / inn       # RF – Range factor: 9*(putouts + assists)/innings played. Used to determine the amount of field that the player can cover
tc = a + po + e                 # TC – Total chances: assists plus putouts plus errors
tp =    # TP – Triple play: one for each triple play during which the fielder recorded a putout or an assist
uzr =   # UZR – Ultimate zone rating: the ability of a player to defend an assigned "zone" of the field compared to an average defensive player at his position
