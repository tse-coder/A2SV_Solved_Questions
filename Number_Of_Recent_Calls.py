class RecentCounter:

    def __init__(self):
        self.recent_requests = []
    
    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        i = len(self.recent_requests) - 1
        count = 0
        while i >= 0 and self.recent_requests[i] > t - 3001:
            count += 1
            i -= 1
        return count

