# problem 2

1. <br>

$$
\begin{aligned}
L(\theta) &= \prod \theta^{X_i}(1- \theta) ^{1-X_i}\\
&= \theta^{\sum X_i}(1-\theta)^{n-\sum X_i}
\end{aligned}
$$

2. <br>

    [code](./hw2.py)

    ![Ltheta](img/pb2.png)

3. <br>

$$
\begin{aligned}
Ln\ L(\theta) &= ln\ \theta\sum X_i +(n - \sum X_i)ln(1-\theta)\\
\frac{\partial Ln\ L(\theta)}{\partial \theta} &= \frac{\sum X_i}{\theta} + -1\frac{n - \sum X_i}{1 - \theta}  = 0\\
\theta& = \frac{\sum X_i}{\theta} = 0.6
\end{aligned}
$$

4. <br>
   
   ![pb2-3.png](img/pb2-3.png)

# problem 3


![pb3-1](img/pb3-1.png)

