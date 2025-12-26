# picoCTF - Crack the Power (Medium)
# Safe & ethical solution script (flag not included)

from Crypto.Util.number import long_to_bytes

def integer_nth_root(x, n):
    """
    Computes the integer n-th root of x using binary search.
    """
    low = 0
    high = x
    while low <= high:
        mid = (low + high) // 2
        if mid ** n < x:
            low = mid + 1
        elif mid ** n > x:
            high = mid - 1
        else:
            return mid
    return high

def main():
    # Example placeholder values (actual challenge values not shared)
    e = 3
    ciphertext = 0  # replace with challenge ciphertext for practice

    m = integer_nth_root(ciphertext, e)
    plaintext = long_to_bytes(m)

    print("Recovered plaintext (bytes):", plaintext)

if __name__ == "__main__":
    main()
