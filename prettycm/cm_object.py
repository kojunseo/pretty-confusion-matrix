import numpy as np
from sklearn.metrics import confusion_matrix as skconfusion_matrix

class confusion_matrix:
    """"
    Confusion Matrix object for drawing.
    Input must be two-dimensional array:
                                    [[1,3,2]
                                    [2,3,1]
                                    [3,1,1]]
    """
    def __init__(self, matrix):
        if type(matrix) == list:
            matrix = np.array(matrix)

        if len(matrix.shape) != 2:
            raise IndexError("The dimmension of the matrix must be 2: ex) matrix.shape = (3,3) ")
        
        else:
            if matrix.shape[0] != matrix.shape[1]:
                raise IndexError("Confusion Matrix shape must be (n, n)")
            if matrix.shape[0] >= 10:
                raise ValueError("The number of the class must be under 10 for pretty confusion matrix")

            else:
                self.matrix = matrix
                self.n_classes = matrix.shape[0]
        self.max_value = matrix.max()

        self.set_classname([f"class{i}" for i in range(self.n_classes)])
        self.set_title("Unknown title")

    def set_classname(self, classnames):
        self.max_classname = -1
        if type(classnames) == list:
            for classname in classnames:
                if type(classname) != str:
                    raise TypeError(f"classname list must consist of 'str', your list consists {type(classname)}")
                if len(classname) >= 15:
                    raise NameError(f"classname is two long: {classname}")
                if len(classname) > self.max_classname:
                    self.max_classname = len(classname)
            classnames = np.array(classnames)

        if len(classnames) != self.n_classes:
            raise IndexError("classname must be same length of confusion matrix")
        self.classnames = classnames

    def __call__(self, x, y):
        return self.matrix[y,x]

    def set_title(self, title):
        self.title = title

    def __str__(self):
        string_for_return = f"{self.title}\n\n"
        for cname, data in zip(self.classnames, self.matrix):
            if self.max_classname <= 5:
                line = f"{cname:5s}  {''.join([f'{d:8.2f}' for d in data])}\n\n"
                spacing = 5
            elif self.max_classname <= 7:
                line = f"{cname:7s}  {''.join([f'{d:8.2f}' for d in data])}\n\n"
                spacing = 7
            elif self.max_classname <= 10:
                line = f"{cname:10s}  {''.join([f'{d:8.2f}' for d in data])}\n\n"
                spacing = 10
            else:
                line = f"{cname:15s}  {''.join([f'{d:8.2f}' for d in data])}\n\n"
                spacing = 15
            string_for_return+= line

        line = f"{' '*(spacing+5)}{' '.join([f'{cname[:10]:6s}' for cname in self.classnames])}"
        string_for_return += line
            
        return string_for_return

class confusion_matrix_by_cal(confusion_matrix):
    def __init__(self, y_true, y_pred):
        matrix = skconfusion_matrix(y_true=y_true, y_pred=y_pred)
        super().__init__(matrix=matrix)
