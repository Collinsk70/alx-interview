def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start the new row with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)
    
    return triangle

# Testing the function with n = 5
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

