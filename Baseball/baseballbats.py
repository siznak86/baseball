import math

# Batting statistics
single =            # 1B – Single: hits on which the batter reaches first base safely without the contribution of a fielding error
double =            # 2B – Double: hits on which the batter reaches second base safely without the contribution of a fielding error
triple =            # 3B – Triple: hits on which the batter reaches third base safely without the contribution of a fielding error
hr =                # HR – Home runs: hits on which the batter successfully touched all four bases, without the contribution of a fielding error
bb =                # BB – Base on balls (also called a "walk"): hitter not swinging at four pitches called out of the strike zone and awarded first base.
so =                # K – Strike out (also abbreviated SO): number of times that a third strike is taken or swung at and missed, or bunted foul. Catcher must catch the third strike or batter may attempt to run to first base.
ab =                # AB – At bat: plate appearances, not including bases on balls, being hit by pitch, sacrifices, interference, or obstruction
abphr = ab / hr     # AB/HR – At bats per home run: at bats divided by home runs
h = (single + double + triple + hr)                             # H – Hit: reaching base because of a batted, fair ball without error by the defense
avg = h / ab        # BA – Batting average (also abbreviated AVG): hits divided by at bats (H/AB)
r =                 # R – Runs scored: number of times a player crosses home plate
rc =                # RC – Runs created: an attempt to measure how many runs a player has contributed to their team
rp =                # RP – Runs produced: an attempt to measure how many runs a player has contributed
rbi =               # RBI – Run batted in: number of runners who score due to a batter's action, except when the batter grounded into a double play or reached on an error
risp =              # RISP – Runner in scoring position: a breakdown of a batter's batting average with runners in scoring position, which includes runners at second or third base
sf =                # SF – Sacrifice fly: fly balls hit to the outfield which, although caught for an out, allow a baserunner to advance
sh =                # SH – Sacrifice hit: number of sacrifice bunts which allow runners to advance on the basepaths
babip = (h - hr)/(ab - so - hr + sf)                            # BABIP – Batting average on balls in play: frequency at which a batter reaches a base after putting the ball in the field of play. Also a pitching category.
bbpk = bb / so      # BB/K – Walk-to-strikeout ratio: number of bases on balls divided by number of strikeouts
# BsR – Base runs: Another run estimator, like runs created
# EQA – Equivalent average: a player's batting average absent park and league factors
fc =                # FC – Fielder's choice: times reaching base safely because a fielder chose to try for an out on another runner
go =                # GO - Ground ball out 
fo =                # FO - Fly ball out
gopfo = go / fo     # GO/AO – Ground ball fly ball ratio: number of ground ball outs divided by number of fly ball outs
gdp =              # GDP or GIDP – Ground into double play: number of ground balls hit that became double plays
# GPA – Gross production average: 1.8 times on-base percentage plus slugging percentage, divided by four
gds =               # GS – Grand slam: a home run with the bases loaded, resulting in four runs scoring, and four RBIs credited to the batter
hbp =               # HBP – Hit by pitch: times touched by a pitch and awarded first base as a result
hrph = hr / h       # HR/H – Home runs per hit: home runs divided by total hits
ithphr =            # ITPHR – Inside-the-park home run: hits on which the batter successfully touched all four bases, without the contribution of a fielding error or the ball going outside the ball park.
ibb =               # IBB – Intentional base on balls: times awarded first base on balls (see BB above) deliberately thrown by the pitcher. Also known as IW (intentional walk).
iso = (double + (2 * triple) + (3 * hr)) / ab                    # ISO – Isolated power: a hitter's ability to hit for extra bases, calculated by subtracting batting average from slugging percentage
lob =               # LOB – Left on base: number of runners neither out nor scored at the end of an inning
obp = (h + bb + hbp) / (ab + bb + hbp + sf)                      # OBP – On-base percentage: times reached base (H + BB + HBP) divided by at bats plus walks plus hit by pitch plus sacrifice flies (AB + BB + HBP + SF)
slg = (single + (2*double) + (3*triple) + (4*hr)) / ab           # SLG – Slugging percentage: total bases achieved on hits divided by at-bats (TB/AB)
ops = obp + slg     # OPS – On-base plus slugging: on-base percentage plus slugging average
pa =                # PA – Plate appearance: number of completed batting appearances
papso = pa / so     # PA/SO – Plate appearances per strikeout: number of times a batter strikes out to their plate appearance
tb = [single + (2 * double) + (3 * triple) + (4 * hr)]           # TB – Total bases: one for each single, two for each double, three for each triple, and four for each home run [H + 2B + (2 × 3B) + (3 × HR)] or [1B + (2 × 2B) + (3 × 3B) + (4 × HR)]
tob = (h + bb + hbp)     # TOB – Times on base(Touched Base): times reaching base as a result of hits, walks, and hit-by-pitches (H + BB + HBP)
xbh = (double + triple + hr)        # XBH – Extra base hits: total hits greater than singles (2B + 3B + HR)
bbp = bb / pa       # BB% - Walk percentage: Base on balls per plate apperance
sop = so / pa       # SO% - Strike out percentage: Strike out per plate apperance

