class Weiji():
    def __init__(self):
        self.Word2Num()

    def Word2Num(self):
        self.word = [chr(i) for i in range(97, 123)]

    def jiami(self, w, k):
        W = [self.word.index(item) for item in w]
        K = [self.word.index(item) for item in k]
        KeyLen = len(K)
        M = [(W[i] + K[i % KeyLen]) % 26 for i in range(len(W))]
        m = [self.word[i] for i in M]
        return ''.join(m)

    def jiemi(self, m, k):
        M = [self.word.index(item) for item in m]
        K = [self.word.index(item) for item in k]
        KeyLen = len(K)
        W = [(M[i] - K[i % KeyLen]) % 26 for i in range(len(M))]
        w = [self.word[i] for i in W]
        return ''.join(w)

# Sys = Weiji()
# w = input('明文：')
# k = input('Key：')
# print(Sys.jiami(w, k))
# w = input('密文：')
# k = input('Key：')
# print(Sys.jiemi(w, k))
