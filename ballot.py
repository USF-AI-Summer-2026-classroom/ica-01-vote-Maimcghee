from candidate import Candidate
import voter

class Ballot:
    def __init__(self, thisVoter,candidates):
        self.voter = thisVoter
        self.candidates = candidates
        self.rank = []

        for candidate in self.candidates:
            distance = abs(self.voter.leaning - candidate.leaning)
            self.rank.append((distance, candidate))

        self.rank = sorted(self.rank, key=lambda x: x[0])

    
    def __repr__(self):
        return ("\n".join([f"Distance: {distance:.3f}, Candidate: {candidate.name}" for distance, candidate in self.rank])
        )