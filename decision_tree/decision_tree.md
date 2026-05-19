Decision Tree is a supervised learning model used for both classification and regression tasks. It intuitively
applies a series of 'if-else' decisions based on input variables to determine outcomes. The tree splits data
successively into two branches at each node using a single variable, eventually reaching leaf nodes that
provide the final decision or prediction. Each decision node in a decision tree splits data into exactly two
branches, regardless of whether the outcome is continuous or categorical. Decision trees are popular for
their easy visualization and interpretability, which help stakeholders understand the decision-making
process.
Nodes:
• Root Node: The initial node of a decision tree where the first split occurs. It is based on the most
important input variable.
• Decision Nodes: Points in the decision tree where data is further split into branches based on
feature values, such as income or credit history.
• Leaf Nodes: The final nodes of a decision tree representing a subset of data where the outcome is
the same for all observations in the leaf node.
Variables and Data Elements:
• Variables: Features or attributes used by the model for making predictions, like 'age' or 'income' in
the 'titanic' dataset.
• X Variables: Independent variables or features used in a predictive model to explain or predict the
outcome.
• Y Variable: The dependent variable or outcome that the model aims to predict.
• Observation ID: Unique identifiers assigned to individual data points in a dataset(e.g., 1,2, 3.. or R1,
R2, R3….)
Training and Test Data:
• Training Data: The dataset that is used to train a model. The outcome variable (Y) must be available
in the dataset. The model learns patterns by picking the right nodes to minimize prediction error on
this dataset.
• Test Data: The outcome variable (Y) is known, and the model's predictions are compared against it
to test the accuracy and generalization capability of the model.
Model Evaluation Metrics:
• Accuracy/Confusion Metric: A performance metric that measures the percentage of correct
predictions when Y is a categorical variable made by the model compared to the actual values. The
higher, the better. The confusion matrix shows the number of correct and incorrect predictions for
each outcome, Y.
• Mean Square Error: A measure of the average squared difference between the predicted and actual
values, used when Y is continuous. Lower values indicate better performance, implying fewer errors
between predictions and actual outcomes.
• Xerror: A metric used to evaluate the error of a model on test data, indicating how well the model
generalizes to unseen data. It is used to set the CP parameter to prune the decision tree to avoid
overfitting.
ISB-ABA
Overfitting and Underfitting:
• Overfitting: A modeling issue where the model becomes too complex and captures noise instead of
the true pattern in the data leads to poor performance on new, unseen data.
• Underfitting: Occurs when a model is too simple to learn the underlying patterns in the data, often
due to insufficient features or overly simplistic model structure.
Depth of the Tree, CP, and Pruning:
• Depth of the Tree: The number of levels in a decision tree. A deeper tree can capture more
complexity and detail in the data but also risks overfitting by being too specific to the training data.
• Model Complexity: A measure of how intricate a model is; higher complexity can lead to overfitting,
where the model captures noise instead of the underlying pattern. Lower complexity can lead to
underfitting, where the model is too simplistic to capture important details.
• Complexity Parameter (CP): A hyperparameter used to control the size of a decision tree by pruning
less significant branches. Lower values result in larger, more complex trees, while higher values
lead to smaller, simpler trees.
• Pruning: The process of removing branches from a decision tree that contribute little to predictive
accuracy. Pruning helps reduce overfitting and improve generalization to new data.
Predictions and Decision Making:
• Prediction: The act of using a model to estimate or infer the outcome Y variable based on input
data.
• Prediction Column (Y): A new column added to a dataset that contains the model's predictions
based on the input features.
• Decision Tree Visual: A graphical representation of the decision-making process, such as a decision
tree diagram, that makes it easier to interpret and understand the results.
• Patterns: The underlying meaningful structure in the data the model aims to learn to make accurate
predictions.
• Noise: Random errors or variations in the data that obscure the true patterns and make it harder for
the model to generalise well.
