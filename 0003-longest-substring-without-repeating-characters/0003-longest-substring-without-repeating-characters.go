func max(i, j  int) int {
    if i > j{
        return i
    }
    return j
}

func lengthOfLongestSubstring(s string) int {  

    mp := make(map[string]int)
    j := 0
    mx := 0
    for i := 0 ; i < len(s) ; i++ {
        ch := s[i : i+1]
        if _, present := mp[ch]; present {
            j = max(mp[ch]+1,j)
        }
        mx = max(mx, i-j+1)
        mp[ch] = i
    }
    return mx

}