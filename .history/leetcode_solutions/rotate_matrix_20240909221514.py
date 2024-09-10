def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1

        # Loop allows me to do inner layers.
        while left < right:
            top, bottom = left, right
            # Loop allows me to traverse a layer.
            for layer in range(right - left):
                # Save top left value.
                top_left_temp = matrix[top][left + layer]
                # Move bottom left to top left.
                matrix[top][left + layer] = matrix[bottom - layer][left]
                # Move bottom right to bottom left.
                matrix[bottom - layer][left] = matrix[bottom][right - layer]
                # Move top right to bottom right.
                matrix[bottom][right - layer] = matrix[top + layer][right]
                # Move top left temp to top right.
                matrix[top + layer][right] = top_left_temp
            # Move to inner layer.
            left  += 1
            right -= 1