class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, n):
        print('New rank: ', n)
        if(self.rank == 8):
            return

        if self.rank - 2 >= n:
            return
        #
        #!!!!!  dddddd
        #

        if (n > self.rank): 
            d = n - self.rank
            if self.rank < 0 and n > 0:
                d -= 1
            prog = 10 * d * d
            self.progress += prog

        if n == self.rank:
            self.progress += 3

        while(self.progress >= 100):
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
        while self.rank > 9:
            self.rank -= 1

if __name__ == "__main__":
    user = User()
    print(user.rank)
    print(user.progress)
    user.inc_progress(-8)
    print(user.progress)
