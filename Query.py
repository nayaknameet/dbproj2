q1 = "select sl.GameID, p.PName, sl.PNo" \
     " from world_cup.team as t, world_cup.game as g," \
     " world_cup.player as p, world_cup.starting_lineups as sl" \
     " where p.Team = '{}' and sl.TeamID = p.TeamID  and sl.PNo = p.PNo group by sl.GameID, sl.PNo Asc;"

q2 = "SELECT distinct c.GameID, p.PName " \
     "from world_cup.cards as c, world_cup.game as g, world_cup.player as p " \
     "where p.Team = '{}' and c.Color = '{}' and c.TeamID = p.TeamID and c.PNo = p.PNo;"