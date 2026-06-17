from candidate import Candidate
from voter import Voter

import random
import heapq


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []

    def generate_candidates(self, count):
        names = ['Aang', 'Katara', 'Sokka', 'Zuko', 'Iroh', 'Appa', 'Momo', 'Toph', 'Azula', 'Suki', 'Ozai', 'Mai', 'Ty']
        self.candidates = [
            Candidate(
                name=names[i],
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def generate_voters(self, count):
        self.voters = [
            Voter(
                id=i + 1,
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    #function that calculates distance between voter and candidate political leaning and ranks them for each voter ballet
    def generate_ballots(self,count):
        all_ballots = []
        for voter in self.voters:
            ballot = []
            for canidate in self.candidates:
                #calculate distance
                distance = abs(voter.leaning - canidate.leaning)
                heapq.heappush(ballot, (distance,canidate))
            all_ballots.append(ballot)
        return all_ballots

    def run_election(self,ballots,num_candidates):
        losers = set()
        round = 1

        while True:
            pols = {candidate: 0 for candidate in self.candidates if candidate not in losers }
            rank = []

            #go through all first place votes
            for ballot in ballots:
                #get first choice
                for distance, candidate in ballot:
                    if candidate not in losers:
                        pols[candidate] += 1
                        break # if top choice is eliminated send vote to next highest choice
           
            total_votes = len(ballots)
            pols = {candidate: (votes/total_votes)*100 for candidate, votes in pols.items()} #candidate % score
            rank = sorted(pols, key=lambda k: pols[k], reverse=True) #candidate name sorted by % score

            print("Round: ",round)
            for candidate in rank:
                print(f"{candidate.name}: {pols[candidate]:.2f}%")
            
            print()
            round +=1

            #calculate % of highest voted candidate
            top_candidate = max(pols, key = lambda k: pols[k])#candidate name
            percentage = (pols[top_candidate]/total_votes )* 100 #candidate % score

            if percentage >= 50.0:
                return top_candidate.name, percentage
            else:
                loosing_candidate = min(pols, key = lambda k: pols[k])#candidate name
                del pols[loosing_candidate]
                #adding votes from loseing candidates to the voters
                leftover_votes = 0
                percentage = pols[top_candidate]/total_votes * 100 
                losers.add(loosing_candidate)
        


if __name__ == "__main__":
    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)
    ballots = voting_system.generate_ballots(100)

    print("Candidates:")
    for candidate in voting_system.candidates:
        print(candidate)

    print("\nVoters:")
    for voter in voting_system.voters:
        print(voter)

    print("\nElection Results:")
    winner = voting_system.run_election(ballots, 5)
    print("\nWinner:")
    print(winner[0], "with", winner[1], "% of the votes")