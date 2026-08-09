def contains_subset_freq(full: dict, subset: dict) -> bool:
    for key, value in subset.items():
        if key not in full or value > full[key]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for val_t in t:
            t_freq[val_t] = t_freq.get(val_t, 0) + 1

        current_freq = {}
        l = 0
        min_output = None
        min_start, min_end = -1, -1
        for r, val in enumerate(s):
            if val in t:
                current_freq[val] = current_freq.get(val, 0) + 1

            if contains_subset_freq(current_freq, t_freq):
                experiment_freq = current_freq.copy()
                while l <= r:
                    if contains_subset_freq(experiment_freq, t_freq):
                        if min_output is None or r - l < (min_end - min_start):
                            min_start = l
                            min_end = r
                            min_output = "1"
                    else:
                        break

                    if s[l] in t_freq:
                        experiment_freq[s[l]] -= 1

                    l += 1
                current_freq = experiment_freq

        return "" if min_output is None else s[min_start : min_end + 1]
        

        