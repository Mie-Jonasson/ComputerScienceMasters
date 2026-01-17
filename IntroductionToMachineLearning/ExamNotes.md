# Exercise Notes
---
## Week01
Basic Python & Vector operations

## Week02
Basic Datapoint distance comparison of "real data"
See data collected in [IML_Projects](https://github.itu.dk/miejo/IML_Projects/tree/main/Assignment_1) on github.itu.dk

## Week03
Basic Linear Algebra

## Week04
Basic Polynomial fitting
TODO: Get descriptions of weights' impact on curve for different polynomial degrees
TODO: Pen & Paper
TODO: Extra 02-Polynomials

## Week05
Least Squares Fitting
TODO: Write util code
TODO: Write up math in a simple overview
TODO: Affine spatial regression notebook

## Week06
Assignemnt 1 solutions
Data Preprocessing of pupil data
Projecting eye coordinates to screen coordinates

## Week07
Polynomial Regression (least squares generalised)
Model Complexity and Generalization (Occam's Razor)

## Week08
Data Cleaning & Smoothing
Gaze Saccade / Fixation detection
Filtering matrices

## Week09
Covariance & Correlation
Descriptive statistics of fitting
Interpolating missing data

## Week10
Logistic Regression (classification using sigmoid function)
Decision Boundaries (functions splitting N-dimensional space into classes)

## Week11
Evaluation Metrics & Confusion Matrices
Histograms of Gradients (HoGs)
HoGs for image classification
Basis

## Week12
Assignment 2
PCA (dimensionality reduction)
TODO: Review Assignemnt Feedback

## Week13
Clustering

## Week14
Neural Networks
Derivatives / Optimization

# Exam Question Notes
todo: "ill-conditioned?"
todo: conclusions for exam question 4
todo: fast fourier transform
todo: fetch all tutorial notebooks
todo: LDA
todo: multi-class confusion matrix and metric aggregation
todo: back propagation
---
## Question 1: Exercises Week 2-3 (Vector & Matrices)
### 1(a) Focus on inner products, vector operations, distance metrics and their relation to ML (evaluation and other metrics). You may relate this to week 10 (evaluation) but focus on vectors.
- Open W02/01-poses.ipynb (pose similarity using euclidean distance)
- **Inner Product** / dot product: $\vec{a} \cdot \vec{b} = a_1 * b_1 + ... + a_n * b_n$
    - Length of vector: $||a|| = \sqrt{a \cdot a}$ (each item of the vector squared == pythagoras)
    - Used for **euclidean distance**: $\sqrt{(x - y) \cdot (x - y)}$
    - Used for **cosine similarity** (angular similarity): $(x \cdot y) / ( ||x|| * ||y||) $
- Other simple operations:
    - *Addition* is done element-by-element, producing vector of same size
    - *Scalar Multiplication* is multiplying the scalar onto every element
- In ML, usually used for:
    - *Distance* metrics as **error terms** (Loss in regression) or **similarity measures** (KNN)
    - **Functions / Polynomials** represented as *dot products*. ($a*cos(x) + b * x + c = [a, b, c] \cdot [cos(x), x, 1] $) - relevant for representing linear equations as matrix multiplication!
    - The **"kernel trick"** is using the *inner product* in high dimensional space
    - **Convolutions**, **gradients** and many more things are *inner products* or rely on them

### 1(b) Focus on matrices and their operations (addition, multiplication, transpose, inverse, determinant, orthogonal). Relate them to their application within the course (e.g., transformations, basis in week 11).
- Open W03/01-linear_algebra.ipynb (Addition / multiplication) and/or W04/01-linear_algebra.ipynb (inverses, determinant)
- Simple Operations:
    - *Addition* is an element-by-element operation (just like with vectors)
    - *Scalar Multiplication* is multiplying the scalar onto every element (just like with vectors)
- **Matrix Multiplication** is non-commutative (order matters), and is done in the following way: given $AB$ with dimensions $A \gets m x n$ & $B \gets n x k$, then we produce the output matrix $C \gets m x k$, for which the element in row $i$ column $j$ is the dot product of the $i^{th}$ row of A and the $j^{th}$ column of B. 
- **Transpose** is the operation of switching around the columns and rows, in result flipping the matrix around the diagonal. Used in a lot of ML applications, for example finding Projection matrices for Least Squares and finding covariance. It flips the perspective of the transformation, such that we have the same transformation of the space from a different viewpoint.
- **Inverse** is the matrix $A^{-1}$, such that $AA^{-1} = A^{-1}A = I$. The inverse is only defined for square matrices, and for a 2 x 2 matrix, it has the closed form: for $A = [[a, b], [c, d]]$ then $A^{-1} = \frac{1}{det(A)} * [[d, -b][-c, a]]$ - Used to "undo" the transformation of A, can be used to eliminate terms when isolating terms in an equation (f.ex. linear equation solutions), or to transfer back and forth between bases. 
- **Determinant** is calculated for a 2 x 2 matrix as: $a * d - c * b$ -> a non-zero determinant indicates invertibility of a square matrix, i.e. det(A) != 0 => non-singular matrix. The determinant describes how a transformation scales the space (det(A) = 0 => collapses space to a lower dimension)
- **Orthogonal** matrices have column vectors that are orthogonal to each other. These column vectors may further be normalized and may represent an orthonormal basis (i.e. a basis that preserves lengths and angles). For orthogonal matrices, $A^TA = I$, one may also therefore say that $A^{-1} = A^T$ for orthogonal matrices. 
    - A common example of an orthogonal matrix is the **PCA matrix**, which contains orthogonal vectors in the direction of highest variance. Orthogonal matrices only perform rotations and flipping!

### 1(c) Focus on how linear equations and their solutions are related to matrices.
- A set of linear equations may be represented as matrices: $\{1x + 2y = 7, 2x - 1y = 4\} = [[1, 2], [2, -1]] [x, y]^T = [7, 4]^T$, in short we may write this as $Ax = b$
- We can solve linear equation using **Gaussian Elimination** to achieve **Row-Echelon Form** (i.e. Identity matrix + vector of results)
- We have a number of different options when looking at the system of equations:
    - **Infinite Solutions** / **Under-determined**: we do not have enough independent observations to determine a single unique solution. Instead, there are infinitely many solutions.
    - **Exact Solution**: We have exactly that $m = n = Rank(A)$, where m denote the number of parameters and n denote the number of linearly independent equations. Here we can determine exactly 1 solution solving the equations.
    - **No Solution** / **Over-determined**: We have too many linearly independent observations, such that we cannot determine a solution fitting them all. In this case, if it was in a polynomial fitting case, we would go to Least Squares to solve the equations. A no solution / over-determined matrix is also called an 'inconsistent' matrix.

## Question 2: Exercise Week 4 (Linear Transformations)
### 2(a) Use the tutorial to focus on exploring linear transformations in 2D and 3D spaces, including operations such as scaling, shearing, reflections, rotations, and translations, while drawing connections to their extensions in higher-dimensional linear transformations. Additionally, you should explain the relationship between linear transformations and non-linear transformations including affine, thus bridging the gap between linear and more complex transformations.
- Open W04/Transformations Tutorial.ipynb
- **Scaling** is scaling one or more dimensions by a constant factor, and is represented by a diagonal matrix of scaling values $s_1, s_2, ..., s_n$
- **Shearing** is skewing/slanting the space in a certain directions (horisontally, vertically or both), and is represented by the identity matrix with skewing values added instead of 0's. Horisontal sheering: $[[1, sh_X], [0, 1]]$, Vertical sheering: $[[1, 0], [sh_Y, 1]]$
- **Reflection** is flipping the data, i.e. the matrix swapping around 2 rows of the identity matrix, for the dimensions that should be flipped over: $[[0, 1], [1, 0]]$ 
- **Rotation** is rotating the data around the center point (0, 0) and is represented by the matrix $[[cos(\theta), -sin(\theta)], [sin(\theta), cos(\theta)]]$
- **Translation** is moving the data, i.e. affine transformation (adding a vector term)
- *Affine Tranformations* May be represented as linear transformations using a trick. I.e. given the affine transformation $Ax + b$, the linear transformation may be represented as $[[A, b],[0, 1]][x, 1]^T$ (**homogenous coordinates**) -> this composes nicely! (b can be given as 0 for all linear transformations) -> we can translate back and forth between homogenous and euclidean coordinates.
    - Affine transformations no longer preserve additivity or preservation of origin. But it's a linear transformation + shift.
    - Neural network layers are affine!
- *Non-linear Transformations* are many things.
    - A common example is **non-linearity of inputs** while remaining linear in parameters, i.e. polynomials, cos/sin etc. - these may still utilize linear transformations / least squares to determine model parameters for a given set of observations.
    - complex decision boundary functions, such as sigmoid, ReLU, tanh etc., are non-linear overall!
- $Linear \subset Affine$, Non-linear complex models require gradient descent as opposed to simple matrix inversion.

### 2(b) Focus on how linear and non-linear models can be learned using matrix inverses. Discuss the relationship between model complexity (e.g., polynomial degree) and the amount of data needed to accurately train these models with matrix inverses.
- Open W04/01-polynomials.ipynb
- Given some matrix A, for which each row represents a data point (f.ex. $[x^2, x, y, 1]$ for a model $f(x, y) = a * x^2 + b * x + c * y + d$), we can write up the linear equations for the model given observations as $Ax = b$ where A are the observed inputs, x are the terms $[a, b, c, d]^T$ that we wish to learn and b are the observed outputs.
- We can isolate x on one side by using the inverse of A, such that: $x = A^{-1}b$, given A is invertible and has $m = n = Rank(A)$ (exact solution)
- More complex models have a higher number of parameters, and therefore also require more linearly independent observations to determine the exact solution. In particular, for k parameters we need $Rank(A) = k$. For polynomials of degree d, we need d+1 observations to fit the model exactly.

### 2(c) Focus on affine transformations, homogeneous coordinates and composition of linear transformations.
- *Affine Tranformations* May be represented as linear transformations using a trick. I.e. given the affine transformation $Ax + b$, the linear transformation may be represented as $[[A, b],[0, 1]][x, 1]^T$ (**homogenous coordinates**) -> this composes nicely! (b can be given as 0 for all linear transformations) -> we can translate back and forth between homogenous and euclidean coordinates.
    - Affine transformations no longer preserve additivity or preservation of origin. But it's a linear transformation + shift.
    - Neural network layers are affine!
- *Composition* refers to the task of applying multiple transformations in some sequence. We may for example do a rotation and then a shift or we may do scaling and then rotations. A cool thing about composition with linear transformations is that they compose nicely, i.e.: $ABx = A(Bx) = (AB)x$, meaning we can actually calculate the matrix AB initially and apply a single transformation to x which does both transformations in the given order. Remember that Matrix multiplication in non-commutative, so order does matter.

## Question 3: Exercise Week 5 (Projections and Least Squares)
### 3(a) Focus on the relation between linear least squares (function minimization) and projections.
- Open W05/00-projection_least_sq.ipynb (Least Squares Example)
- When we have a set of linear equations on the form $Ax = b$ and A is over-determined (i.e. $||x|| < Rank(A)$), we cannot find an exact solution to the set, because the set of linear equations is inconsistent!
- In this case we can use projections to find the vector $\hat{b}$ that is closest to $b$ in the vector space spanned by the column vectors of A. -> Draw example of a projection of a vector onto a line, emphasize orthogonality of projection and the fact that this is the vector in vector space of A with the smallest distance to the observed vector.
- The projection matrix P is $A(A^TA)^{-1}A^T$, and we find that $\hat{b} = A(A^TA)^{-1}A^Tb$, we may now replace in the initial equations to get: $Ax = \hat{b} = A(A^TA)^{-1}A^Tb$ and isolate x to get the parameters of the least squares solution: $x = (A^TA)^{-1}A^Tb$.
- Least Squares minimizes MSE as a feature of how projections work.

### 3(b) Focus on linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions) and the interpretation of results for various types of models (see week 7).
- **Design Matrix** is a matrix for which each row corresponds to a datapoints and each column corresponds to a certain term or transformed term. It can be made for any function that is linear in its parameters.
- **Kernels** may be used to describe higher order dimensions of the same data, and corresponds to constructing a design matrix in a certain structured way.
- Specific examples:
    - *Lines* through the origin will have a design matrix of a single column
    - *Polynomials* through the origin will have a design matrix with a column for each degree x^1 to x^d
    - *Affine* models have the design matrix of the data including an extra column of ones
    - *Other multivariate* have a column for each term of the input
- The columns of the design matrix are each associated with a parameter that we are trying to learn.
- Observing the outputs of the fitted model is beneficial, as we need to examine the errors in order to examine under-fitting / over-fitting tendencies as well as generalization. Fitting the training data super well is usually not a good sign - we want to land on a good place of the bias-variance tradeoff.

### 3(c) Learning of Affine (multivariate) functions and linear optimization.
- **Affine multivariate functions** have the form $f(x) = w^Tx + b = w_1x_1 + w_2x_2 + ... + w_nx_n + b$, where $x$ is a feature vector, $w$ contains weights, and $b$ is the bias term. This generalizes lines to hyperplanes in n-dimensional space.
- Learning affine functions means finding optimal $w$ and $b$ that minimize a loss function, typically **Mean Squared Error (MSE)**: $L = \frac{1}{m}\sum_i (y_i - w^Tx_i - b)^2$
- We can absorb the bias $b$ into $w$ by appending 1 to each $x_i$, making it $w^Tx$ where $x = [x_1, ..., x_n, 1]^T$ and $w = [w_1, ..., w_n, b]^T$. This allows us to represent the affine function as a linear function in an augmented space.
- **Linear optimization** refers to solving this using linear algebra. The least squares solution is $w^* = (X^TX)^{-1}X^Ty$, where $X$ is the design matrix with rows $[x_i; 1]^T$. This is a **closed-form solution** - we compute it directly via matrix operations, no iterative optimization needed.
- **Affine transformations** in 2D/3D can be learned using the same approach. For a 2D affine transformation $T$ mapping points from one coordinate system to another, we can set up a system of linear equations where each corresponding point pair gives us constraints, and solve using least squares to find the transformation matrix coefficients.

## Question 4: Exercise Week 6 (Mandatory 1)
### 4(a) Focus on preprocessing and feature extraction in Mandatory 1
- Open W06/01-data-preprocessing.ipynb
- Preprocessing of images to extract pupil centers.
    - Take photos from each trial (pattern)
    - Determine contours within the bounding box to determine the shape and placement of the pupil
    - Take the found pupil and determine the most likely center
- Preprocessing needs to be specific to the dataset recording session - i.e. the bounding box is specific to the test subject setup at a particular time, eye shape and contouring may change from person to person and placement of the subject may not be the same each time.
- Good and accurate preprocessing is important for generalization and validity of results, depending on the type of experiment one is conducting.

### 4(b) Focus on model predictions and learning Mandatory 1
- Open W06/02-gaze.ipynb
- Fits a linear least squares model for x and a model for y separately. Both are fits as $f(x, y) = a * x + b * y + c$
- Look at prediction plot - some are good, some are less good!
- Look at prediction on whole different set - it is not generalizable to data recorded at a different time in a different setup.

### 4(c) Focus on model evaluation in Mandatory 1
- Open W06/02-gaze.ipynb (Model evaluation for gaze estimation)
- **Multiple evaluation metrics** are used to assess model performance comprehensively:
    - **RMSE (Root Mean Squared Error)**: Calculated as `rmse = np.sqrt(np.mean(np.sum((predicted - ground_truth)**2, axis=1)))` - provides overall prediction error magnitude
    - **MAE (Mean Absolute Error)**: Mean absolute error in x and y dimensions separately - shows per-dimension error
    - **Mean Euclidean distance**: `dist = np.mean(np.sqrt(np.sum((predicted - ground_truth)**2, axis=1)))` - measures spatial distance between predicted and actual gaze positions
    - **Absolute errors**: Per-sample absolute errors between predictions and ground truth - allows identification of individual problematic predictions
- **Cross-subject evaluation** tests generalization by training on `test_subject_0` and testing on `test_subject_1` (Task 8-9). This reveals that models trained on one person don't generalize well to another person, demonstrating the need for person-specific calibration due to individual differences in fovea placement ($\pm$ 5 degrees).
- **Evaluation across different patterns** assesses performance on various data distributions:
    - **Grid pattern**: Used for training/calibration (9 calibration points)
    - **Circle, line, and random patterns**: Used for testing to evaluate how model performs on different movement patterns
    - This reveals that models may perform well on grid but show larger errors on other patterns, indicating potential overfitting to the training pattern or systematic biases
- **Visualization of error patterns** using `plot_results_grid` function provides:
    - Error distributions across different test patterns
    - Differences in error between x and y coordinate predictions (systematic biases may appear, e.g., consistent upward skew)
    - Identification of systematic errors and failure modes
    - Helps diagnose whether errors are random or systematic, and whether they differ between dimensions

### 4(d) Describe vector space, basis, independence and how these are related to concepts in machine learning (learning, transformations etc). You MAY include exercises week 12 if you have done them.
- Vector spaces are **subspaces** of spaces such as $R^2$ (vectors of two numbers) or $M^{2x2}$ (matrices of size 2 x 2) - a subspace is a well-described subset of the items within the full space, such that f.ex. $V \subset R^2$.
- A Vector space is defined by its **basis**, i.e. the set of vectors $\vec{a_i}$ that **span** the entire vector space. We talk about spanning in terms of linear combinations, so a subspace described by the single vector $w = [1, 2]^T$ is the subspace of all vectors that can be obtained by multiplying some scalar onto $w$.
- A basis always contains independent vectors, as linear dependence between vectors does not constitute part of a basis.
- A basis may be **orthogonal** (i.e. vectors are orthogonal to each other) and normalized (all unit length) -> if both hold, we may call it an **orthonormal** basis.
- **PCA is an orthonormal basis**, and we may transform between bases (we can consider different orthonormal bases as different perspectives of looking at the same data while retaining angles and distances)

## Question 5: Exercise Week 7 (Model Complexity, Model seleection and noise)

### 5(a) Linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions).
- Open W07/01-polynomial_regression.ipynb
- **Design Matrix** is a matrix for which each row corresponds to a datapoints and each column corresponds to a certain term or transformed term. It can be made for any function that is linear in its parameters.
- **Kernels** may be used to describe higher order dimensions of the same data, and corresponds to constructing a design matrix in a certain structured way.
- Specific examples:
    - *Lines* through the origin will have a design matrix of a single column
    - *Polynomials* through the origin will have a design matrix with a column for each degree x^1 to x^d
    - *Affine* models have the design matrix of the data including an extra column of ones
    - *Other multivariate* have a column for each term of the input
- The columns of the design matrix are each associated with a parameter that we are trying to learn.
- Observing the outputs of the fitted model is beneficial, as we need to examine the errors in order to examine under-fitting / over-fitting tendencies as well as generalization. Fitting the training data super well is usually not a good sign - we want to land on a good place of the bias-variance tradeoff.
- Noise can be a problem in settings where we do not have that much data, as we end up learning some of the noise instead of the underlying patterns.

### 5(b) Discuss the relationship between data quality, uncertainty, and the challenges of overfitting and underfitting in model learning.
- Open w07/01-polynomial_regression.ipynb
- Data quality is super important both for reliance and generalizability of the results from an experiment / trained model. When dat aquality is poor, we may not have much of a clear signal at all, and may instead learn an indesireable pattern.
- Uncertainty should always be considered, as no real data is ever clean - there will always be various different errors to account for, both including natural variation as well as systematic errors (measurement errors etc.).
- Overfitting causes issues as we may overfit to noise rather than underlying patterns, which will cause issues in terms of generalizability. 
- Underfitting causes issues as we may have a too simple setup or not enough data to learn the actual underlying distribution - this will cause bad performance even on the training data itself. 
- We need to balance between over- and under-fitting, which is often referred to as the bias-variance tradeoff; high bias == underfitting & high variance == overfitting. This is a common challenge across machine learning domains.

### 5(c) Discuss how factors affect a model’s ability to generalize to unseen data. Relate this to concepts of data evaluation, such as train-test splits, cross-validation, and performance metrics, to assess a model’s predictive capability and robustness.
- Open W07/02-model_complexity.ipynb
- it is important to be aware of model generalizability while training, as being able to generalize is the whole point of creating a machine learning model. There are several methodologies that one might use to either get a robust model or determine model robustness:
    - *Train-Test Splits* are important, as performance on data unseen by the model can give us an idea of how the model would perform in real life. On the other hand, we need to tweak the sampling strategy depending on the data - timeseries or classification with underrepresented classes may require special considerations in the process.
    - *Cross-validation* takes the training split to the next level, keeping out a certain proportion of data and switching between folds of data as validation data. This is a more robust version of train-val splits that gives us a more robust average performance on unseen data or helps us pick good hyper parameters more robustly. (removes the lucky/unlucky draw risks)
    - *Performance Metrics* depending on the task at hand, one may use various loss metrics to compare models. Are particularly useful approach for complex models is the notion of *"early stopping"* when the performance on a validation set no longer decreases. Another approach for determining model complexity (hyper parameter tuning) is the *elbow method* which seeks to determine f.ex. the optimal polynomial degree d.
- When model have similar performance on train, val and test data, we can be convinced to some degree that, if data in the real world is sampled from the same distribution, then teh performance will be similar. We may increase robustness of the conclusions with cross-validation metrics.

## Question 6: Exercise Week 8 (Filtering)
### 6(a) Focus on filtering (1D, 2D, and n-D convolution and correlation, blurring and smoothing, and noise).
- Open W08/02-filter_basics.ipynb
- We can do kernel filtering on many different types of data. kernel filtering is sliding some filter of numbers over a matrix of data and convolving the filter with the matrix values as a sum.
- Useful for example for probability distributions or image analysis - we may have a filter that does gaussian blurring (see notebook examples) or smoothing / sharpening of edges (see notebook examples) etc. These kinds of transformations may be performed on any dimension of data to create a similar effect of smoothing out or sharpening various attributes of the input data or creating additional features (i.e. the entire prupose of convolutional layers in CNNs)
- May be useful to eliminate / blur noisy signals or to extract certain prominent features from an image.

### 6(b) Focus on filtering for derivatives, gradients, and edges. You may include how these operations can be used to construct features such as HOG.
- Open w08/Filters Tutorial.ipynb (computing x- & y-derivates + finding gradient) and W11/03-hog.ipynb (using gradients in pixels to create HoG features)
- We can find derivatives in x- and y-direction and combine these into a gradient for each pixel (i.e. for grayscale values) -> this will in turn detect edges and lines in the image, which may for example be combined into a HoG
- The detection is a useful feature view of the data and may be used for object detection and classification as it removes a lot of redundant data.
- Gradients are per-pixel and HoG aggregates these in cells, and cells. A cell contains the total gradient across pixels for a bucket. These cell histograms are then normalized across a block.

## Question 7: Exercise Week 9 (Understanding Data and Descriptive Methods)
### 7(a) Describe correlation and covariance, explain how they are calculated, and discuss how they are useful for understanding data and for descriptive analysis.

### 7(b) Explain how descriptive statistics can be used to assess model selection and the generalization ability of machine learning models.

### 7(c) Describe noise, outliers, and missing data.

### 7(d) Focus on uncertainty, noise, data cleaning in relation to regression, classification, clustering or dimensionality reduction (Covariance, distributions (e.g Normal/Gaussian))

## Question 8: Exercise Week 10-11 (Classification)
### 8(a) Linear classification, kernels, and classification boundaries

### 8(b) Logistic regression and classification boundaries

### 8(c) Linear and non-linear decision boundaries including SVM (include week 10) and possibly HOG features.

## Question 9: Exercise Week 11 (Evaluation)
### 9(a) Metrics/Evaluation of Classifiers

### 9(b) Metrics/Evaluation of Regression

### 9(c) Imbalanced data for classification and regression

## Question 10: Exercise Week 12 + Assignment 2 (Principal Component Analysis)
### 10(a) Basis and transformations

### 10(b) Dimensionality reduction and PCA. Focus on mandatory 2

### 10(c) Generating models and PCA

### 10(d) Eigenvalues, covariance matrix and basis

## Question 11: Exercise Week 13 (Clustering )
### 11(a) K-means and Mean shift

### 11(b) K-means and Algomerative clustering

### 11(c) Kmeans and ELBOW

## Question 12: Exercise Week 14 (Neural networks)
### 12(a) Neural networks prediction (regression vs classification)

### 12(b) Neural networks training (Gradients, the chain rule and back/forward propagation)

### 12(c) Training and Evaluation including over/underfitting

### 12(d) Model architectures: Difference between fully connected /multi layer perceptron (MLP) and CNN

### 12(e) Loss functions, model complexity, cross-validation.

---
# Extra Reflective Questions
## Linear Algebra
### Basics
- List as many purposes for which we use vectors for image analysis and Machine learning
- What is the equation of a line, planes and hyperplane using vector notation?
- How do you calculate the length and orientation of a vector?
- How do we know when two vectors u and v are orthogonal to each other?
- How do we know when two vectors u and v are parallel to each other?

### Linear Equation
- What is a linear equation and how is this relate to matrices?

### Inner product
- How is the inner product related to:
    - a measure of distance.
    - matrix multiplication
    - projections
    - convolution
    - neural networks

### Solutions to Linear Equation
- What does it mean to have a solution to a linear set of equations?
- When can we have one, zero or many solutions to a linear set of equations?
- What is an over-determined set of equations.
- What is an under-determined set of equations.
- Why is the Determinant relevant when talking about solutions to linear equations.
- Why are subspaces important when talking about solutions to linear set of equations.
- Given data X ∈ RN and labels y. How w can linear equations be used to find the coefficients of the following models and how much training data is needed to learn the model parameters
    - (a) A straight line in the plane
    - (b) A plane in 3D
    - (c) A hyperplane in N-dimensional spaces
    - (d) Find the coefficients of a an N-order polynomial
    - (e) Find the coefficients of an similarity or affine transformations
- In the above cases what is the minimal number of points needed to solve the linear set of equations.

### Transformation
- What is a transformation and how is it related to a projection.
- Matrix multiplications may be considered as a transformation. Why?
- How are linear transformations combined?
- What is the purpose of homogeneous coordinates.
- What is the inverse of a transformation and what is its relevance to the course / ML.
- How is least squares (formally) related to projections

## Signals
- What are the definitions of convolution and correlation and how are they related
- When can correlation and convolution be used interchangeably
- How can correlation be implemented in a neural architechture and why is this beneficial?
- How is image templates useful as a machine learning model and a metric for comparison.
- How do image templates relate to machine learning

## Machine Learning
- Where is supervised and unsupervised learning used and how do they differ.
- How is least squares used in machine learning and how does it relate to least squares when using matrices.
- What is an objective function
- Which methods can be used to learn linear and non-linear models
- what is the difference between linear and non-linear models (including affine)
- What is the difference in how to optimize/minimize linear and non-linear functions (such as a loss function)
- Describe cases in which a non-linear prediction model can be learned with linear optimization methods
- How do recommender systems work and how is this related to inner products and matrix factorization.
- What is PCA? and how does PCA make use of subspaces , eigenvalues and eigenvectors.
- How is PCA and certain neural architectures related.
- Why is it called linear classification
- How does logistic regression differ from linear classifiation.
- What is the decision boundary and how can you find it.
- what is a kernel, where are they used and how is it related to model learning

## Evaluation
- Why is evaluation needed
- How do you ensure proper evaluation of models
- Why are training, test and verification sets needed in the training procedures?
- What is cross validation and how is it related to overfitting / underfitting
- How how can we tell when a model is under and overfitted?
