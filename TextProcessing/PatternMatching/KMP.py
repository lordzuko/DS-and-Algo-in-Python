def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m                      # by default, presume overlap of 0 everywhere
    j = 1
    k = 0

    while j < m:                        # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def find_kmp(T,P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    if m == 0: return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if k == m-1:
            return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1