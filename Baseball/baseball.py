import math

# standard variables
name = 
team =
g =

# batting variables
ab = # at bats
r = # runs
sing = # singles
doub = # doubles
trip = # triples
hr = # home runs
rbi = # runs batted in
bb = # base on balls
ibb = # intentional base on balls
so = # strike outs
cs = # caught stealing
hbp = # hit by pitch
sac = #sac bunt
sf = # sac fly
go = # ground out
fo = # fly out
gidp = # ground into double play

# batting stats
h = sing + doub + trip + hr # hits
avg = h/ab # batting average
obp = (h + bb + hbp) / (ab + bb + hbp + sf) # on base percentage
slg = (s + (2*doub) + (3*trip) + (4*hr)) / ab # slugging percentage
ops = obp + slg # on base plus slugging
xbh = # extra base hits
gtf = go / fo # ground out to fly out ratio
tb = h + bb + hbp # touched base

# advanced batting stats
gtar = 