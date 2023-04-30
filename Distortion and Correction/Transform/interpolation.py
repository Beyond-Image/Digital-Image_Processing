class interpolation:

    def linear_interpolation(self, x, x1, x2, i1, i2):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here


        i = i1 * ((x2 - x) / (x2 - x1)) + i2 * ((x - x1) / (x2 - x1))

        return i

    def bilinear_interpolation(self, p1, p2, p3, p4, x, y):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task

        hold1 = self.linear_interpolation(y, p1[1], p2[1], p1[2], p2[2])
        hold2 = self.linear_interpolation(y, p3[1], p4[1], p3[2], p4[2])
        return self.linear_interpolation(x, p1[0], p3[0], hold1, hold2)
