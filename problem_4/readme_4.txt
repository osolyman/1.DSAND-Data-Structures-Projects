From the concept of groups, children and subgroups, it's clear that we are dealing with a tree.

We traverse every level of this tree to find the user.

Using the recursive function is very useful, as it allows us to perform the same check within every subgroup of the main group.

Time Complexity:    It could be O(i*n) because we may need to traverse through all groups denoted by "i" and 
                    through all users in each group denoted by "n".

Space Complexity:   It could be O(n), where "n" represents the depth of the group or the tree. So, in the worst case, we
                    may require space for "n" times recursive function calls.