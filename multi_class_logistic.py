import torch
import torch.nn.functional as F

class LinearModelMultiClass:
    def __init__(self, num_features, num_classes):
        #Initialize weight matrix with shape (num_features, num_classes)
        #each column corresponds to weights for one class
        self.w = torch.rand(num_features, num_classes)  #shape (p, k)

    def score(self, X):
        """
        Calculate scores for each class and each data point.
        Here, scores is a matrix of shape (n, k), where
        n = number of samples, k = number of classes.

        agumensts:
            X (torch.Tensor): feature matrix (n, p)
                              Assumes last column is bias term of 1s.

        Return:
            scores (torch.Tensor): (n, k) class scores for each sample
        """
        scores = X @ self.w 
        return scores


class LogisticRegressionMultiClass(LinearModelMultiClass):
    def loss(self, X, y):
        """
        Calculate our cross-entropy loss.

        arguensts:
            X (torch.Tensor): feature matrix (n, p)
            y (torch.Tensor): true class labels (n,) with values in {0, ..., k-1}

        Return:
            loss (torch.Tensor): scalar average cross-entropy loss
        """
        scores = self.score(X)  #shape (n, k)
        probs = F.softmax(scores, dim=1)  # softmax for classes for each sample
        # Cross-entropy loss... negative log likelihood of true class probabilities
        loss = -torch.mean(torch.log(probs[range(len(y)), y] + 1e-8))
        return loss

    def grad(self, X, y):
        """
        Calculate gradient of cross-entropy loss.

        argumenst:
            X (torch.Tensor): feature matrix (n, p)
            y (torch.Tensor): true class labels (n,)

        Return:
            grad (torch.Tensor): gradient matrix with shape (p, k)
        """
        n = X.size(0)
        scores = self.score(X)  #(n, k)
        probs = F.softmax(scores, dim=1)  #(n, k)

        #Create one-hotencoding of y
        y_onehot = torch.zeros_like(probs)
        y_onehot[range(n), y] = 1

        #Gradient is X^T @ (probs - y_onehot)/n
        grad = X.T @ (probs - y_onehot) / n
        return grad


class GradientDescentOptimizerMultiClass:
    def __init__(self, model):
        self.model = model
        self.prev_w = None

    def step(self, X, y, alpha=0.1, beta=0.9):
        """
        Perform one gradient descent step with momentum.

        Args:
            X (torch.Tensor): feature matrix (n, p)
            y (torch.Tensor): true labels (n,)
            alpha (float): learning rate
            beta (float): momentum term

        Updates:
            self.model.w: updated weights matrix (p, k)
            self.prev_w: stores previous weights for next step
        """
        grad = self.model.grad(X, y)  #calculate gradient matrix (p, k)

        if self.prev_w is None:
            self.prev_w = self.model.w.clone()

        w_current = self.model.w.clone()

        # Update weights with momentum: w_new = w - alpha*grad + beta*(w - w_prev)
        self.model.w = self.model.w - alpha * grad + beta * (self.model.w - self.prev_w)

        self.prev_w = w_current
