import numpy as np

# Convert a hexadecimal string to a bit vector in numpy
def hex_to_bit_vector(hex_string):
	# Remove any leading '0x' if present
	hex_string = hex_string.lstrip('0x')
	
	# Convert the hexadecimal string to an integer
	integer_value = int(hex_string, 16)
	
	# Convert the integer to a binary string and remove the '0b' prefix
	binary_string = bin(integer_value)[2:]
	
	# Pad the binary string with leading zeros to make its length a multiple of 8
	padded_length = ((len(binary_string) + 7) // 8) * 8
	binary_string = binary_string.zfill(padded_length)
	
	# Convert the binary string to a numpy array of bits (0s and 1s)
	bit_vector = np.array(list(binary_string), dtype=int)
	
	return bit_vector

# Visualize theory of https://github.com/lowRISC/opentitan/blob/master/hw/ip/prim/rtl/prim_secded_hamming_22_16_dec.sv
v1 = hex_to_bit_vector("0x01AD5B")
v2 = hex_to_bit_vector("0x02366D")
v3 = hex_to_bit_vector("0x04C78E")
v4 = hex_to_bit_vector("0x0807F0")
v5 = hex_to_bit_vector("0x10F800")
v6 = hex_to_bit_vector("0x3FFFFF")
parity_matrix = np.vstack([v1, v2, v3, v4, v5, v6])
print(parity_matrix)

# Transpose the parity matrix to get the generator matrix
generator_matrix = np.transpose(parity_matrix)
print(generator_matrix)

# Create an identity bit matrix of size 16x16

identity_matrix = np.eye(16, dtype=int)
print(identity_matrix)

# Write code to step by step generate the parity and generator matrices for a (k, m) Hamming code where k is the number of data bits and m is the number of parity bits. The total codeword length n is given by n = k + m. The parity matrix should be constructed such that it can detect and correct single-bit errors.
def generate_hamming_code(k):
	# Calculate the number of parity bits needed
	m = 0
	while (2**m < k + m + 1):
		m += 1
	
	n = k + m  # Total codeword length
	
	# Create the parity matrix
	parity_matrix = np.zeros((m, n), dtype=int)
	
	# Fill the parity matrix according to the Hamming code construction
	for i in range(1, n + 1):
		binary_representation = bin(i)[2:].zfill(m)  # Get binary representation of the index
		for j in range(m):
			parity_matrix[j][i - 1] = int(binary_representation[m - j - 1])  # Fill the parity

	return parity_matrix

g = generate_hamming_code(11)
print(g)

# 41, 34 with all 1's as valid
import numpy as np

def generate_secded_hsiao(data_bits=34, ecc_bits=7):
    # 1. Generate all columns with odd weights >= 3 (ensures SECDED)
    candidates = []
    for i in range(1, 2**ecc_bits):
        col = [int(x) for x in format(i, f'0{ecc_bits}b')]
        if sum(col) % 2 == 1 and sum(col) >= 3:
            candidates.append(col)
    
    matrix = np.array(candidates).T
    target = np.ones(ecc_bits, dtype=int)
    
    # 2. Find a subset of 34 columns whose XOR sum is [1,1,1,1,1,1,1]
    # This ensures that H * [1...1] = [P|I] * [1...1] = [1...1] + [1...1] = 0
    # Using a simple greedy completion for the 34th column
    for i in range(len(candidates) - 34):
        subset_indices = list(range(i, i + 33))
        current_sum = np.sum(matrix[:, subset_indices], axis=1) % 2
        needed_col = (target + current_sum) % 2
        
        # Verify needed_col is a valid unused candidate
        needed_list = needed_col.tolist()
        if needed_list in candidates:
            final_idx = candidates.index(needed_list)
            if final_idx not in subset_indices:
                subset_indices.append(final_idx)
                return matrix[:, subset_indices]
    return None

# Generate and Display
p_matrix = generate_secded_hsiao()

if p_matrix is not None:
    print(f"Generated {p_matrix.shape[1]} data bit columns for {p_matrix.shape[0]} ECC bits.")
    print("Row sums of P (must be all 1s):", np.sum(p_matrix, axis=1) % 2)
    print("\nParity Equations (P-Matrix Columns):")
    for idx, col in enumerate(p_matrix.T):
        print(f"Data Bit {idx:02}: {col.tolist()}")
else:
    print("Could not find a valid matrix for these constraints.")

# Colored matrix print

# 1. Create the matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 2. Define ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

colors = [Colors.RED, Colors.GREEN, Colors.BLUE]

# 3. Print with column colors
for row in matrix:
    formatted_row = []
    for i, val in enumerate(row):
        # Apply color based on column index, reset after each value
        color = colors[i % len(colors)]
        formatted_row.append(f"{color}{val:4}{Colors.RESET}")
    print(" ".join(formatted_row))
