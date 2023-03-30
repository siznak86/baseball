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

