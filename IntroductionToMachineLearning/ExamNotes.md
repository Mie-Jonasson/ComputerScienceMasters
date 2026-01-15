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
Todo: SVM / Kernels
todo: "ill-conditioned?"
todo: conclusions for exam question 4
todo: understand convolutions
todo: investigate common filter types
todo: fast fourier transform
todo: HoG explained & edge detection
todo: fetch all tutorial notebooks
todo: orthonormal bases, change of basis matrix
todo: LDA
todo: multi-class confusion matrix and metric aggregation
todo: back propagation
---
## Question 1: Exercises Week 2-3 (Vector & Matrices)
### 1(a) Focus on inner products, vector operations, distance metrics and their relation to ML (evaluation and other metrics). You may relate this to week 10 (evaluation) but focus on vectors.

### 1(b) Focus on matrices and their operations (addition, multiplication, transpose, inverse, determinant, orthogonal). Relate them to their application within the course (e.g., transformations, basis in week 11).

### 1(c) Focus on how linear equations and their solutions are related to matrices.

## Question 2: Exercise Week 4 (Linear Transformations)
### 2(a) Use the tutorial to focus on exploring linear transformations in 2D and 3D spaces, including operations such as scaling, shearing, reflections, rotations, and translations, while drawing connections to their extensions in higher-dimensional linear transformations. Additionally, you should explain the relationship between linear transformations and non-linear transformations including affine, thus bridging the gap between linear and more complex transformations.

### 2(b) Focus on how linear and non-linear models can be learned using matrix inverses. Discuss the relationship between model complexity (e.g., polynomial degree) and the amount of data needed to accurately train these models with matrix inverses.

### 2(c) Focus on affine transformations, homogeneous coordinates and composition of linear transformations.

## Question 3: Exercise Week 5 (Projections and Least Squares)
### 3(a) Focus on the relation between linear least squares (function minimization) and projections.

### 3(b) Focus on linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions) and the interpretation of results for various types of models (see week 7).

### 3(c) Learning of Affine (multivariate) functions and linear optimization.

## Question 4: Exercise Week 6 (Mandatory 1)
### 4(a) Focus on preprocessing and feature extraction in Mandatory 1

### 4(b) Focus on model predictions and learning Mandatory 1

### 4(c) Focus on model evaluation in Mandatory 1

### 4(d) Describe vector space, basis, independence and how these are related to concepts in machine learning (learning, transformations etc). You MAY include exercises week 12 if you have done them.

## Question 5: Exercise Week 7 (Model Complexity, Model seleection and noise)

### 5(a) Linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions).

### 5(b) Discuss the relationship between data quality, uncertainty, and the challenges of overfitting and underfitting in model learning.

### 5(c) Discuss how factors affect a model’s ability to generalize to unseen data. Relate this to concepts of data evaluation, such as train-test splits, cross-validation, and performance metrics, to assess a model’s predictive capability and robustness.

## Question 6: Exercise Week 8 (Filtering)
### 6(a) Focus on filtering (1D, 2D, and n-D convolution and correlation, blurring and smoothing, and noise).

### 6(b) Focus on filtering for derivatives, gradients, and edges. You may include how these operations can be used to construct features such as HOG.

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
