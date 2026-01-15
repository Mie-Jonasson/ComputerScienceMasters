# Exam Question Notes
---
## Question 1: Exercises Week 2-3 (Vector & Matrices)
### 1(a) Focus on inner products, vector operations, distance metrics and their relation to ML (evaluation and other metrics). You may relate this to week 10 (evaluation) but focus on vectors.

**5-6 Minute Pitch:**

Inner products are fundamental operations in machine learning that measure similarity and enable distance calculations. The inner product (dot product) of two vectors **u** and **v** is calculated as **u** · **v** = Σᵢ uᵢvᵢ, which geometrically represents the projection of one vector onto another, scaled by their magnitudes.

Vector operations form the backbone of ML computations. Addition and scalar multiplication allow us to combine features and scale them. The inner product is particularly crucial because it measures how aligned two vectors are - when vectors point in similar directions, their inner product is large; when orthogonal, it's zero; when opposite, it's negative.

Distance metrics derived from inner products are essential for ML evaluation. The Euclidean distance between two data points **x** and **y** is ||**x** - **y**|| = √[(**x** - **y**) · (**x** - **y**)], which measures straight-line distance in feature space. This is used in k-nearest neighbors, clustering algorithms, and evaluation metrics. The cosine similarity, defined as (**x** · **y**)/(||**x**|| ||**y**||), measures angular similarity regardless of magnitude, crucial for text analysis and recommendation systems.

In ML evaluation, these distance metrics quantify prediction errors. For regression, mean squared error (MSE) is essentially an average of squared Euclidean distances between predictions and true values. For classification, distance metrics help assess how well-separated classes are in feature space. The margin in support vector machines is directly related to the distance from data points to the decision boundary, computed using inner products.

Vector operations enable efficient batch processing - we can compute predictions for multiple data points simultaneously using matrix-vector products, where each row represents a data point. This computational efficiency is why vectorized operations are fundamental to modern ML frameworks.

### 1(b) Focus on matrices and their operations (addition, multiplication, transpose, inverse, determinant, orthogonal). Relate them to their application within the course (e.g., transformations, basis in week 11).

**5-6 Minute Pitch:**

Matrices are rectangular arrays of numbers that enable us to represent and manipulate linear transformations, systems of equations, and data transformations in machine learning. Each operation has specific geometric and computational meaning.

**Matrix addition** combines corresponding elements, useful for aggregating features or combining transformations. **Matrix multiplication** (AB) is the cornerstone operation - it represents composition of linear transformations. When we multiply a matrix A by a vector **x**, we transform **x** into a new space. In ML, this is how we apply learned weights to input features.

The **transpose** Aᵀ swaps rows and columns. Geometrically, it represents the adjoint transformation. In ML, transposes are crucial for computing gradients in backpropagation and for solving least squares problems, where we use (XᵀX)⁻¹Xᵀ**y** to find optimal parameters.

The **inverse** A⁻¹ undoes the transformation represented by A, satisfying AA⁻¹ = I. It's used to solve linear systems directly: if A**x** = **b**, then **x** = A⁻¹**b**. However, inverses only exist for square, non-singular matrices. In ML, we often use pseudo-inverses for over-determined systems (more equations than unknowns) in least squares fitting.

The **determinant** det(A) measures how a transformation scales volumes. If det(A) = 0, the transformation collapses space to a lower dimension, making A singular (non-invertible). This is critical in understanding when systems have unique solutions - a non-zero determinant guarantees invertibility.

**Orthogonal matrices** satisfy AᵀA = I, meaning their columns are orthonormal (unit length and mutually perpendicular). Orthogonal transformations preserve lengths and angles - they represent rotations and reflections. In week 11, we see that orthogonal matrices provide orthonormal bases, which are ideal for representing data efficiently. Principal Component Analysis (PCA) finds orthogonal directions of maximum variance, creating an optimal basis for dimensionality reduction.

In transformations, matrices encode how coordinates change: scaling stretches space, rotation preserves distances, shearing skews space. These operations are fundamental to data preprocessing, feature engineering, and understanding how neural network layers transform representations.

### 1(c) Focus on how linear equations and their solutions are related to matrices.

**5-6 Minute Pitch:**

Linear equations and matrices are intimately connected - every system of linear equations can be expressed as a matrix equation, and solving linear equations is fundamentally about matrix operations.

A system of m linear equations in n unknowns can be written as A**x** = **b**, where A is an m×n coefficient matrix, **x** is the n×1 vector of unknowns, and **b** is the m×1 constant vector. This compact notation reveals the geometric interpretation: we're finding which vector **x**, when transformed by A, produces **b**.

The solution space depends on the relationship between m (number of equations) and n (number of unknowns), and the rank of A (number of linearly independent rows/columns):

**Unique solution** (m = n, rank(A) = n): The system is well-determined. If det(A) ≠ 0, A is invertible and **x** = A⁻¹**b** gives the unique solution. This occurs when we have exactly enough constraints to determine all parameters uniquely - for example, fitting a line (2 parameters) through 2 points.

**No solution** (over-determined, m > n, inconsistent): More constraints than unknowns, but they conflict. The system is inconsistent. In ML, this is common with noisy data - we can't satisfy all equations exactly, so we use least squares to find the best approximate solution by minimizing ||A**x** - **b**||².

**Infinitely many solutions** (under-determined, m < n, or rank(A) < n): Fewer constraints than unknowns, or linear dependencies. The solution space is a subspace. We can add regularization (like L2 penalty) to select a unique solution, or use the minimum-norm solution.

Gaussian elimination systematically transforms the augmented matrix [A | **b**] into row-echelon form, revealing the solution structure. The reduced row-echelon form makes the solution explicit and shows whether the system is consistent.

In machine learning, we frequently solve A**x** = **b** for model fitting. For polynomial regression, A is the design matrix (Vandermonde matrix), **x** contains polynomial coefficients, and **b** contains target values. The normal equations (AᵀA)**x** = Aᵀ**b** convert over-determined systems into square systems, enabling direct solution via matrix inversion when AᵀA is invertible.

## Question 2: Exercise Week 4 (Linear Transformations)
### 2(a) Use the tutorial to focus on exploring linear transformations in 2D and 3D spaces, including operations such as scaling, shearing, reflections, rotations, and translations, while drawing connections to their extensions in higher-dimensional linear transformations. Additionally, you should explain the relationship between linear transformations and non-linear transformations including affine, thus bridging the gap between linear and more complex transformations.

**5-6 Minute Pitch:**

Linear transformations preserve vector addition and scalar multiplication: T(**u** + **v**) = T(**u**) + T(**v**) and T(c**u**) = cT(**u**). They can be represented as matrix multiplication: T(**x**) = A**x**, where A encodes the transformation.

In 2D, fundamental transformations include: **Scaling** stretches/compresses along axes using diagonal matrices diag(sₓ, sᵧ). **Rotation** by angle θ uses [[cos θ, -sin θ], [sin θ, cos θ]], preserving distances and angles. **Reflection** across lines uses matrices with determinant -1, like [[1, 0], [0, -1]] for x-axis reflection. **Shearing** skews space using matrices like [[1, k], [0, 1]], which preserves area but distorts angles.

These extend naturally to higher dimensions. A 3D rotation around an axis, or an n-dimensional scaling transformation, follows the same principles. The key insight is that linear transformations preserve the origin (T(0) = 0) and map lines to lines, parallelograms to parallelograms.

