# ----------------------------
# Define Fuzzy Sets A and B
# ----------------------------
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

# ----------------------------
# Union of Fuzzy Sets: A ∪ B
# Union is defined as: μ(x) = max(A(x), B(x))
# ----------------------------
def union(A, B):
    return {k: round(max(A[k], B[k]), 2) for k in A}

# ----------------------------
# Intersection of Fuzzy Sets: A ∩ B
# Intersection is defined as: μ(x) = min(A(x), B(x))
# ----------------------------
def intersection(A, B):
    return {k: round(min(A[k], B[k]), 2) for k in A}

# ----------------------------
# Difference of Fuzzy Sets: A - B
# Defined as: μ(x) = min(A(x), 1 - B(x))
# ----------------------------
def difference(A, B):
    return {k: round(min(A[k], 1 - B[k]), 2) for k in A}

# ----------------------------
# Complement of a Fuzzy Set A
# Defined as: μ(x) = 1 - A(x)
# ----------------------------
def complement(A):
    return {k: round(1 - A[k], 2) for k in A}

# ----------------------------
# Cartesian Product of Fuzzy Sets A × B
# Relation μR(x, y) = min(A(x), B(y))
# ----------------------------
def cartesian_product(A, B):
    return {(x, y): round(min(A[x], B[y]), 2) for x in A for y in B}

# ----------------------------
# Max-Min Composition of Two Fuzzy Relations R1 and R2
# μR(x, z) = max_y (min(R1(x, y), R2(y, z)))
# ----------------------------
def max_min_composition(R1, R2):
    # Extract all unique x, y, and z values from relations
    X = sorted(set(i for (i, _) in R1))  # x values from R1
    Y = sorted(set(j for (_, j) in R1))  # y values (intermediate)
    Z = sorted(set(k for (_, k) in R2))  # z values from R2

    result = {}
    for x in X:
        for z in Z:
            # For each y, calculate min(R1(x, y), R2(y, z))
            values = [min(R1.get((x, y), 0), R2.get((y, z), 0)) for y in Y]
            # Max-min rule: take the maximum of all min values
            result[(x, z)] = round(max(values), 2) if values else 0
    return result

# ----------------------------
# Perform and Print All Operations
# ----------------------------
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)

print("Union A ∪ B:", union(A, B))
print("Intersection A ∩ B:", intersection(A, B))
print("Difference A - B:", difference(A, B))
print("Complement of A:", complement(A))
print("Complement of B:", complement(B))

# Create fuzzy relations (Cartesian Products)
R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
print("Fuzzy Relation R1 (A × B):", R1)
print("Fuzzy Relation R2 (B × A):", R2)

# Max-Min Composition of Relations R1 and R2
composition_result = max_min_composition(R1, R2)
print("Max-Min Composition of R1 and R2:", composition_result)