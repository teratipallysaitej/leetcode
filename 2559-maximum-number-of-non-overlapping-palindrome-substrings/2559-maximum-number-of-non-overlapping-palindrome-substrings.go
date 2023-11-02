

func maxPalindromes(s string, k int) int {
	res := 0
	lastp := -1
	n := len(s)

	helper := func(l, r *int) {
		for *l >= 0 && *r < n && s[*l] == s[*r] && *l > lastp {
			if *r-*l+1 >= k {
				res++
				lastp = *r
				break // find the shortest palindrome
			} else {
				*l--
				*r++
			}
		}
	}

	for i := 0; i < len(s); i++ {
		l, r := i, i // odd length
		helper(&l, &r)
		l, r = i, i+1 // even length
		helper(&l, &r)
	}
	return res
}

