class Route():
    star        = (int, int)
    end         = (int, int)
    distanciakm = int
    timeAprox   = int
    
    def __init__(self, star, end, distanciakm, timeAprox):
        self.star   = star
        self.end    = end
        self.distanciakm = distanciakm
        self.timeAprox =timeAprox
        