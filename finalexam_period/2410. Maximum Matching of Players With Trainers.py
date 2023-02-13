class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pt_trainer, count = 0, 0
        for player in players:
            while pt_trainer < len(trainers) and player > trainers[pt_trainer]: 
                pt_trainer += 1
            if pt_trainer >= len(trainers):
                break
            if player <= trainers[pt_trainer]:
                count += 1
                pt_trainer += 1
            
        return count
        
