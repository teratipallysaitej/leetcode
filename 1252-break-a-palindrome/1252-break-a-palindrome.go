func breakPalindrome(p string) string {
    runes := []rune(p)
    n := len(runes)
    if n == 1 {
        return ""
    }

    for i := 0; i < n/2; i++ {
        if runes[i] != 'a' {
            runes[i] = 'a'
            return string(runes)
        }
    }

    runes[n-1] = 'b'
    return string(runes)
}