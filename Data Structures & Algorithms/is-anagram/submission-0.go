func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    seen := make(map[string]int)

    for i := 0; i< len(s); i++ {
        if _, exists := seen[s[i:i+1]]; exists {
            seen[s[i:i+1]] = seen[s[i:i+1]] + 1
        } else {
            seen[s[i:i+1]] = 1
        }
    }

    for i := 0; i< len(t); i++ {
        if _, exists := seen[t[i:i+1]]; exists {
            seen[t[i:i+1]] = seen[t[i:i+1]] - 1
            if seen[t[i:i+1]] == 0 {
                delete(seen, t[i:i+1])
            }
        } else {
            return false;
        }
    }

    fmt.Println("Animals in the set:")
    for item := range seen {
        fmt.Printf("* %s\n", item)
    }

    if len(seen) == 0 {
        return true
    }

    return false
}
