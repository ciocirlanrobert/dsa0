Task 0 :
Compute the length of the calls list and then print twice the asked information. O(1 + 2) = O(3) which is actually O(1).





Task 1:
Declare the dictionary where I store the phone numbers(O(1)), then Let N = number of rows in the texts file and M = number of rows in calls file.
Iterate through every row in texts and mark twice two telephone numbers in the dictionary ( O(2*N) ).
Do the same thing for calls ( O(2*M) ).
Store the number of unique numbers (O(1)) and print them (O(1)).

The overall complexity: O(1 + 2*N + 2*M + 1 + 1) which would be O(n) where n = max(N,M);





Task 2:
Let N = number of rows in calls file
Let M = number of unique telephone numbers


The function get_duration_for_numbers executes 2 lines for every row in calls files, which means O(2*N) => O(N)

The function get_max_duration iterates through a dictionary with M unique elements, does two assignements for every element, so that would be an O(2*M) => O(M)

The overall complexity: O(N+M) but we know that M <= N
=> O(2*N) => O(N)





Task3: 
Part A:
Let N = number of rows in calls
Let M = number of unique codes being called from Bangalore

get_codes => O(N)
print_codes_sorted => O(M * log M) since sorted is O(n*logn) for both worst and average case

Overall complexity: O(M*logM)



Part B:
Let N = number of rows in calls
get_number_calls => O(N)
get_bangalore_percent => O(1)
Overall: O(N)





Task 4:
Let N = number of rows in calls file
Let M = number of rows in texts file
Let P = number of possible telemarketers
Let Q = number of unique telephone numbers
generate_telephones => O(2*M + 2*N) => O(n) with n = max(N,M)
get_telemarketers => O(Q)
sort the telemarketers => O(p*logp)
Overall: O(p*logp).