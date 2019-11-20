class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, n):
        print('New rank: ', n, '    Old rank: ', self.rank)
        print('Old progr: ', self.progress)
        if n >= 9 or n < -8 or n == 0:
            raise

        if(self.rank == 8):
            return

        #if self.rank - 2 >= n:
        #    return
        #
        #!!!!!  dddddd
        #
        d = n - self.rank
        if  self.rank > 0 and n < 0:
                d += 1
        if d <= -2:
            return

        if (n > self.rank): 
            d = n - self.rank
            if self.rank < 0 and n > 0:
                d -= 1
            prog = 10 * d * d
            self.progress += prog

        if n == self.rank:
            self.progress += 3

        if n < self.rank:
            self.progress += 1

        while(self.progress >= 100):
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0

if __name__ == "__main__":
    user = User()
    user.rank = 7
    user.progress = 91
    user.inc_progress(8)

