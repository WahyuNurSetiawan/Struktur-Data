import ctypes  # Provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self.n = 0  # Count actual elements
        self.capacity = 1  # Default array capacity
        self.A = self.make_array(self.capacity)  # Low-level array

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self.n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self.n:
            raise IndexError("Invalid index")
        return self.A[k]  # Retrieve from array

    def append(self, obj):
        """Add an object to the end of the array."""
        if self.n == self.capacity:  # Not enough room
            self.resize(2 * self.capacity)  # Double capacity
        self.A[self.n] = obj
        self.n += 1

    def resize(self, c):  # Non-public utility
        """Resize internal array to capacity c."""
        B = self.make_array(c)  # Create a new (bigger) array
        for k in range(self.n):  # Copy existing values to the new array
            B[k] = self.A[k]
        self.A = B  # Use the bigger array
        self.capacity = c

    def make_array(self, c):  # Non-public utility
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()

A = DynamicArray()
A.append(1)
A.append(4)
A.append(7)
print(A[0], A[1], A[2])
