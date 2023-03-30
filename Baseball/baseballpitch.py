import math

# Pitching statistics
w =                 # W – Win: number of games where pitcher was pitching while their team took the lead and went on to win, also the starter needs to pitch at least 5 innings of work (also related: winning percentage)
l =                 # L - Loss: number of games where pitcher was pitching while the opposing team took the lead, never lost the lead, and went on to win
g =                 # G – Games (AKA "appearances"): number of times a pitcher pitches in a season
ip =                # IP – Innings pitched: the number of outs a team gets while a pitcher is pitching divided by 3
bba =                # BB – Base on balls (also called a "walk"): times pitching four balls, allowing the batter to take first base
bbpn = (bb * 9) / ip        # BB/9 – Bases on balls per 9 innings pitched: base on balls multiplied by nine, divided by innings pitched
bf =                # BF – Total batters faced: opponent team's total plate appearances
bk=                 # BK – Balk: number of times pitcher commits an illegal pitching action while in contact with the pitching rubber as judged by umpire, resulting in baserunners advancing one base
bs=                 # BS – Blown save: number of times entering the game in a save situation, and being charged the run (earned or not) which eliminates his team's lead
erc = 9 * [((h + bb + hbp) * ptb)/(bfp * ip)] - .56             # CERA – Component ERA: an estimate of a pitcher's ERA based upon the individual components of his statistical line (K, H, 2B, 3B, HR, BB, HBP)
cg =                # CG – Complete game: number of games where player was the only pitcher for their team
dice =              # DICE – Defense-Independent Component ERA: an estimate of a pitcher's ERA based upon the defense-independent components of his statistical line (K, HR, BB, HBP) but which also uses number of outs (IP), which is not defense independent.
er =                # ER – Earned run: number of runs that did not occur as a result of errors or passed balls
era = (er * 9) / ip         # ERA – Earned run average: total number of earned runs (see "ER" above), multiplied by 9, divided by innings pitched
erap =              # ERA+ – Adjusted ERA+: earned run average adjusted for the ballpark and the league average
# FIP – Fielding independent pitching: a metric, scaled to resemble an ERA, that focuses on events within the pitcher's control – home runs, walks, and strikeouts – but also uses in its denominator the number of outs the team gets (see IP), which is not entirely within the pitcher's control.
# xFIP: This variant substitutes a pitcher's own home run percentage with the league average
gf =                # GF – Games finished: number of games pitched where player was the final pitcher for their team as a relief pitcher
gidp =              # GIDP – Double plays induced: number of double play groundouts induced
gidpo =             # GIDPO – Double play opportunities: number of groundout induced double play opportunities
gir =               # GIR – Games in relief: games as a non starting pitcher
# GO/AO or G/F – Ground Out to Air Out ratio, aka Ground ball fly ball ratio: ground balls allowed divided by fly balls allowed
gs =                # GS – Starts: number of games pitched where player was the first pitcher for their team
ha =                # H (or HA) – Hits allowed: total hits allowed
hpn = (ha * 9 ) / ip        # H/9 (or HA/9) – Hits allowed per 9 innings pitched: hits allowed times nine divided by innings pitched (also known as H/9IP)
hb =                # HB – Hit batsman: times hit a batter with pitch, allowing runner to advance to first base
hld =               # HLD (or H) – Hold: number of games entered in a save situation, recorded at least one out, did not surrender the lead, and did not complete the game
hra =               # HR (or HRA) – Home runs allowed: total home runs allowed
hrpn = (hra * 9) / ip       # HR/9 (or HRA/9) – Home runs per nine innings: home runs allowed times nine divided by innings pitched (also known as HR/9IP)
ibba =              # IBB – Intentional base on balls allowed
avgip = ip / gs     # IP/GS – Average number of innings pitched per game started
ir =                # IR – Inherited runners: number of runners on base when the pitcher enters the game
ira =               # IRA – Inherited runs allowed: number of inherited runners allowed to score
k =                 # K (or SO) – Strikeout: number of batters who received strike three
kpn = (k * 9) / ip          # K/9 (or SO/9) – Strikeouts per 9 innings pitched: strikeouts times nine divided by innings pitched
kpb = k / bba       # K/BB (or SO/BB) – Strikeout-to-walk ratio: number of strikeouts divided by number of base on balls
# LOB% – Left-on-base percentage: LOB% represents the percentage of baserunners a pitcher does not allow to score. LOB% tends to regress toward 70–72% over time, so unusually high or low percentages could indicate that pitcher's ERA could be expected to rise or lower in the future. An occasional exception to this logic is a pitcher with a very high strikeout rate.[3]
oba = ha / ab       # OBA (or just AVG) – Opponents batting average: hits allowed divided by at-bats faced
pc = # PIT (or NP) – Pitches thrown (Pitch count)
# PC-ST – An individual pitcher's total game pitches [Pitch Count] and [ST] his no. of strikes thrown within that PC.
pfr = (k + bba) / ip        # PFR – Power finesse ratio: The sum of strikeouts and walks divided by innings pitched.
# pNERD – Pitcher's NERD: expected aesthetic pleasure of watching an individual pitcher
# QOP – Quality of pitch: comprehensive pitch evaluation statistic which combines speed, location and movement (rise, total break, vertical break and horizontal break) into a single numeric value
# QS – Quality start: a game in which a starting pitcher completes at least six innings and permits no more than three earned runs
r =                 # Runs
ra = (r * 9) / ip           # RA – Run average: number of runs allowed times nine divided by innings pitched
sho =               # SHO – Shutout: number of complete games pitched with no runs allowed
# SIERA – Skill-Interactive Earned Run Average: another advanced stat that measures pitching. SIERA builds on FIP and xFIP by taking a deeper look at what makes pitchers better.
sv =                # SV – Save: number of games where the pitcher enters a game led by the pitcher's team, finishes the game without surrendering the lead, is not the winning pitcher, and either (a) the lead was three runs or fewer when the pitcher entered the game; (b) the potential tying run was on base, at bat, or on deck; or (c) the pitcher pitched three or more innings
svo =               # SVO – Save opportunity: When a pitcher 1) enters the game with a lead of three or fewer runs and pitches at least one inning, 2) enters the game with the potential tying run on base, at bat, or on deck, or 3) pitches three or more innings with a lead and is credited with a save by the official scorer # W + S – Wins in relief + saves.
# whiff rate: a term, usually used in reference to pitchers, that divides the number of pitches swung at and missed by the total number of swings in a given sample. If a pitcher throws 100 pitches at which batters swing, and the batters fail to make contact on 26 of them, the pitcher's whiff rate is 26%.
whip = (bba + ha) / ip      # WHIP – Walks and hits per inning pitched: average number of walks and hits allowed by the pitcher per inning
wp =                # WP – Wild pitches: charged when a pitch is too high, low, or wide of home plate for the catcher to field, thereby allowing one or more runners to advance or score
