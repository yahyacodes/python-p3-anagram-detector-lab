class Anagram:
    def __init__(self, contest):
        self.contest = contest.lower()

    def match(self, contest):
        return [content for content in contest if self.anagram(content)]
    
    def anagram(self, content):
        content_lower = content.lower()

        if len(self.contest) != len(content_lower):
            return False

        return sorted(self.contest) == sorted(content_lower) 