# Baserunning statistics
sb =                # SB – Stolen base: number of bases advanced by the runner while the ball is in the possession of the defense
cs =                # CS – Caught stealing: times tagged out while attempting to steal a base
sba = (sb + cs)     # SBA or ATT – Stolen base attempts: total number of times the player has attempted to steal a base (SB+CS)
sbp = sb / sba      # SB% – Stolen base percentage: the percentage of bases stolen successfully. (SB) divided by (SBA) (stolen bases attempted).
di =                # DI – Defensive Indifference: if the catcher does not attempt to throw out a runner (usually because the base would be insignificant), the runner is not awarded a steal. Scored as a fielder's choice.
r =                 # R – Runs scored: times reached home plate legally and safely
ubr =               # UBR – Ultimate base running: a metric that assigns linear weights to every individual baserunning event in order to measure the impact of a player's baserunning skill
ta = [(tb + bb + hbp + sb -cs) / (ab - h + cs + gdp)]            # TA – Total average: total bases, plus walks, plus hit by pitch, plus steals, minus caught stealing divided by at bats, minus hits, plus caught stealing, plus grounded into double plays [(TB + BB + HBP + SB – CS)/(AB – H + CS + GIDP)]

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
ra = (r * 9) / ip           # RA – Run average: number of runs allowed times nine divided by innings pitched
sho =               # SHO – Shutout: number of complete games pitched with no runs allowed
# SIERA – Skill-Interactive Earned Run Average: another advanced stat that measures pitching. SIERA builds on FIP and xFIP by taking a deeper look at what makes pitchers better.
sv =                # SV – Save: number of games where the pitcher enters a game led by the pitcher's team, finishes the game without surrendering the lead, is not the winning pitcher, and either (a) the lead was three runs or fewer when the pitcher entered the game; (b) the potential tying run was on base, at bat, or on deck; or (c) the pitcher pitched three or more innings
svo =               # SVO – Save opportunity: When a pitcher 1) enters the game with a lead of three or fewer runs and pitches at least one inning, 2) enters the game with the potential tying run on base, at bat, or on deck, or 3) pitches three or more innings with a lead and is credited with a save by the official scorer # W + S – Wins in relief + saves.
# whiff rate: a term, usually used in reference to pitchers, that divides the number of pitches swung at and missed by the total number of swings in a given sample. If a pitcher throws 100 pitches at which batters swing, and the batters fail to make contact on 26 of them, the pitcher's whiff rate is 26%.
whip = (bba + ha) / ip      # WHIP – Walks and hits per inning pitched: average number of walks and hits allowed by the pitcher per inning
wp =                # WP – Wild pitches: charged when a pitch is too high, low, or wide of home plate for the catcher to field, thereby allowing one or more runners to advance or score

# Fielding statistics
# A – Assists: number of outs recorded on a play where a fielder touched the ball, except if such touching is the putout
# CI – Catcher's Interference (e.g., catcher makes contact with bat)
# DP – Double plays: one for each double play during which the fielder recorded a putout or an assist.
# E – Errors: number of times a fielder fails to make a play he should have made with common effort, and the offense benefits as a result
# FP – Fielding percentage: total plays (chances minus errors) divided by the number of total chances
# INN – Innings: number of innings that a player is at one certain position
# PB – Passed ball: charged to the catcher when the ball is dropped and one or more runners advance
# PO – Putout: number of times the fielder tags, forces, or appeals a runner and he is called out as a result
# RF – Range factor: 9*(putouts + assists)/innings played. Used to determine the amount of field that the player can cover
# TC – Total chances: assists plus putouts plus errors
# TP – Triple play: one for each triple play during which the fielder recorded a putout or an assist
# UZR – Ultimate zone rating: the ability of a player to defend an assigned "zone" of the field compared to an average defensive player at his position

# Overall player value
# VORP – Value over replacement player: a statistic that calculates a player's overall value in comparison to a "replacement-level" player. There are separate formulas for players and pitchers
# Win shares: a complex metric that gauges a player's overall contribution to his team's wins
# WAR – Wins above replacement: a non-standard formula to calculate the number of wins a player contributes to his team over a "replacement-level player"
# PWA – Player Win Average: performance of players is shown by how much they increase or decrease their team's chances of winning a specific game[4]
# PGP – Player Game Percentage: defined as, "the sum of changes in the probability of winning the game for each play in which the player has participated"[4]

# General statistics
# G – Games played: number of games where the player played, in whole or in part
# GS – Games started: number of games a player starts
# GB – Games behind: number of games a team is behind the division leader
# Pythagorean expectation: estimates a team's expected winning percentage based on runs scored and runs allowed