**Affine transformations** bridge linear and non-linear: T(**x**) = A**x** + **b**, adding translation via **b**. This breaks linearity because T(0) = **b** ≠ 0. However, using homogeneous coordinates, we represent affine transformations as linear: [**x'**; 1] = [[A, **b**], [0, 1]] [**x**; 1]. This trick allows composition of translations with rotations/scalings using matrix multiplication.

Affine transformations are crucial in ML: they model relationships where outputs depend linearly on inputs plus a bias term. A neural network layer computes **y** = W**x** + **b**, which is affine. Polynomial models become non-linear, but can be learned using linear methods by expanding features (e.g., [x, x², x³] for cubic polynomials).

True non-linear transformations (like sigmoid, ReLU activations) enable modeling complex decision boundaries. However, many "non-linear" models in ML are actually linear in their parameters - polynomial regression is linear in coefficients, even though it's non-linear in inputs. This distinction is crucial: we can use linear optimization (least squares) to learn non-linear functions by transforming the input space.

### 2(b) Focus on how linear and non-linear models can be learned using matrix inverses. Discuss the relationship between model complexity (e.g., polynomial degree) and the amount of data needed to accurately train these models with matrix inverses.

**5-6 Minute Pitch:**

Matrix inverses enable direct solution of model parameters when we have exactly determined or over-determined systems. For a linear model **y** = X**w**, where X is the design matrix and **w** contains parameters, we solve X**w** = **y** using **w** = X⁻¹**y** (if square) or **w** = (XᵀX)⁻¹Xᵀ**y** (least squares for over-determined systems).

**Linear models** (lines, planes, hyperplanes) require parameters equal to dimensionality plus bias. A line in 2D needs 2 parameters (slope, intercept), solvable with 2 data points. A hyperplane in n dimensions needs n+1 parameters, requiring n+1 points for exact solution.

**Non-linear models** become linear in parameters through feature expansion. A polynomial of degree d in 1D has d+1 coefficients. We construct the Vandermonde design matrix X where row i is [1, xᵢ, xᵢ², ..., xᵢᵈ]. Now **y** = X**w** is linear in **w**, even though the function is non-linear in x. We solve using matrix inverses: **w** = (XᵀX)⁻¹Xᵀ**y**.

**Model complexity vs. data requirements**: A polynomial of degree d needs at least d+1 points for a unique solution. However, with exactly d+1 points, we get perfect interpolation (zero training error) but likely poor generalization due to overfitting. More data points (m > d+1) create an over-determined system, requiring least squares. This regularization effect improves generalization.

The relationship is: **minimum data = number of parameters** for exact solution, but **recommended data >> parameters** for good generalization. For a 10th-degree polynomial (11 parameters), we need at least 11 points, but hundreds of points are needed to learn a smooth, generalizable curve. The design matrix XᵀX becomes ill-conditioned (nearly singular) when data is insufficient or poorly distributed, making inversion numerically unstable.

Higher complexity models (more parameters) are more flexible but require exponentially more data. This is the bias-variance tradeoff: simple models (low degree) may underfit, complex models (high degree) overfit without sufficient data. Matrix inversion works when the system is well-conditioned, which requires adequate, well-distributed training data relative to model complexity.

### 2(c) Focus on affine transformations, homogeneous coordinates and composition of linear transformations.

**5-6 Minute Pitch:**

**Affine transformations** combine linear transformations with translation: T(**x**) = A**x** + **b**, where A is a matrix and **b** is a translation vector. Unlike pure linear transformations, affine transformations don't preserve the origin - they can shift the entire space. Examples include: rotating then translating an object, scaling from an arbitrary point, or applying a linear transformation followed by a shift.

The challenge is that affine transformations don't compose nicely as matrices because translation addition doesn't combine with matrix multiplication. **Homogeneous coordinates** solve this elegantly by embedding n-dimensional space into (n+1)-dimensional space. We represent point **x** as [**x**; 1] (appending 1), and represent affine transformation T(**x**) = A**x** + **b** as the matrix [[A, **b**], [0, 1]] acting on [**x**; 1].

This matrix representation enables **composition of transformations** through matrix multiplication. If we want to apply rotation R, then scaling S, then translation **t**, we compute the single matrix [[S, 0], [0, 1]] × [[R, 0], [0, 1]] × [[I, **t**], [0, 1]] = [[SR, S**t**], [0, 1]]. This is computationally efficient and mathematically elegant.

In machine learning, affine transformations are everywhere: neural network layers compute **y** = W**x** + **b** (affine), which can be represented in homogeneous coordinates. Batch normalization applies affine transformations. Data augmentation uses affine transformations (rotation, translation, scaling) to expand training sets.

The composition property is crucial: we can build complex transformations from simple ones, and the order matters (matrix multiplication is non-commutative). Rotating then translating gives different results than translating then rotating. This compositionality allows us to model complex relationships by chaining simple affine operations, which is fundamental to deep learning architectures where each layer applies an affine transformation followed by a non-linearity.

## Question 3: Exercise Week 5 (Projections and Least Squares)
### 3(a) Focus on the relation between linear least squares (function minimization) and projections.

**5-6 Minute Pitch:**

Linear least squares and projections are fundamentally the same geometric operation viewed from different perspectives. Least squares minimizes ||A**x** - **b**||², finding **x** that makes A**x** as close as possible to **b** in Euclidean distance.

Geometrically, when **b** is not in the column space of A (the subspace spanned by A's columns), there's no exact solution to A**x** = **b**. The least squares solution finds the point A**x*** in the column space that's closest to **b**. This closest point is the **orthogonal projection** of **b** onto the column space of A.

The projection theorem states: the error vector **b** - A**x*** must be orthogonal to the column space of A, meaning Aᵀ(**b** - A**x***) = 0. Rearranging gives the normal equations: AᵀA**x*** = Aᵀ**b**, which yields **x*** = (AᵀA)⁻¹Aᵀ**b**.

The matrix P = A(AᵀA)⁻¹Aᵀ is the **projection matrix** that projects any vector onto the column space of A. It satisfies P² = P (idempotent) and Pᵀ = P (symmetric). The projection of **b** is P**b** = A**x***, and the residual **b** - P**b** is orthogonal to the column space.

This connection is profound: **least squares = finding the projection of the target vector onto the model space**. When fitting a line to data points, we're projecting the target vector **y** onto the 2D subspace spanned by [1, 1, ..., 1]ᵀ (constant) and [x₁, x₂, ..., xₙ]ᵀ (linear term). The fitted line is this projection, and the residuals are perpendicular to the fitted line in the geometric sense.

In higher dimensions, polynomial fitting projects **y** onto the subspace spanned by polynomial basis functions. PCA projects data onto lower-dimensional subspaces. Every linear regression is fundamentally a projection operation, making the geometric intuition of projections essential for understanding least squares optimization.

### 3(b) Focus on linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions) and the interpretation of results for various types of models (see week 7).

**5-6 Minute Pitch:**

Linear least squares provides a unified framework for fitting diverse models by constructing an appropriate **design matrix** X where each row represents a data point's transformed features, and each column represents a basis function.

For a **line** y = w₀ + w₁x, the design matrix is X = [[1, x₁], [1, x₂], ..., [1, xₙ]], where the first column (all 1s) enables the bias term w₀. We solve X**w** = **y** using least squares: **w** = (XᵀX)⁻¹Xᵀ**y**. The coefficients **w** = [w₀, w₁]ᵀ directly give intercept and slope.

For **polynomials** of degree d: y = w₀ + w₁x + w₂x² + ... + wₐxᵈ, we use the Vandermonde matrix X = [[1, x₁, x₁², ..., x₁ᵈ], [1, x₂, x₂², ..., x₂ᵈ], ...]. Higher-degree terms allow modeling curvature, but increase risk of overfitting. The coefficients indicate the contribution of each polynomial term.

For **affine functions** in multiple dimensions: y = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ, the design matrix is X = [[1, x₁₁, x₁₂, ...], [1, x₂₁, x₂₂, ...], ...]. Each coefficient wᵢ measures how much y changes per unit change in xᵢ, holding other variables constant (partial effect).

**Kernels** enable non-linear models using linear methods. Instead of explicit polynomial features, we use kernel functions K(**x**, **x'**) that compute inner products in a high-dimensional feature space. The kernel trick allows fitting complex decision boundaries without explicitly constructing high-dimensional feature vectors. Common kernels include polynomial K(**x**, **x'**) = (**x**ᵀ**x'** + 1)ᵈ and RBF K(**x**, **x'**) = exp(-γ||**x** - **x'**||²).

**Interpretation** varies by model type: Linear models have direct coefficient interpretation (slope, effect size). Polynomial coefficients are harder to interpret individually but capture non-linear relationships. Affine multivariate models show how each feature contributes additively. Kernel-based models sacrifice interpretability for flexibility - we can't directly interpret "coefficients" but can understand support vectors or feature importance.

The design matrix structure determines model capacity: more columns (features) = more parameters = greater flexibility but higher overfitting risk. Regularization (Ridge, Lasso) modifies the normal equations to control this tradeoff.

### 3(c) Learning of Affine (multivariate) functions and linear optimization.

**5-6 Minute Pitch:**

**Affine multivariate functions** have the form f(**x**) = **w**ᵀ**x** + b = w₁x₁ + w₂x₂ + ... + wₙxₙ + b, where **x** is a feature vector, **w** contains weights, and b is the bias. This generalizes lines to hyperplanes in n-dimensional space.

Learning affine functions means finding optimal **w** and b that minimize a loss function, typically mean squared error: L = (1/m)Σᵢ(yᵢ - **w**ᵀ**x**ᵢ - b)². We can absorb b into **w** by appending 1 to each **x**ᵢ, making it **w**ᵀ**x** where **x** = [x₁, ..., xₙ, 1]ᵀ and **w** = [w₁, ..., wₙ, b]ᵀ.

**Linear optimization** refers to solving this using linear algebra. The least squares solution is **w*** = (XᵀX)⁻¹Xᵀ**y**, where X is the design matrix with rows [**x**ᵢ; 1]ᵀ. This is a **closed-form solution** - we compute it directly via matrix operations, no iterative optimization needed.

The key advantage: linear optimization is fast, deterministic, and globally optimal (no local minima). The normal equations XᵀX**w** = Xᵀ**y** form a linear system we solve exactly. This works when XᵀX is invertible (full rank), which requires at least n+1 linearly independent data points for n features.

However, when XᵀX is ill-conditioned (nearly singular) or when we have many features, we use **regularized linear optimization**: minimize ||X**w** - **y**||² + λ||**w**||² (Ridge) or ||X**w** - **y**||² + λ||**w**||₁ (Lasso). These modify the normal equations to (XᵀX + λI)**w** = Xᵀ**y**, ensuring numerical stability and preventing overfitting.

Linear optimization extends beyond least squares: **linear programming** optimizes linear objectives subject to linear constraints. In ML, this appears in support vector machines (maximizing margin subject to classification constraints) and certain neural network training scenarios. The efficiency and reliability of linear optimization make it the foundation for many ML algorithms, even when the underlying model is non-linear (through feature transformations).

## Question 4: Exercise Week 6 (Mandatory 1)
### 4(a) Focus on preprocessing and feature extraction in Mandatory 1

**5-6 Minute Pitch:**

Preprocessing and feature extraction are critical first steps that transform raw data into a format suitable for machine learning. In Mandatory 1, this likely involved working with eye-tracking or gaze data that required careful preparation.

**Preprocessing** addresses data quality issues: **Normalization** scales features to similar ranges (e.g., [0,1] or z-score standardization), preventing features with larger magnitudes from dominating. **Handling missing data** through imputation (mean, median, forward-fill) or removal ensures complete feature vectors. **Outlier detection and removal** eliminates erroneous measurements that could skew models. **Temporal alignment** synchronizes data streams (e.g., eye coordinates with screen coordinates) when dealing with time-series data.

**Feature extraction** creates informative representations from raw data. For gaze data, this might include: **Coordinate transformation** from eye coordinates to screen coordinates using affine transformations learned from calibration points. **Derived features** like velocity, acceleration, or fixation duration computed from raw position data. **Temporal features** capturing patterns over time windows. **Statistical aggregations** (mean, variance) over time segments.

The design matrix construction involves organizing these features: each row is a data point, each column is a feature. For polynomial or affine models, we might create basis functions - for screen coordinate prediction, features could be [eye_x, eye_y, eye_x², eye_y², eye_x·eye_y, 1] to enable quadratic relationships.

Feature engineering choices directly impact model performance: too few features may underfit, too many may overfit. Domain knowledge guides selection - understanding that gaze data has spatial relationships suggests including interaction terms or distance-based features. The preprocessing pipeline must be applied consistently to training, validation, and test sets to avoid data leakage and ensure fair evaluation.

### 4(b) Focus on model predictions and learning Mandatory 1

**5-6 Minute Pitch:**

Model learning in Mandatory 1 likely involved predicting screen coordinates from eye-tracking data using linear or polynomial regression. The learning process follows the least squares framework.

**Model formulation**: We define a model like **y** = X**w**, where **y** contains target screen coordinates, X is the design matrix with extracted features, and **w** contains learnable parameters. For a linear model predicting screen_x from eye_x and eye_y: screen_x = w₀ + w₁·eye_x + w₂·eye_y. For polynomial models, we include higher-order terms like eye_x², eye_y², eye_x·eye_y.

**Learning process**: We solve the normal equations **w*** = (XᵀX)⁻¹Xᵀ**y** to find optimal parameters. This minimizes mean squared error between predictions and true screen coordinates. The solution projects the target vector onto the column space of the design matrix, finding the best linear combination of features.

**Prediction**: Once **w*** is learned, predictions for new eye coordinates **x**ₙₑᵥ are **ŷ** = **w***ᵀ**x**ₙₑᵥ (with appropriate feature expansion for polynomial models). The model generalizes the mapping learned from calibration data to unseen gaze positions.

**Model selection** involves choosing appropriate complexity: linear models (affine transformations) are simple and interpretable but may miss non-linear relationships. Polynomial models capture curvature but require more data and risk overfitting. Cross-validation helps select the optimal degree by evaluating generalization performance.

The learning process reveals the relationship between eye and screen coordinate systems - the learned **w** encodes the transformation (rotation, scaling, translation) that maps between these spaces. This is fundamentally learning an affine or polynomial transformation from data, demonstrating how matrix-based optimization enables model learning from examples.

### 4(c) Focus on model evaluation in Mandatory 1

**5-6 Minute Pitch:**

Model evaluation assesses how well the learned model generalizes to unseen data, using metrics that quantify prediction accuracy and methods that prevent overfitting.

**Evaluation metrics for regression**: **Mean Squared Error (MSE)** = (1/n)Σ(yᵢ - ŷᵢ)² measures average squared prediction error, penalizing large errors more heavily. **Root Mean Squared Error (RMSE)** = √MSE is in the same units as predictions, easier to interpret. **Mean Absolute Error (MAE)** = (1/n)Σ|yᵢ - ŷᵢ| is more robust to outliers. For screen coordinate prediction, these measure pixel-level accuracy.

**Train-test split**: We partition data into training (e.g., 70-80%) and test (20-30%) sets. The model learns on training data, and we evaluate on held-out test data to estimate generalization performance. This prevents overfitting - a model that memorizes training data will perform poorly on test data.

**Cross-validation**: K-fold cross-validation divides data into k folds, trains on k-1 folds, evaluates on the held-out fold, and averages results. This provides more robust performance estimates and helps with model selection (choosing polynomial degree, regularization strength). Leave-one-out cross-validation uses each point as a test case, computationally expensive but uses maximum training data.

**Visual evaluation**: Plotting predicted vs. true coordinates reveals systematic biases (e.g., consistent offset) or regions of poor performance. Residual plots (errors vs. predictions) show whether errors are random (good) or systematic (model misspecification).

**Overfitting detection**: Large gap between training and test error indicates overfitting - the model is too complex relative to available data. Solutions include: reducing model complexity (lower polynomial degree), increasing training data, or adding regularization. Good models show similar performance on training and test sets, indicating they've learned generalizable patterns rather than noise.

### 4(d) Describe vector space, basis, independence and how these are related to concepts in machine learning (learning, transformations etc). You MAY include exercises week 12 if you have done them.

**5-6 Minute Pitch:**

A **vector space** is a set of vectors closed under addition and scalar multiplication, with properties like associativity and distributivity. In ML, feature vectors live in a vector space where each dimension represents a feature, and operations like weighted combinations of features are vector space operations.

A **basis** is a set of linearly independent vectors that span the entire vector space. Any vector can be uniquely expressed as a linear combination of basis vectors. The standard basis uses unit vectors along each axis (e.g., [1,0,0], [0,1,0], [0,0,1] in 3D), but any linearly independent set of n vectors forms a basis in n-dimensional space.

**Linear independence** means no vector in a set can be written as a linear combination of the others. If vectors are linearly dependent, at least one is redundant. The **rank** of a matrix is the maximum number of linearly independent rows/columns, indicating the dimensionality of the column/row space.

In ML, these concepts are fundamental: **Feature spaces** are vector spaces where data points are vectors. **Basis functions** in polynomial regression (1, x, x², ...) form a basis for the function space we're fitting. **Design matrix rank** determines whether we have enough independent constraints to uniquely determine parameters - if rank(X) < number of parameters, the system is under-determined.

**Transformations** map vectors from one space to another. A linear transformation T: V → W preserves vector space structure. The columns of the transformation matrix form a basis for the image (output space). In PCA (week 12), we find an orthonormal basis (principal components) that optimally represents data variance - this new basis enables dimensionality reduction by projecting onto the most important directions.

**Learning** involves finding optimal representations in appropriate vector spaces. Neural networks learn transformations that map inputs through intermediate representations (hidden layers) to outputs, where each layer's weights define a basis for that representation space. Understanding vector spaces, bases, and independence helps us reason about model capacity, feature engineering, and the geometry of learning.

## Question 5: Exercise Week 7 (Model Complexity, Model seleection and noise)

### 5(a) Linear least squares problems for model fitting (design matrix, kernel, lines, polynomials, affine, and other multivariate functions).

**5-6 Minute Pitch:**

Linear least squares provides a unified framework for fitting diverse function classes by constructing appropriate design matrices that encode the model structure.

The **design matrix** X has rows corresponding to data points and columns corresponding to basis functions. For a **line** y = w₀ + w₁x, X = [[1, x₁], [1, x₂], ..., [1, xₙ]] where the constant column enables the intercept. For **polynomials** of degree d, we use the Vandermonde structure: X = [[1, x₁, x₁², ..., x₁ᵈ], ...], where each column is a monomial basis function. For **affine multivariate** functions y = **w**ᵀ**x** + b, X = [[1, x₁₁, x₁₂, ...], [1, x₂₁, x₂₂, ...], ...] where features can be raw inputs or engineered (interactions, transformations).

**Kernels** enable non-linear models using linear optimization. Instead of explicit feature expansion, kernel methods use K(**x**ᵢ, **x**ⱼ) to compute similarities. The kernel matrix K has entries Kᵢⱼ = K(**x**ᵢ, **x**ⱼ). Polynomial kernels K(**x**, **x'**) = (**x**ᵀ**x'** + 1)ᵈ implicitly map to high-dimensional polynomial features without constructing them explicitly. RBF kernels K(**x**, **x'**) = exp(-γ||**x** - **x'**||²) map to infinite-dimensional spaces, enabling very flexible models.

The least squares solution **w*** = (XᵀX)⁻¹Xᵀ**y** works for all these cases. The design matrix structure determines model capacity: more columns = more parameters = greater flexibility. However, explicit polynomial features suffer from the curse of dimensionality - a degree-d polynomial in n dimensions has (n+d choose d) terms, growing combinatorially. Kernels avoid this by working implicitly in high-dimensional spaces.

**Interpretation**: Linear models have direct coefficient meaning (effect size per unit change). Polynomial coefficients are harder to interpret but capture curvature. Kernel-based models sacrifice interpretability for flexibility - we understand them through support vectors or feature importance rather than explicit coefficients. The choice between explicit design matrices and kernels trades off interpretability, computational cost, and model flexibility.

### 5(b) Discuss the relationship between data quality, uncertainty, and the challenges of overfitting and underfitting in model learning.

**5-6 Minute Pitch:**

Data quality, uncertainty, and model complexity interact to create the fundamental challenges of overfitting and underfitting in machine learning.

**Data quality** encompasses completeness, accuracy, and representativeness. **Noise** (random measurement errors) introduces uncertainty that models shouldn't learn. **Outliers** (anomalous points) can disproportionately influence model parameters. **Missing data** creates gaps in the feature space. **Bias** (systematic errors) shifts the entire distribution. Poor data quality amplifies the risk of learning spurious patterns rather than true relationships.

**Uncertainty** has multiple sources: **Aleatoric uncertainty** (inherent randomness in the process) is irreducible - even perfect models have prediction variance. **Epistemic uncertainty** (model uncertainty due to limited data) is reducible with more training data. **Measurement uncertainty** comes from sensor limitations. Models must distinguish signal from noise, learning robust patterns while ignoring random fluctuations.

**Underfitting** occurs when models are too simple to capture underlying patterns. Symptoms: high training error, high test error, similar performance on both sets. Causes: insufficient model capacity (e.g., linear model for non-linear relationship), excessive regularization, or insufficient training. Solutions: increase model complexity, reduce regularization, or add relevant features.

**Overfitting** occurs when models memorize training data instead of learning generalizable patterns. Symptoms: low training error but high test error, large train-test gap. Causes: excessive model complexity relative to data (e.g., high-degree polynomial with few points), insufficient training data, or learning noise as signal. Solutions: reduce complexity, increase training data, add regularization, or use simpler models.

The **bias-variance tradeoff** formalizes this: total error = bias² + variance + irreducible error. High bias (underfitting) means models miss true patterns. High variance (overfitting) means models are sensitive to training data fluctuations. Optimal models balance both. Data quality affects this balance: noisy data requires simpler models (higher bias, lower variance) to avoid learning noise. Clean, abundant data allows complex models (lower bias) without excessive variance.

### 5(c) Discuss how factors affect a model’s ability to generalize to unseen data. Relate this to concepts of data evaluation, such as train-test splits, cross-validation, and performance metrics, to assess a model’s predictive capability and robustness.

**5-6 Minute Pitch:**

Generalization - a model's ability to perform well on unseen data - depends on multiple factors that we assess through rigorous evaluation protocols.

**Factors affecting generalization**: **Model complexity** must match data complexity - too simple underfits, too complex overfits. **Training data size** - more data generally improves generalization, but diminishing returns apply. **Data quality** - noisy, biased, or unrepresentative data hurts generalization. **Feature relevance** - informative features improve generalization; irrelevant features add noise. **Regularization** controls complexity, trading training fit for generalization. **Distribution shift** - if test data differs from training distribution, generalization fails.

**Train-test splits** provide the foundation for evaluation. We partition data into training (learn parameters) and test (estimate generalization) sets, typically 70-80% / 20-30%. The test set must remain untouched during model development to give unbiased performance estimates. A single split can be misleading if data is small or unrepresentative - the split might be unlucky.

**Cross-validation** addresses split variability. **K-fold CV** divides data into k folds, trains on k-1, tests on 1, repeats k times, averages results. This provides robust performance estimates and uses all data for both training and testing (at different times). **Stratified CV** maintains class distributions in each fold for classification. **Leave-one-out CV** uses each point as a test case, maximally using training data but computationally expensive.

**Performance metrics** quantify generalization: For **regression**, MSE, RMSE, MAE measure prediction accuracy; R² measures explained variance. For **classification**, accuracy, precision, recall, F1-score, ROC-AUC assess different aspects. These metrics on test/validation sets estimate true generalization error.

**Robustness assessment** involves: **Multiple metrics** - no single metric captures everything. **Cross-validation variance** - low variance across folds indicates stable performance. **Learning curves** (performance vs. training size) show if more data would help. **Error analysis** - examining failure cases reveals systematic weaknesses. **Adversarial testing** - evaluating on edge cases or corrupted data tests robustness.

Proper evaluation prevents false confidence: models that perform well on training but poorly on test are overfitted. Models with similar train/test performance likely generalize well. Cross-validation provides confidence intervals for performance estimates, helping distinguish real improvements from random variation.

## Question 6: Exercise Week 8 (Filtering)
### 6(a) Focus on filtering (1D, 2D, and n-D convolution and correlation, blurring and smoothing, and noise).

**5-6 Minute Pitch:**

Filtering operations process signals and images by applying local operations that combine neighboring values, enabling noise reduction, smoothing, and feature extraction. The fundamental operations are **convolution** and **correlation**, which are closely related.

**Convolution** (f * g)[n] = Σₖ f[k]g[n-k] slides a kernel g over signal f, computing weighted sums. For images, we use 2D convolution: (I * K)[i,j] = Σₘ,ₙ I[i-m, j-n]K[m,n]. Convolution is commutative and associative, making it mathematically elegant. **Correlation** (f ⋆ g)[n] = Σₖ f[k]g[k+n] is similar but doesn't flip the kernel - it's essentially convolution with a flipped kernel. For symmetric kernels, they're identical.

**1D filtering** processes time-series or 1D signals. A moving average filter (box filter) with kernel [1/3, 1/3, 1/3] smooths by averaging neighboring values, reducing high-frequency noise. Gaussian filters use weights from a Gaussian distribution, providing better frequency response. **2D filtering** processes images. A 3×3 Gaussian blur kernel smooths images by averaging nearby pixels, reducing noise while preserving edges better than box filters. **n-D filtering** extends to volumes, video sequences, or multi-dimensional data using n-dimensional kernels.

**Blurring and smoothing** reduce high-frequency components (noise, fine details). Gaussian blur is the most common, with kernel values proportional to exp(-(x²+y²)/(2σ²)). Larger σ creates more blur. Box filters are simpler but create artifacts (ringing). Bilateral filters preserve edges while smoothing, using both spatial and intensity similarity.

**Noise reduction** is a primary filtering application. **Additive noise** (random fluctuations) is reduced by averaging (low-pass filtering). **Salt-and-pepper noise** (random black/white pixels) requires median filtering (replacing each pixel with median of neighbors) rather than linear filters. **Gaussian noise** is effectively removed by Gaussian smoothing.

Filtering is implemented efficiently using the convolution theorem: convolution in spatial domain equals multiplication in frequency domain. Fast Fourier Transform (FFT) enables O(n log n) filtering vs. O(n²) direct convolution for large kernels. In practice, small kernels (3×3, 5×5) are applied directly, while large kernels benefit from FFT or separable filters (applying 1D filters along each dimension).

### 6(b) Focus on filtering for derivatives, gradients, and edges. You may include how these operations can be used to construct features such as HOG.

**5-6 Minute Pitch:**

Filtering enables computing derivatives, gradients, and detecting edges by using kernels that approximate differentiation operators, extracting local structure and boundaries in images.

**Derivatives** measure rate of change. The first derivative of a 1D signal f(x) is approximated by finite differences: f'(x) ≈ [f(x+1) - f(x-1)]/2, implemented as convolution with kernel [-1/2, 0, 1/2]. The **Sobel operator** uses kernels like Gₓ = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] for horizontal gradients and Gᵧ (transpose) for vertical gradients, with larger weights on center row/column for noise robustness.

**Gradients** in 2D are vectors [∂I/∂x, ∂I/∂y] indicating direction and magnitude of intensity change. **Gradient magnitude** ||∇I|| = √[(∂I/∂x)² + (∂I/∂y)²] measures edge strength. **Gradient direction** θ = arctan(∂I/∂y / ∂I/∂x) indicates edge orientation. These are computed by convolving with Sobel or Prewitt kernels, then combining horizontal and vertical components.

**Edge detection** identifies boundaries where intensity changes rapidly. The **Canny edge detector** combines: (1) Gaussian smoothing to reduce noise, (2) gradient computation (Sobel), (3) non-maximum suppression (thin edges to 1 pixel), (4) hysteresis thresholding (connect strong edges, remove weak isolated edges). **Laplacian of Gaussian (LoG)** detects edges at zero-crossings of second derivative, finding intensity extrema.

**HOG (Histogram of Oriented Gradients)** constructs powerful features for object detection by aggregating gradient information. The process: (1) Compute gradients (magnitude and direction) for each pixel. (2) Divide image into cells (e.g., 8×8 pixels). (3) Create histogram of gradient orientations (typically 9 bins: 0°, 20°, 40°, ..., 160°) weighted by gradient magnitude in each cell. (4) Normalize histograms across blocks (groups of cells, e.g., 2×2 cells) to handle lighting variations. (5) Concatenate normalized histograms into feature vector.

HOG features capture local shape and texture: edges, corners, and object boundaries produce strong gradients in specific orientations. The histogram representation is robust to small translations and deformations. These features are used in pedestrian detection, object recognition, and as inputs to classifiers (SVM, neural networks). HOG demonstrates how filtering operations (gradient computation) combined with spatial aggregation create discriminative features for machine learning.

## Question 7: Exercise Week 9 (Understanding Data and Descriptive Methods)
### 7(a) Describe correlation and covariance, explain how they are calculated, and discuss how they are useful for understanding data and for descriptive analysis.

**5-6 Minute Pitch:**

**Covariance** measures how two variables vary together. For variables X and Y with means μₓ and μᵧ, covariance is Cov(X,Y) = E[(X - μₓ)(Y - μᵧ)] = E[XY] - μₓμᵧ. For sample data, it's computed as (1/(n-1))Σᵢ(xᵢ - x̄)(yᵢ - ȳ). Covariance is positive when large X values tend to pair with large Y values, negative when they vary oppositely, and zero when variables are independent (though zero covariance doesn't guarantee independence for non-linear relationships).

**Correlation** is normalized covariance, measuring linear relationship strength on a [-1, 1] scale. Pearson correlation is r = Cov(X,Y) / (σₓσᵧ), where σₓ and σᵧ are standard deviations. Correlation = 1 indicates perfect positive linear relationship, -1 perfect negative, 0 no linear relationship. Unlike covariance, correlation is scale-invariant - multiplying variables by constants doesn't change correlation.

**Covariance matrix** Σ for a d-dimensional dataset has entries Σᵢⱼ = Cov(Xᵢ, Xⱼ), with variances on the diagonal (Cov(Xᵢ, Xᵢ) = Var(Xᵢ)) and covariances off-diagonal. It's symmetric and positive semi-definite, encoding all pairwise relationships.

**Understanding data**: Covariance/correlation reveal feature relationships. High positive correlation suggests redundant features (one can predict the other). Negative correlation indicates inverse relationships. Near-zero correlation suggests independence. **Multicollinearity** (high correlations among features) causes problems in regression - it makes coefficient estimates unstable and hard to interpret.

**Descriptive analysis**: Correlation matrices visualize relationships in datasets, guiding feature selection. In PCA, we analyze the covariance matrix to find directions of maximum variance. Correlation helps identify clusters of related variables. For time-series, autocorrelation (correlation with lagged values) reveals patterns and periodicity.

Covariance is fundamental to multivariate statistics: it appears in multivariate Gaussian distributions, determines ellipse shapes in 2D scatter plots, and underlies many ML algorithms including PCA, linear discriminant analysis, and Gaussian mixture models.

### 7(b) Explain how descriptive statistics can be used to assess model selection and the generalization ability of machine learning models.

**5-6 Minute Pitch:**

Descriptive statistics provide quantitative summaries that help assess model quality, guide model selection, and diagnose generalization issues without requiring test data.

**Error statistics** summarize prediction quality: **Mean error** indicates systematic bias (consistently over/under-predicting). **Standard deviation of errors** measures prediction consistency - low std means stable predictions. **Error distribution** (histogram, Q-Q plots) reveals if errors are normally distributed (expected for well-specified models) or have skew/outliers indicating model misspecification.

**Residual analysis** examines prediction errors: **Residual plots** (errors vs. predictions) should show random scatter. Patterns (curves, funnels) indicate model misspecification - e.g., curved patterns suggest missing non-linear terms. **Autocorrelation of residuals** (for time-series) should be near zero - significant autocorrelation indicates the model misses temporal dependencies.

**Model complexity assessment**: **R² (coefficient of determination)** = 1 - (SS_res/SS_tot) measures explained variance. High R² on training but low on validation indicates overfitting. **Adjusted R²** penalizes model complexity, helping compare models with different numbers of parameters. **AIC/BIC** (information criteria) balance fit quality and complexity, lower is better.

**Generalization indicators**: **Train-test error gap** - large gaps suggest overfitting. **Cross-validation variance** - high variance across folds indicates instability. **Learning curves** plot error vs. training size - if validation error plateaus while training error decreases, more data won't help (overfitting). If both decrease, more data would improve generalization.

**Feature statistics**: **Feature importance** (coefficient magnitudes, correlation with target) identifies which features matter. **Feature correlations** reveal multicollinearity causing instability. **Feature distributions** - if training and test distributions differ (distribution shift), generalization will fail.

**Diagnostic statistics** flag problems: **Cook's distance** identifies influential outliers. **Leverage** measures how unusual input values are. **Variance inflation factor (VIF)** quantifies multicollinearity severity. High values indicate problematic features.

These statistics guide model selection: choose models with good error statistics, stable cross-validation performance, appropriate complexity (not too high R² on training), and well-behaved residuals. They help diagnose whether poor performance comes from underfitting (high bias), overfitting (high variance), or data issues (distribution shift, outliers).

### 7(c) Describe noise, outliers, and missing data.

**5-6 Minute Pitch:**

**Noise, outliers, and missing data** are three fundamental data quality issues that must be understood and handled appropriately in machine learning.

**Noise** is random variation that obscures true signals. **Additive noise** (e.g., y = f(x) + ε where ε ~ N(0, σ²)) adds random fluctuations. **Measurement noise** comes from sensor limitations, quantization, or environmental factors. **Label noise** occurs when training labels are incorrect. Noise is typically modeled as random variables (often Gaussian) with zero mean. It's irreducible - even perfect models have prediction variance due to noise. Models should learn robust patterns while ignoring noise, not memorize it. Overfitting often means learning noise as signal. Smoothing, regularization, and ensemble methods help models be robust to noise.

**Outliers** are data points that deviate significantly from the majority. **Point outliers** are individual anomalous observations. **Contextual outliers** are normal in isolation but anomalous in context (e.g., high temperature in winter). **Collective outliers** are groups that are anomalous together. Outliers can be: **Errors** (measurement mistakes, data entry errors) - should be removed or corrected. **Rare but valid events** (fraud, rare diseases) - should be preserved as they may be important. **Different distributions** (contamination) - may indicate data quality issues.

**Detection methods**: Statistical (z-scores, IQR method: Q1 - 1.5×IQR, Q3 + 1.5×IQR), distance-based (isolation forest, DBSCAN), model-based (high residuals in regression). **Handling**: Remove if errors, transform (log, winsorizing), use robust methods (median, robust regression), or treat as separate class.

**Missing data** occurs when values are unobserved. **Missing Completely At Random (MCAR)** - missingness independent of observed and unobserved data (e.g., random sensor failure). **Missing At Random (MAR)** - missingness depends on observed data but not missing values (e.g., income missing more often for unemployed). **Missing Not At Random (MNAR)** - missingness depends on missing values themselves (e.g., people with high income less likely to report it).

**Handling strategies**: **Deletion** (listwise, pairwise) - simple but loses information, can introduce bias if not MCAR. **Imputation** - mean/median (simple), regression (predicts from other features), multiple imputation (accounts for uncertainty), KNN imputation (uses similar cases). **Model-based** - some algorithms handle missing data natively (tree-based methods). **Indicator variables** - add binary flags for missingness, which can be informative if MAR.

The choice of handling method depends on the missingness mechanism and the analysis goal. Improper handling can introduce bias or reduce statistical power.

### 7(d) Focus on uncertainty, noise, data cleaning in relation to regression, classification, clustering or dimensionality reduction (Covariance, distributions (e.g Normal/Gaussian))

**5-6 Minute Pitch:**

Uncertainty, noise, and data cleaning interact differently with various ML tasks, and understanding probability distributions (especially Gaussian) is crucial for proper handling.

**Regression** assumes a probabilistic model: y = f(x) + ε, where ε ~ N(0, σ²) represents noise. The **Gaussian distribution** is natural because: (1) Central Limit Theorem - sums of random variables tend to Gaussian, (2) Maximum likelihood estimation under Gaussian noise gives least squares, (3) Gaussian has nice properties (closed-form solutions, conjugate priors). **Covariance** in multivariate regression: if errors are correlated, we use weighted least squares with covariance matrix Σ. **Data cleaning** removes outliers that violate Gaussian assumptions, handles missing values through imputation, and normalizes features to similar scales. **Uncertainty quantification** provides prediction intervals: ŷ ± z·σ, where σ estimates noise variance.

**Classification** models class probabilities. **Gaussian Naive Bayes** assumes features are Gaussian within each class: P(x|class) ~ N(μ_class, Σ_class). The covariance matrix captures feature relationships within classes. **Logistic regression** doesn't assume Gaussian features but models log-odds as linear, with errors following logistic distribution. **Data cleaning** is critical: class imbalance requires balancing, label noise causes misclassification, missing features need imputation. **Uncertainty** appears as predicted probabilities - low confidence (probabilities near 0.5) indicates uncertain predictions.

**Clustering** groups similar data points. **Gaussian Mixture Models (GMM)** model clusters as multivariate Gaussians with means μₖ and covariance matrices Σₖ. Each cluster's covariance determines its shape (spherical if diagonal, ellipsoidal if full). **K-means** assumes spherical clusters (implicitly uses identity covariance). **Noise** creates outliers that don't belong to any cluster - methods like DBSCAN handle this explicitly. **Data cleaning** normalizes features so distance metrics aren't dominated by high-variance features. Covariance structure determines cluster shapes - if features are correlated, clusters are elongated along correlation directions.

**Dimensionality reduction** (PCA) is fundamentally about covariance. PCA finds directions of maximum variance by eigendecomposition of the **covariance matrix** Σ = (1/n)XᵀX (after centering). Eigenvalues λᵢ give variance along principal components, eigenvectors give directions. **Noise** appears as small eigenvalues - components with λᵢ near zero capture mostly noise and can be discarded. **Gaussian assumption**: PCA is optimal (in maximum variance sense) for Gaussian data, but works well for other distributions too. **Data cleaning** is essential: outliers distort covariance estimates, missing data requires imputation before PCA, normalization ensures all features contribute equally. **Uncertainty** in PCA: reconstruction error measures information loss, eigenvalues quantify variance explained by each component.

Across all tasks, **Gaussian distributions** provide mathematical tractability and often good approximations. **Covariance** captures relationships and uncertainty structure. **Data cleaning** ensures assumptions are met and improves model quality. Understanding these connections enables proper application of ML methods.

## Question 8: Exercise Week 10-11 (Classification)
### 8(a) Linear classification, kernels, and classification boundaries

**5-6 Minute Pitch:**

**Linear classification** finds a hyperplane that separates classes in feature space. A linear classifier has the form f(**x**) = **w**ᵀ**x** + b, where the **decision boundary** is the hyperplane **w**ᵀ**x** + b = 0. Points with f(**x**) > 0 are classified as one class, f(**x**) < 0 as the other. The vector **w** is normal to the decision boundary, and |b|/||**w**|| is the distance from origin to the boundary.

**Perceptron** is the simplest linear classifier: it finds any separating hyperplane by iteratively updating **w** when misclassifications occur. **Linear SVM** finds the optimal separating hyperplane that maximizes the **margin** (distance to nearest points of each class). The margin-maximizing hyperplane is robust and generalizes well. Support vectors are the training points closest to the boundary - they determine the solution.

**Kernels** enable non-linear classification using linear methods. The **kernel trick** maps data to a high-dimensional feature space where classes become linearly separable, without explicitly computing the transformation. A kernel function K(**x**, **x'**) computes inner products in this high-dimensional space. **Polynomial kernels** K(**x**, **x'**) = (**x**ᵀ**x'** + 1)ᵈ map to polynomial features. **RBF kernels** K(**x**, **x'**) = exp(-γ||**x** - **x'**||²) map to infinite-dimensional spaces, enabling very flexible boundaries.

**Classification boundaries** separate the feature space into regions assigned to each class. **Linear boundaries** are hyperplanes - simple but limited to linearly separable data. **Non-linear boundaries** (enabled by kernels) can be curves, allowing classification of complex patterns. The boundary shape depends on the kernel: polynomial kernels create polynomial curves, RBF kernels create smooth, flexible curves that can separate intricate patterns.

Kernelized SVMs find boundaries of the form Σᵢ αᵢyᵢK(**x**ᵢ, **x**) + b = 0, where only support vectors (αᵢ ≠ 0) matter. This is computationally efficient - we never explicitly work in the high-dimensional space. Kernels make "non-linear" classification use the same linear optimization framework, just in a transformed space.

### 8(b) Logistic regression and classification boundaries

**5-6 Minute Pitch:**

**Logistic regression** is a probabilistic linear classifier that models class probabilities using the logistic (sigmoid) function. Unlike hard linear classification (which outputs class labels), logistic regression outputs probabilities P(class=1|**x**) = σ(**w**ᵀ**x** + b) = 1/(1 + exp(-(**w**ᵀ**x** + b))), where σ is the sigmoid function mapping real numbers to [0,1].

The model assumes the **log-odds** (logit) are linear: log(P/(1-P)) = **w**ᵀ**x** + b. This means the decision boundary (where P = 0.5, so log-odds = 0) is the hyperplane **w**ᵀ**x** + b = 0, same as linear classification. However, logistic regression provides probability estimates, not just class labels.

**Learning** minimizes the **cross-entropy loss** (negative log-likelihood): L = -Σᵢ [yᵢ log(ŷᵢ) + (1-yᵢ)log(1-ŷᵢ)], where yᵢ ∈ {0,1} are true labels and ŷᵢ are predicted probabilities. This loss is convex, ensuring global optimum. Unlike least squares (used in regression), cross-entropy is appropriate for probabilities and penalizes confident wrong predictions heavily.

**Classification boundaries**: The decision boundary is where P(class=1) = 0.5, i.e., **w**ᵀ**x** + b = 0. This is a linear hyperplane. Points far from the boundary have probabilities near 0 or 1 (high confidence), points near the boundary have probabilities near 0.5 (uncertainty). The boundary shape is linear, but the probability surface is S-shaped (sigmoid), transitioning smoothly from 0 to 1.

**Multiclass extension**: **Softmax regression** (multinomial logistic regression) generalizes to K classes: P(class=k|**x**) = exp(**w**ₖᵀ**x** + bₖ) / Σⱼ exp(**w**ⱼᵀ**x** + bⱼ). Each class gets its own weight vector, and probabilities sum to 1. Decision boundaries are still linear (hyperplanes), but now we have K-1 boundaries separating K classes.

**Advantages**: Provides probability estimates (useful for uncertainty quantification), works well with small datasets, interpretable coefficients (log-odds ratios), and handles multi-class naturally. **Limitations**: Assumes linear decision boundaries (though can be extended with kernels or feature engineering), may struggle with non-linearly separable data without transformations.

### 8(c) Linear and non-linear decision boundaries including SVM (include week 10) and possibly HOG features.

**5-6 Minute Pitch:**

Decision boundaries separate feature space into class regions. **Linear boundaries** are hyperplanes - simple, interpretable, but limited to linearly separable data. **Non-linear boundaries** are curves/surfaces that can separate complex patterns, enabled by kernels, feature engineering, or non-linear models.

**Support Vector Machines (SVM)** find optimal decision boundaries. **Linear SVM** maximizes the margin (distance from boundary to nearest training points), finding the hyperplane **w**ᵀ**x** + b = 0 that best separates classes. Support vectors (points on margin boundaries) determine the solution. The optimization problem maximizes margin subject to classification constraints, solvable via quadratic programming.

**Kernelized SVM** enables non-linear boundaries. By mapping data to high-dimensional spaces via kernels, classes become linearly separable there, creating non-linear boundaries in original space. **Polynomial kernels** K(**x**, **x'**) = (**x**ᵀ**x'** + 1)ᵈ create polynomial decision boundaries. **RBF kernels** K(**x**, **x'**) = exp(-γ||**x** - **x'**||²) create smooth, flexible boundaries that can separate intricate patterns. The parameter γ controls flexibility - large γ creates complex boundaries (risk of overfitting), small γ creates smoother boundaries.

**HOG (Histogram of Oriented Gradients) features** are powerful for image classification. HOG computes gradient histograms in local image regions, capturing edge and texture information. These features are then used with classifiers (linear SVM, kernel SVM) to create decision boundaries. HOG + linear SVM was historically very successful for pedestrian detection - the engineered features capture relevant structure, allowing even linear boundaries to work well. HOG + RBF SVM can create non-linear boundaries in HOG feature space, handling more complex patterns.

**Boundary complexity tradeoff**: Linear boundaries (simple models) are interpretable and less prone to overfitting but may underfit complex data. Non-linear boundaries (complex models) can fit intricate patterns but risk overfitting and are harder to interpret. **Feature engineering** (like HOG) can make linear boundaries effective by transforming the input space. **Kernels** provide non-linearity without explicit feature engineering but sacrifice interpretability.

The choice depends on data complexity: linearly separable data needs linear boundaries, complex patterns need non-linear boundaries or good features. SVMs with appropriate kernels provide a principled way to learn non-linear boundaries while controlling complexity through regularization.

## Question 9: Exercise Week 11 (Evaluation)
### 9(a) Metrics/Evaluation of Classifiers

**5-6 Minute Pitch:**

Classifier evaluation requires metrics that capture different aspects of performance, as accuracy alone can be misleading, especially with imbalanced data.

**Confusion matrix** organizes predictions: rows = true classes, columns = predicted classes. For binary classification, this gives: **True Positives (TP)** - correctly predicted positive, **True Negatives (TN)** - correctly predicted negative, **False Positives (FP)** - negative predicted as positive (Type I error), **False Negatives (FN)** - positive predicted as negative (Type II error).

**Basic metrics**: **Accuracy** = (TP + TN) / (TP + TN + FP + FN) measures overall correctness but is misleading with class imbalance (e.g., 99% accuracy if 99% of data is one class). **Precision** = TP / (TP + FP) measures how many predicted positives are actually positive (low precision = many false alarms). **Recall (Sensitivity)** = TP / (TP + FN) measures how many actual positives are found (low recall = missing many positives). **Specificity** = TN / (TN + FP) measures how many negatives are correctly identified.

**F1-score** = 2·(Precision·Recall) / (Precision + Recall) is the harmonic mean, balancing precision and recall. Useful when both are important. **Fβ-score** generalizes this with β controlling recall vs. precision emphasis (β > 1 favors recall, β < 1 favors precision).

**ROC curve** plots True Positive Rate (Recall) vs. False Positive Rate (1 - Specificity) as the classification threshold varies. **AUC-ROC** (area under curve) measures separability - AUC = 1.0 means perfect separation, AUC = 0.5 means random. ROC is threshold-invariant and works well with balanced data. **PR curve** (Precision-Recall) plots Precision vs. Recall, better for imbalanced data as it focuses on the minority class.

**Multiclass metrics**: **Macro-averaging** computes metric per class then averages (treats all classes equally). **Micro-averaging** aggregates all predictions first then computes metric (dominated by frequent classes). **Weighted averaging** accounts for class frequencies.

**When to use what**: Accuracy for balanced data. Precision when false positives are costly. Recall when false negatives are costly. F1 when both matter equally. ROC-AUC for threshold selection and balanced data. PR-AUC for imbalanced data. The choice depends on the application's cost structure and class distribution.

### 9(b) Metrics/Evaluation of Regression

**5-6 Minute Pitch:**

Regression evaluation metrics quantify prediction accuracy and assess how well models capture relationships between features and continuous targets.

**Error-based metrics**: **Mean Squared Error (MSE)** = (1/n)Σ(yᵢ - ŷᵢ)² averages squared prediction errors. It penalizes large errors heavily (quadratic penalty) and is differentiable, making it suitable for optimization. **Root Mean Squared Error (RMSE)** = √MSE is in the same units as predictions, easier to interpret (e.g., "RMSE of 5.2 degrees" for temperature prediction). **Mean Absolute Error (MAE)** = (1/n)Σ|yᵢ - ŷᵢ| averages absolute errors, more robust to outliers than MSE (linear vs. quadratic penalty). **Median Absolute Error** is even more robust, using median instead of mean.

**Variance-explained metrics**: **R² (coefficient of determination)** = 1 - (SS_res/SS_tot) = 1 - (Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²) measures proportion of variance explained. R² = 1 means perfect predictions, R² = 0 means model performs as well as predicting the mean, R² < 0 means worse than baseline. **Adjusted R²** = 1 - [(1-R²)(n-1)/(n-p-1)] penalizes model complexity (p = number of parameters), enabling fair comparison across models with different numbers of features.

**Relative metrics**: **Mean Absolute Percentage Error (MAPE)** = (100/n)Σ|yᵢ - ŷᵢ|/|yᵢ| expresses errors as percentages, useful for comparing across different scales. Problems when yᵢ ≈ 0. **Symmetric MAPE** addresses this by using (yᵢ + ŷᵢ)/2 in denominator.

**Distribution metrics**: **Quantile loss** evaluates predictions at different quantiles (useful for uncertainty estimation). **Correlation coefficient** r measures linear relationship strength between predictions and targets, but doesn't capture systematic bias.

**Visual evaluation**: **Scatter plots** (predicted vs. actual) reveal systematic biases (points off diagonal), heteroscedasticity (varying spread), or non-linear patterns. **Residual plots** (errors vs. predictions) should show random scatter - patterns indicate model misspecification. **Q-Q plots** check if residuals are normally distributed (expected for well-specified models).

**When to use what**: MSE/RMSE for optimization and when large errors are particularly costly. MAE for robustness to outliers. R² for variance explanation. MAPE for percentage interpretation. Multiple metrics together provide comprehensive assessment - no single metric captures everything.

### 9(c) Imbalanced data for classification and regression

**5-6 Minute Pitch:**

Imbalanced data occurs when classes (classification) or target value ranges (regression) are unequally represented, creating evaluation and learning challenges.

**Imbalanced classification**: When one class dominates (e.g., 95% negative, 5% positive), accuracy is misleading - a "dumb" classifier predicting the majority class achieves high accuracy. The minority class is often the important one (fraud, rare diseases).

**Handling strategies**: **Resampling** - **Oversampling** duplicates minority class examples (SMOTE creates synthetic examples), **undersampling** removes majority class examples (risks losing information). **Class weights** penalize misclassifying minority class more heavily in the loss function. **Threshold tuning** - move decision threshold to favor minority class (trade precision for recall). **Ensemble methods** combine multiple models, some trained on balanced subsets.

**Evaluation for imbalanced classification**: **Precision-Recall curve** and **PR-AUC** focus on minority class performance, better than ROC for imbalanced data. **F1-score** balances precision and recall. **Confusion matrix** reveals class-specific performance. **Stratified sampling** in cross-validation maintains class proportions.

**Imbalanced regression**: When target values are unequally distributed (e.g., most houses are $200K-$500K, few are $2M+), models may perform poorly on rare value ranges.

**Handling strategies**: **Resampling** - oversample rare value ranges or undersample common ranges. **Stratified sampling** - divide target into bins, sample equally from each. **Weighted loss** - assign higher weights to rare value ranges during training. **Quantile regression** - predict different quantiles, useful for imbalanced distributions. **Transformation** - log transform for skewed distributions, making them more balanced.

**Evaluation for imbalanced regression**: **Stratified metrics** - compute errors separately for different value ranges. **Quantile-based metrics** - evaluate performance at different quantiles. **Visualization** - scatter plots colored by value ranges reveal where models fail. **Domain-specific metrics** - for example, in medical costs prediction, errors on expensive cases may matter more.

**Key principle**: Standard metrics (accuracy, overall MSE) can hide poor performance on important but rare cases. Always examine performance stratified by class/value range and use appropriate metrics that reflect the application's priorities.

## Question 10: Exercise Week 12 + Assignment 2 (Principal Component Analysis)
### 10(a) Basis and transformations

**5-6 Minute Pitch:**

A **basis** is a set of linearly independent vectors that span a vector space - any vector in the space can be uniquely expressed as a linear combination of basis vectors. The **standard basis** uses unit vectors along coordinate axes (e.g., [1,0,0], [0,1,0], [0,0,1] in 3D), but any linearly independent set of n vectors forms a basis in n-dimensional space.

**Orthonormal bases** have vectors that are unit length and mutually perpendicular (orthogonal). They're particularly nice: coordinates are computed via inner products (projection), and transformations between orthonormal bases preserve lengths and angles. The standard basis is orthonormal, but rotated coordinate systems also provide orthonormal bases.

**Transformations** map vectors from one space to another. A **linear transformation** T satisfies T(**u** + **v**) = T(**u**) + T(**v**) and T(c**u**) = cT(**u**), and can be represented as matrix multiplication T(**x**) = A**x**. The columns of A are the images of the standard basis vectors under T - they form a basis for the image (output) space.

**Change of basis**: Representing the same vector in different bases requires transformation. If **v** has coordinates [c₁, c₂, ..., cₙ] in basis B₁ and we want coordinates in basis B₂, we use a change-of-basis matrix P where columns are B₁ vectors expressed in B₂ coordinates. Then coordinates in B₂ are P[c₁, ..., cₙ]ᵀ.

**Basis in ML**: **Feature spaces** use bases - each feature is a basis vector. **Polynomial regression** uses monomial basis [1, x, x², ...]. **Fourier analysis** uses sinusoidal basis functions. **PCA** finds an optimal orthonormal basis (principal components) that maximizes variance. **Neural networks** learn transformations between representations, where each layer's weights define a basis for that representation space.

**Optimal bases**: PCA finds the basis that best represents data variance - the first principal component is the direction of maximum variance, the second is orthogonal to the first with maximum remaining variance, etc. This creates a coordinate system aligned with data structure, enabling dimensionality reduction by projecting onto the most important directions. Understanding bases helps us reason about feature engineering, dimensionality reduction, and how neural networks transform representations.

### 10(b) Dimensionality reduction and PCA. Focus on mandatory 2

**5-6 Minute Pitch:**

**Dimensionality reduction** projects high-dimensional data onto lower-dimensional subspaces while preserving important information. This reduces computational cost, mitigates the curse of dimensionality, enables visualization, and can improve generalization by removing noise.

**Principal Component Analysis (PCA)** is the most common linear dimensionality reduction method. PCA finds an orthonormal basis (principal components) that maximizes variance in the projected space. The first principal component **u**₁ maximizes Var(**u**ᵀ**X**) subject to ||**u**|| = 1. Subsequent components maximize variance while being orthogonal to previous ones.

**PCA computation**: (1) Center data (subtract mean). (2) Compute covariance matrix Σ = (1/n)XᵀX. (3) Eigendecomposition: Σ = UΛUᵀ, where columns of U are eigenvectors (principal components) and Λ contains eigenvalues (variances). (4) Project data: **Y** = **X**Uₖ, where Uₖ contains top k eigenvectors. Eigenvalues λᵢ give variance along each component - we keep components with large eigenvalues.

**Variance explained**: The proportion of variance explained by k components is (Σᵢ₌₁ᵏ λᵢ) / (Σᵢ λᵢ). We choose k such that, say, 95% of variance is explained, or use a scree plot (eigenvalues vs. component number) to find the "elbow" where eigenvalues drop off.

**In Mandatory 2**, PCA likely involved: **Data preprocessing** - centering features, possibly normalizing. **Covariance computation** - analyzing feature relationships. **Component selection** - choosing how many components to keep based on variance explained or visualization needs. **Reconstruction** - projecting back to original space to assess information loss. **Interpretation** - understanding what each principal component represents (combinations of original features).

**Applications**: **Visualization** - 2D/3D projections of high-dimensional data. **Noise reduction** - discarding low-variance components (often noise). **Feature extraction** - using principal components as new features. **Compression** - storing data in lower-dimensional space.

**Limitations**: PCA is linear - it can't capture non-linear relationships. It assumes variance is the right thing to preserve - sometimes other criteria matter more. It's sensitive to scaling - features with larger variance dominate. Understanding these limitations helps choose when PCA is appropriate vs. non-linear methods (autoencoders, t-SNE).

### 10(c) Generating models and PCA

**5-6 Minute Pitch:**

PCA can be used to **generate** new data samples by modeling the distribution in the reduced-dimensional space and sampling from it, then projecting back to original space.

**Generative process**: (1) Project training data to PCA space: **Y** = **X**Uₖ (k principal components). (2) Model the distribution of **Y** (often assumed Gaussian: **Y** ~ N(μ, Σ), where μ and Σ are estimated from projected data). (3) Sample new points **y**ₙₑᵥ from this distribution. (4) Project back to original space: **x**ₙₑᵥ = **y**ₙₑᵥUₖᵀ + **x̄** (add back the mean).

This generates data in the **subspace spanned by principal components** - new samples are linear combinations of the top k principal components. The generated data preserves the main patterns (high variance directions) but loses details captured by discarded components.

**Probabilistic PCA (PPCA)** formalizes this: it models data as **x** = W**z** + **μ** + **ε**, where **z** ~ N(0, I) is a latent variable in k-dimensional space, W contains principal components, and **ε** ~ N(0, σ²I) is noise. This provides a probabilistic generative model where we can sample **z** and generate **x**.

**Applications**: **Data augmentation** - generating synthetic training examples. **Missing data imputation** - projecting to PCA space, imputing there, projecting back. **Anomaly detection** - points far from the PCA subspace are anomalous. **Denoising** - projecting to PCA space and back removes noise in low-variance directions.

**Limitations**: Generated samples are constrained to the linear subspace - they can't capture non-linear patterns. The Gaussian assumption may not hold. Generated data may lack realism if important variance is in discarded components.

**Connection to autoencoders**: PCA is a linear autoencoder - encoding projects to PCA space, decoding projects back. Non-linear autoencoders generalize this to learn non-linear manifolds, enabling more flexible generative models. Understanding PCA's generative aspect bridges to modern deep generative models (VAEs, GANs) that learn non-linear data manifolds.

### 10(d) Eigenvalues, covariance matrix and basis

**5-6 Minute Pitch:**

Eigenvalues, the covariance matrix, and basis concepts are intimately connected in PCA and many ML methods.

**Covariance matrix** Σ = (1/n)XᵀX (after centering) encodes all pairwise feature relationships. Diagonal entries are variances (Cov(Xᵢ, Xᵢ) = Var(Xᵢ)), off-diagonal entries are covariances. It's symmetric (Σ = Σᵀ) and positive semi-definite (all eigenvalues ≥ 0), meaning it represents a valid covariance structure.

**Eigendecomposition** of the covariance matrix: Σ = UΛUᵀ, where U contains **eigenvectors** (columns) and Λ is diagonal with **eigenvalues**. Eigenvectors are orthonormal (UᵀU = I), forming an orthonormal basis. Eigenvalues are non-negative and typically ordered λ₁ ≥ λ₂ ≥ ... ≥ λₙ.

**Geometric interpretation**: The covariance matrix defines an ellipsoid in feature space. Eigenvectors are the **principal axes** of this ellipsoid (directions of maximum/minimum spread). Eigenvalues are the **squared lengths** of these axes - larger eigenvalues mean more variance (spread) along that direction.

**PCA connection**: Principal components are the **eigenvectors** of the covariance matrix, ordered by decreasing **eigenvalues**. The first PC (largest eigenvalue) is the direction of maximum variance. Each eigenvalue λᵢ gives the variance along the i-th principal component. The proportion of variance explained by component i is λᵢ / (Σⱼ λⱼ).

**Basis perspective**: Eigenvectors form an **orthonormal basis** for the feature space. This basis is special - it's aligned with the data's covariance structure. Representing data in this basis (PCA coordinates) decorrelates features - in the PCA basis, the covariance matrix is diagonal (only variances, no covariances). This is the **Karhunen-Loève transform** - finding the basis that diagonalizes the covariance matrix.

**Dimensionality reduction**: By keeping only eigenvectors with large eigenvalues, we keep the directions with most variance (information). The discarded directions (small eigenvalues) typically capture noise. Projecting onto the top k eigenvectors gives the k-dimensional representation that preserves maximum variance.

This connection - **covariance matrix → eigenvalues/eigenvectors → optimal basis → dimensionality reduction** - is fundamental to understanding PCA and appears in many ML methods (LDA, factor analysis, spectral clustering).

## Question 11: Exercise Week 13 (Clustering )
### 11(a) K-means and Mean shift

**5-6 Minute Pitch:**

**K-means** and **Mean shift** are both clustering algorithms but use different approaches: K-means partitions data into k predetermined clusters, while Mean shift finds clusters by identifying density modes without specifying k.

**K-means** algorithm: (1) Initialize k cluster centers (centroids) randomly. (2) Assign each point to nearest centroid. (3) Update centroids to mean of assigned points. (4) Repeat steps 2-3 until convergence (assignments don't change). It minimizes within-cluster sum of squares: Σₖ Σᵢ∈Cₖ ||**x**ᵢ - **μ**ₖ||², where Cₖ is cluster k and **μ**ₖ is its centroid.

**K-means properties**: Simple, fast (O(nkd) per iteration), works well with spherical clusters of similar size. **Limitations**: Requires specifying k, sensitive to initialization (can get stuck in local minima), assumes spherical clusters, sensitive to outliers. **K-means++** improves initialization by choosing initial centroids far apart.

**Mean shift** is a mode-seeking algorithm that finds clusters by identifying local maxima of the probability density. Algorithm: (1) For each point, compute weighted mean of nearby points (using a kernel, typically Gaussian). (2) Shift the point toward this mean. (3) Repeat until convergence (points converge to modes). Points converging to the same mode belong to the same cluster.

**Mean shift properties**: Automatically determines number of clusters (no k needed), finds clusters of arbitrary shape (not just spherical), robust to outliers. **Limitations**: Computationally expensive (O(n²) in naive implementation), sensitive to bandwidth parameter (kernel width), can merge nearby modes if bandwidth too large.

**Key differences**: K-means is **partition-based** - divides data into k groups. Mean shift is **density-based** - finds dense regions. K-means is faster and simpler but requires k and assumes spherical clusters. Mean shift is more flexible (arbitrary shapes) and automatic (no k) but slower and requires bandwidth tuning. **When to use**: K-means for speed and when k is known. Mean shift when cluster shapes are non-spherical or k is unknown.

### 11(b) K-means and Algomerative clustering

**5-6 Minute Pitch:**

**K-means** and **Agglomerative clustering** represent different clustering paradigms: K-means is partition-based (divides data into k groups), while Agglomerative is hierarchical (builds a tree of cluster merges).

**K-means** (covered in 11a) partitions data by iteratively updating cluster centers. It's a **flat clustering** method - produces a single partition with k clusters, no hierarchical structure.

**Agglomerative clustering** is a **bottom-up hierarchical** method: (1) Start with each point as its own cluster. (2) Iteratively merge the two closest clusters. (3) Continue until all points are in one cluster (or until k clusters remain). This creates a **dendrogram** (tree) showing the merge sequence.

**Linkage criteria** determine which clusters to merge: **Single linkage** uses minimum distance between any points in two clusters (can create long, chain-like clusters). **Complete linkage** uses maximum distance (creates compact clusters). **Average linkage** uses mean distance between all pairs (balanced). **Ward linkage** minimizes increase in within-cluster variance (similar to K-means objective).

**Key differences**: **Structure**: K-means gives flat partition; Agglomerative gives hierarchical tree (can extract k clusters at any level). **Flexibility**: Agglomerative can find non-spherical clusters (with appropriate linkage), K-means assumes spherical. **Computation**: K-means is O(nkd) per iteration, typically fast; Agglomerative is O(n² log n) or O(n³), slower for large datasets. **Initialization**: K-means needs k and good initialization; Agglomerative needs linkage choice but no k (extract k from dendrogram).

**When to use**: **K-means** for speed, large datasets, when k is known, and spherical clusters are expected. **Agglomerative** when hierarchical structure is meaningful (e.g., taxonomy), when cluster shapes are non-spherical, when you want to explore different k values via dendrogram, or for smaller datasets where computation is feasible.

**Dendrogram interpretation**: Height represents distance at which clusters merged. Cutting the dendrogram at a certain height gives a partition. Long vertical lines indicate natural cluster separations. This visualization helps choose k and understand cluster relationships.

### 11(c) Kmeans and ELBOW

**5-6 Minute Pitch:**

The **Elbow method** is a heuristic for choosing the optimal number of clusters k in K-means when k is unknown, which is a fundamental challenge since K-means requires k as input.

**K-means objective**: Minimize within-cluster sum of squares (WCSS) = Σₖ Σᵢ∈Cₖ ||**x**ᵢ - **μ**ₖ||², also called **inertia**. As k increases, WCSS decreases (more clusters = tighter clusters = lower error). However, increasing k beyond the true number of clusters provides diminishing returns and risks overfitting.

**Elbow method**: Plot WCSS (or inertia) vs. k. The plot typically shows a sharp decrease followed by a gradual decrease. The **"elbow"** is the point where the rate of decrease sharply changes - this suggests the optimal k. Before the elbow, adding clusters significantly reduces error (finding real structure). After the elbow, adding clusters provides little benefit (splitting existing clusters unnecessarily).

**Procedure**: (1) Run K-means for k = 1, 2, 3, ..., k_max. (2) Compute WCSS for each k. (3) Plot k vs. WCSS. (4) Identify the elbow (point of maximum curvature or where slope changes sharply). (5) Choose k at the elbow.

**Challenges**: The elbow isn't always clear - sometimes there's no obvious elbow, or multiple elbows. The method is subjective - different people might identify different elbows. It assumes clusters are well-separated and similar in size.

**Alternative methods**: **Silhouette analysis** measures how similar points are to their own cluster vs. other clusters, with values in [-1, 1]. Higher average silhouette score indicates better clustering. Plot silhouette score vs. k, choose k with highest score. **Gap statistic** compares WCSS to that expected under a null reference distribution. Choose k where gap is largest. **Cross-validation** uses stability of clusters across data subsets.

**Interpretation**: The elbow method works best when clusters are distinct and roughly spherical (K-means assumptions). If the plot shows smooth decrease with no elbow, the data might not have clear cluster structure, or K-means might not be appropriate. Understanding the elbow method helps diagnose whether K-means is suitable and guides hyperparameter selection.

## Question 12: Exercise Week 14 (Neural networks)
### 12(a) Neural networks prediction (regression vs classification)

**5-6 Minute Pitch:**

Neural networks can perform both **regression** (predicting continuous values) and **classification** (predicting discrete classes), with the main differences being the output layer activation and loss function.

**Architecture**: Both use the same structure - input layer, hidden layers (with non-linear activations like ReLU, tanh, sigmoid), and output layer. The difference is in the **output layer**: **Regression** uses linear activation (or no activation) - outputs can be any real number. **Classification** uses activation functions that produce probabilities: **sigmoid** for binary classification (outputs in [0,1]), **softmax** for multi-class (outputs probability distribution over classes, sums to 1).

**Regression**: Output **ŷ** is a continuous value (or vector for multi-output). Examples: predicting house prices, temperature, stock prices. The network learns a function f(**x**) that maps inputs to continuous targets. **Loss function**: Typically **Mean Squared Error (MSE)** = (1/n)Σ(yᵢ - ŷᵢ)², which penalizes large errors quadratically. **Evaluation**: RMSE, MAE, R².

**Classification**: Output is class probabilities P(class|**x**). For binary: single output with sigmoid gives P(class=1). For multi-class: k outputs with softmax give P(class=i) for each class i. Prediction is the class with highest probability: argmax P(class|**x**). **Loss function**: **Cross-entropy** = -Σᵢ yᵢ log(ŷᵢ), where yᵢ is one-hot encoded true label and ŷᵢ is predicted probability. This is appropriate for probabilities and heavily penalizes confident wrong predictions. **Evaluation**: Accuracy, precision, recall, F1, confusion matrix.

**Key insight**: The same network architecture can switch between regression and classification by changing only the output layer and loss function. Hidden layers learn feature representations that work for both tasks. The choice of output activation ensures outputs are in the correct range (probabilities for classification, unbounded for regression) and the loss function matches the task (MSE for continuous errors, cross-entropy for probability distributions).

### 12(b) Neural networks training (Gradients, the chain rule and back/forward propagation)

**5-6 Minute Pitch:**

Neural network training uses **gradient descent** to minimize loss by computing gradients of the loss with respect to all parameters, enabled by the **chain rule** and implemented via **backpropagation**.

**Forward propagation**: Data flows forward through the network: **a**⁽⁰⁾ = **x** (input), **z**⁽ˡ⁾ = W⁽ˡ⁾**a**⁽ˡ⁻¹⁾ + **b**⁽ˡ⁾ (linear transformation), **a**⁽ˡ⁾ = σ(**z**⁽ˡ⁾) (activation), where l is layer index, W are weights, **b** are biases, σ is activation function. The final output **a**⁽ᴸ⁾ is compared to target **y** via loss function L.

**Gradient descent**: We update parameters to reduce loss: θ ← θ - α∇θL, where α is learning rate and ∇θL is the gradient (vector of partial derivatives ∂L/∂θᵢ). The gradient points in the direction of steepest increase, so moving opposite (negative gradient) decreases loss.

**Chain rule**: For composite functions f(g(x)), the derivative is df/dx = (df/dg)(dg/dx). In neural networks, loss depends on outputs, which depend on activations, which depend on weights. The chain rule lets us compute gradients layer by layer.

**Backpropagation** efficiently computes all gradients using the chain rule: (1) **Forward pass**: Compute activations for all layers, store intermediate values. (2) **Backward pass**: Start from output layer, compute ∂L/∂**a**⁽ᴸ⁾ (loss gradient w.r.t. output). (3) **Propagate backwards**: For each layer l, compute ∂L/∂**z**⁽ˡ⁾ = (∂L/∂**a**⁽ˡ⁾) ⊙ σ'(**z**⁽ˡ⁾) (element-wise product with activation derivative), then ∂L/∂W⁽ˡ⁾ = (∂L/∂**z**⁽ˡ⁾)**a**⁽ˡ⁻¹⁾ᵀ and ∂L/∂**b**⁽ˡ⁾ = ∂L/∂**z**⁽ˡ⁾, and ∂L/∂**a**⁽ˡ⁻¹⁾ = W⁽ˡ⁾ᵀ(∂L/∂**z**⁽ˡ⁾) to continue backwards. (4) **Update**: Use gradients to update all parameters.

**Efficiency**: Backpropagation computes all gradients in one backward pass (O(parameters)), much more efficient than finite differences (O(parameters²)). The chain rule enables this by reusing computations - gradients flow backwards, reusing values computed in forward pass.

**Activation derivatives**: ReLU' = 1 if x > 0 else 0, sigmoid' = σ(1-σ), tanh' = 1-tanh². These are crucial for backpropagation - vanishing gradients occur when derivatives are small (sigmoid, tanh), exploding gradients when derivatives are large.

### 12(c) Training and Evaluation including over/underfitting

**5-6 Minute Pitch:**

Neural network training involves iterative optimization, and proper evaluation is essential to detect and prevent overfitting and underfitting.

**Training process**: (1) **Forward pass** - compute predictions. (2) **Loss computation** - compare predictions to targets. (3) **Backward pass** - compute gradients via backpropagation. (4) **Parameter update** - gradient descent step. (5) Repeat for many epochs (full passes through training data). **Mini-batch training** processes small batches at a time, providing gradient estimates and enabling training on large datasets.

**Evaluation**: We monitor performance on both **training set** (data used for learning) and **validation set** (held-out data not used for training). Metrics depend on task: accuracy, loss, precision/recall for classification; MSE, RMSE, R² for regression. **Learning curves** plot these metrics vs. training epochs.

**Overfitting** occurs when the network memorizes training data instead of learning generalizable patterns. **Symptoms**: Training loss decreases but validation loss increases (or plateaus then increases), large gap between training and validation performance, training accuracy near 100% but validation accuracy much lower. **Causes**: Model too complex relative to data, insufficient training data, training too long (memorizing noise).

**Underfitting** occurs when the network is too simple to capture patterns. **Symptoms**: Both training and validation loss are high and similar, model performance plateaus at poor level, network can't fit training data well. **Causes**: Model too simple (too few layers/neurons), insufficient training, poor initialization, learning rate too high (overshooting optimum).

**Preventing overfitting**: **Regularization** - L2 (weight decay) penalizes large weights, L1 encourages sparsity, dropout randomly disables neurons during training. **Early stopping** - stop training when validation loss stops improving. **Data augmentation** - artificially expand training set. **Reduce model complexity** - fewer layers/neurons. **More training data**.

**Preventing underfitting**: **Increase model capacity** - more layers/neurons, different architectures. **Train longer** - more epochs. **Lower learning rate** - smaller steps, better convergence. **Better initialization** - proper weight initialization. **Feature engineering** - better input representations.

**Best practices**: Use validation set to monitor generalization, stop early if validation performance degrades, compare multiple architectures, use cross-validation for robust estimates, visualize learning curves to diagnose issues.

### 12(d) Model architectures: Difference between fully connected /multi layer perceptron (MLP) and CNN

**5-6 Minute Pitch:**

**Fully Connected (FC) layers** / **Multi-Layer Perceptron (MLP)** and **Convolutional Neural Networks (CNN)** represent different architectural paradigms for different data types and tasks.

**MLP / Fully Connected Networks**: Each neuron in layer l is connected to every neuron in layer l-1. Computation: **a**⁽ˡ⁾ = σ(W⁽ˡ⁾**a**⁽ˡ⁻¹⁾ + **b**⁽ˡ⁾), where W is a dense matrix. **Properties**: Treats input as flat vector (loses spatial structure for images), every input feature connects to every hidden unit, number of parameters is large (if input is 28×28 image = 784 pixels, and first hidden layer has 128 neurons, that's 784×128 = 100,352 parameters just for first layer).

**Use cases**: Works for any data that can be vectorized - tabular data, flattened images, feature vectors. Good for problems where all features interact with all others. **Limitations**: Doesn't exploit spatial structure in images, parameter count grows quadratically with input size, not translation-invariant.

**CNN (Convolutional Neural Networks)**: Uses **convolutional layers** that apply the same small filter (kernel) across the input, sharing parameters. Computation: **a**⁽ˡ⁾ = σ(conv(**a**⁽ˡ⁻¹⁾, K) + **b**), where K is a small kernel (e.g., 3×3) that slides across the input. **Properties**: **Parameter sharing** - same kernel used everywhere, dramatically fewer parameters. **Local connectivity** - each output depends on small local region (receptive field). **Translation invariance** - same features detected regardless of position.

**Architecture**: Typically **conv layers** (feature extraction) → **pooling** (downsampling, e.g., max pooling) → **FC layers** (classification). Early conv layers detect low-level features (edges, textures), deeper layers detect high-level features (shapes, objects).

**Key differences**: **Parameters**: CNN has far fewer (shared kernels vs. dense matrices). **Structure**: CNN preserves spatial structure, MLP flattens it. **Inductive bias**: CNN assumes translation invariance and local patterns, MLP makes no spatial assumptions. **Efficiency**: CNN is more efficient for images due to parameter sharing and local operations.

**When to use**: **MLP** for tabular data, when spatial structure doesn't matter, or when you need global interactions. **CNN** for images, signals, or any data with spatial/temporal structure where translation invariance and local patterns matter. CNNs revolutionized computer vision by exploiting the structure of image data.

### 12(e) Loss functions, model complexity, cross-validation.

**5-6 Minute Pitch:**

**Loss functions, model complexity, and cross-validation** are interconnected concepts for training and evaluating neural networks.

**Loss functions** quantify prediction error and guide optimization. **For regression**: **Mean Squared Error (MSE)** = (1/n)Σ(yᵢ - ŷᵢ)² penalizes large errors quadratically, assumes Gaussian noise. **Mean Absolute Error (MAE)** = (1/n)Σ|yᵢ - ŷᵢ| is more robust to outliers. **Huber loss** combines MSE and MAE (quadratic for small errors, linear for large). **For classification**: **Cross-entropy** = -Σᵢ yᵢ log(ŷᵢ) is standard, appropriate for probabilities, heavily penalizes confident wrong predictions. **Focal loss** downweights easy examples, focusing on hard cases.

The loss function choice affects what the model learns - MSE encourages mean predictions, MAE encourages median, cross-entropy encourages correct class probabilities.

**Model complexity** refers to the capacity to fit complex functions. **Factors**: Number of layers (depth), number of neurons per layer (width), total parameters. More complex models can represent more functions but risk overfitting. **Complexity control**: **Regularization** - L2 (weight decay) penalizes large weights, L1 encourages sparsity, dropout randomly disables neurons. **Architecture choices** - fewer layers/neurons reduce capacity. **Early stopping** - prevents overfitting by stopping when validation loss increases.

**Bias-variance tradeoff**: Simple models (high bias) may underfit, complex models (high variance) may overfit. Optimal complexity balances both. The loss function on training data measures fit quality, but we need validation to assess generalization.

**Cross-validation** provides robust performance estimates and helps select model complexity. **K-fold CV**: Divide data into k folds, train on k-1, validate on 1, repeat k times, average results. This uses all data for both training and validation (at different times), giving more reliable estimates than a single train-test split. **Stratified CV** maintains class distributions in each fold for classification.

**Using CV for model selection**: Train models with different complexities (different architectures, regularization strengths), evaluate each via cross-validation, choose the model with best CV performance. This prevents overfitting to a particular train-test split and provides confidence intervals for performance.

**Learning curves** (performance vs. training size) help diagnose issues: if training and validation curves converge at high error → underfitting (need more complexity). If large gap → overfitting (need less complexity or more data). If both decreasing → more data would help.

The interplay: **Loss function** defines what to optimize, **model complexity** determines capacity, **cross-validation** assesses generalization and guides complexity selection. Together, they enable building models that generalize well to unseen data.

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
