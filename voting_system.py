from ballot import Ballot
from candidate import Candidate
from voter import Voter

import random



class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []
        self.Allballots = []

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
    def generate_ballots(self):
        self.Allballots = [
            Ballot(
                thisVoter = voter,
                candidates = self.candidates
            )
            for voter in self.voters
        ]
        return self.Allballots

    def run_election(self,ballots,num_candidates):
        losers = set()
        round = 1
        prev_pol = None

        while True:
            pols = {candidate: 0 for candidate in self.candidates if candidate not in losers }
           
            #go through all first place votes
            for ballot in ballots:
                for distance, candidate in ballot.rank:
                    if candidate not in losers:
                        pols[candidate] += 1
                        break # if top choice is eliminated send vote to next highest choice
           
            total_votes = len(ballots)
            pols = {candidate: (votes/total_votes)*100 for candidate, votes in pols.items()} 
            rank = sorted(pols, key=lambda k: pols[k], reverse=True) 

            print("Round: ",round)
            for candidate in rank:
                print(f"{candidate.name}: {pols[candidate]:.2f}%")
            
            print()
            round +=1

            #calculate % of highest voted candidate
            top_candidate = rank[0]
            percentage = pols[top_candidate]

            if percentage >= 50.0:
                #in case of a tie
                winners = [candidate for candidate in pols if pols[candidate] == percentage]
                if len(winners) > 1 and prev_pol:
                    win = max(winners, key=lambda candidate: prev_pol[candidate])
                else:
                    win = top_candidate
                return win.name, percentage
            else:
                losing_candidate = min(pols, key = lambda k: pols[k])
                losers.add(losing_candidate)
                prev_pol = pols
        


if __name__ == "__main__":
    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)
    ballots = voting_system.generate_ballots()

    print("\nElection Results:")
    winner = voting_system.run_election(ballots, 5)
    print("\nWinner:")
    print(winner[0], "with", winner[1], "% of the votes")