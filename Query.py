q1 = "select GameID, PNo, PName" \
     " from(select g.GameId,  sl.PNo, p.PName " \
     "from world_cup.game as g, world_cup.team as t," \
     " world_cup.starting_lineups as sl, world_cup.player as p " \
     "where t.TeamID = g.TeamID1 and t.Team = '{}' and g.GameID = sl.GameID" \
     " and p.TeamID = sl.TeamID and p.PNo = sl.PNo " \
     "union " \
     "select g.GameId,  sl.PNo, p.PName from world_cup.game as g, world_cup.team as t, " \
     "world_cup.starting_lineups as sl, world_cup.player as p where t.TeamID = g.TeamID2 and t.Team = '{}' and g.GameID = sl.GameID and " \
     "p.TeamID = sl.TeamID and p.PNo = sl.PNo) as results order by GameID, PNo;"

q2 = "SELECT distinct c.GameID, p.PName " \
     "from world_cup.cards as c, world_cup.game as g, world_cup.player as p " \
     "where p.Team = '{}' and c.Color = '{}' and c.TeamID = p.TeamID and c.PNo = p.PNo;"