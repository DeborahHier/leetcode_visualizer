
# Sliding Window


## Longest Substring Without Repeating Characters
- [LC #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
- Given a string `s`, find the length of the longest substring without duplicate characters.

### Solution Walkthrough
- start by initializing `left` and `max_len` to 0, and `seen` as an empty dict
- `right` will be the current index while looping through `s`

```mermaid
flowchart TD
    D[Loop over each char in s] --> E{"Is char in seen AND seen[char] >= left?"}
    E -->|Yes| F["Move left to seen[char] + 1"]
    E -->|No| G[Keep left as is]
    F --> H["Update seen[char] = right"]
    G --> H["Update seen[char] = right"]
    H --> I["Update max_len = max(max_len, right - left + 1)"]
    I-->X[Are we done looping through s?]
    X -->|no| D
    X -->|yes| J[Return max_len]
```