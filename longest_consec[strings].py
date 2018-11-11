def longest_consec(x):

# Given an array of strings, return the the two consecutive strings 
# that, when joined, make the longest string possible
    
    first_s = x[0]                               
    second_s = x[1]
    longest = first_s + second_s

    for value in x(range(2,-1)):
        if len(second_s) + len(value)>len(longest):
            first_s = second_s
            second_s = value
            longest = first_s + second_s
        else:
            continue
    
    print(len(longest),longest)
    return longest


given_a = ['hat','abigail','theta','hero','balthazar','dragonslayer','tartarus']

longest_consec(given_a)