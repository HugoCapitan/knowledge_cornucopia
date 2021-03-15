def find_permutations(a_str = "", b_str = ""):
    print(f'Checking for all permutations of "{a_str}" in \n "{b_str}" \n')
    
    freq_table = init_freq_table(a_str)
    found_perms = []
    occ_counter = 0
    
    beggining = 0
    
    for end in range(len(b_str)):
        occ_counter += add_occurrence(freq_table, b_str[end])
        
        if end - beggining == len(a_str) - 1:
            check_for_permutation(occ_counter, beggining, end, a_str, b_str, found_perms)
            occ_counter -= remove_occurrence(freq_table, b_str[beggining])
            beggining += 1

            
def add_occurrence(freq_table, char):
    if char in freq_table:
        val_for_occ = freq_table.get(char)
        if val_for_occ[1] < val_for_occ[0]:
            freq_table[char][1] += 1
            return 1
        else:
            freq_table[char][2] += 1
    
    return 0
        


def remove_occurrence(freq_table, char):
    if char in freq_table:
        val_for_occ = freq_table.get(char)
        if val_for_occ[2] == 0:
            freq_table[char][1] -= 1
            return 1
        else:
            freq_table[char][2] -= 1
            
    return 0


def check_for_permutation(occ_counter, begging, end, a_str, b_str, found):
    if occ_counter == len(a_str):
        print("FOUND ONE!", b_str[begging:end + 1])
        found.append(begging)
    

# O(n)
def init_freq_table(a_str):
    freq_table = {}
    
    for char in a_str:
        if char not in freq_table:
            freq_table[char] = [0, 0, 0]
            
        freq_table[char][0] += 1
        
    return freq_table
            

if __name__ == '__main__':
    find_permutations(
        'abbc',
        'abbabcbabbccbacbb'
    )
