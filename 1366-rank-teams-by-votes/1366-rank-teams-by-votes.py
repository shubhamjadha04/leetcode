
class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        n = len(votes[0])
        dic = {}

        # Initialize each team with position counts
        for team in votes[0]:
            dic[team] = [0] * n

        # Count votes for each position
        for vote in votes:
            for i, team in enumerate(vote):
                dic[team][i] += 1

        # Sort based on position counts
        result = sorted(
            dic.keys(),
            key=lambda team: (dic[team], -ord(team)),
            reverse=True
        )

        return "".join(result)
