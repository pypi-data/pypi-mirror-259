import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures, OneHotEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.svm import SVR, SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift, AffinityPropagation, SpectralClustering
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, silhouette_score
from sklearn.gaussian_process import GaussianProcessRegressor, GaussianProcessClassifier
from sklearn.mixture import GaussianMixture
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE

class DataExplorer:
    def __init__(self, df):
        self.df = df.copy()

    def feature_importance_analysis(self, X, y):
        """
        Perform feature importance analysis using Random Forest.

        Args:
        X (DataFrame): The feature matrix.
        y (Series): The target variable.

        Returns:
        DataFrame: Feature importance scores.
        """
        # Preprocess categorical variables if present
        categorical_features = X.select_dtypes(include=['object']).columns.tolist()
        if categorical_features:
            df = X.copy()
            for col in categorical_features:
                # Use label encoding for low cardinality columns
                if df[col].nunique() <= 5:
                    label_encoder = LabelEncoder()
                    df[col] = label_encoder.fit_transform(df[col])
                # Use one-hot encoding for high cardinality columns
                else:
                    df = pd.get_dummies(df, columns=[col], drop_first=True)
            X = df

        # Instantiate Random Forest model
        rf_model = RandomForestRegressor()

        # Fit the model
        rf_model.fit(X, y)

        # Retrieve feature importances from the trained model
        importances = rf_model.feature_importances_

        # Create a DataFrame to store feature names and their importances
        feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': importances})

        # Sort the features by importance
        feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

        return feature_importances

    def explore_dataset(self):
        """
        Perform data exploration on the provided DataFrame.

        Returns:
        None
        """
        # Understanding the structure of the dataset
        dataset_shape = pd.DataFrame({"Value": [self.df.shape]})
        dataset_shape.index = ['Dataset Shape']

        # Data types of each column
        column_datatypes = pd.DataFrame(self.df.dtypes, columns=['Data Type'])

        # Display a few sample rows
        sample_rows = self.df.head()

        # Identify numeric and categorical columns
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = self.df.select_dtypes(exclude=[np.number]).columns.tolist()

        # Check for missing values
        missing_values = self.df.isnull().sum().reset_index()
        missing_values.columns = ['Column', 'Missing Values']
        missing_values['Missing Percentage'] = (missing_values['Missing Values'] / len(self.df)) * 100

        # Calculate summary statistics for numerical features
        summary_statistics = self.df.describe().transpose()

        # For categorical features, check unique values and their frequencies
        unique_values_categorical = pd.DataFrame(columns=['Column', 'Unique Percentage'])
        for feature in categorical_columns:
            unique_values = self.df[feature].value_counts().reset_index()
            unique_values.columns = ['Value', 'Frequency']
            unique_values['Column'] = feature
            unique_values['Unique Percentage'] = (unique_values['Frequency'] / len(self.df[feature])) * 100
            unique_values_categorical = pd.concat([unique_values_categorical, unique_values], ignore_index=True)

        # Convert numeric columns and categorical columns into table format
        numeric_columns_df = pd.DataFrame({"Numeric Columns": numeric_columns})
        categorical_columns_df = pd.DataFrame({"Categorical Columns": categorical_columns})

        # Print the results in a tabular format
        print("Dataset Shape:")
        print(dataset_shape)
        print("\nColumn Data Types:")
        print(column_datatypes)
        print("\nSample Rows:")
        print(sample_rows)
        print("\nNumeric Columns:")
        print(numeric_columns_df)
        print("\nCategorical Columns:")
        print(categorical_columns_df)
        print("\nMissing Values:")
        print(missing_values)
        print("\nSummary Statistics:")
        print(summary_statistics)
        print("\nUnique Values for Categorical Columns:")
        print(unique_values_categorical)

    def encode_categorical_columns(self, columns):
        """
        Encode specified categorical columns in the DataFrame.

        Args:
        columns (list): The list of column names to encode.

        Returns:
        DataFrame: The DataFrame with specified categorical columns encoded.
        """
        df = self.df.copy()
        for col in columns:
            # Use label encoding for low cardinality columns
            if df[col].nunique() <= 5:
                label_encoder = LabelEncoder()
                df[col] = label_encoder.fit_transform(df[col])
            # Use one-hot encoding for high cardinality columns
            else:
                df = pd.get_dummies(df, columns=[col], drop_first=True)

        return df

    def evaluate_regression_algorithms(self, X_train, X_test, y_train, y_test):
        algorithms = {
            'Linear Regression': LinearRegression(),
            'Ridge Regression': Ridge(),
            'Lasso Regression': Lasso(),
            'Neural Network Regression': MLPRegressor(),
            'Decision Tree Regression': DecisionTreeRegressor(),
            'Random Forest': RandomForestRegressor(),
            'KNN Model': KNeighborsRegressor(),
            'Support Vector Machines (SVM)': SVR(),
            'Gaussian Regression': GaussianProcessRegressor(),
            'Polynomial Regression': make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
        }

        results = {}
        for name, model in algorithms.items():
            # Fit the model
            model.fit(X_train, y_train)

            # Predict on the test set
            predictions = model.predict(X_test)

            # Calculate evaluation metrics
            mse = mean_squared_error(y_test, predictions)
            rmse = mean_squared_error(y_test, predictions, squared=False)
            mae = mean_absolute_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)

            # Store metrics in dictionary
            results[name] = {'Mean Squared Error': mse, 'Root Mean Squared Error': rmse,
                             'Mean Absolute Error': mae, 'R2 Score': r2}

            # Print results for this model
            print("\nRegression Model:", name)
            print("Mean Squared Error:", mse)
            print("Root Mean Squared Error:", rmse)
            print("Mean Absolute Error:", mae)
            print("R2 Score:", r2)

        # Choose the best model based on average RMSE and R2 score
        best_model = min(results, key=lambda x: (results[x]['Root Mean Squared Error'], -results[x]['R2 Score']))

        # Print the reason for selecting the best model
        print("\nBest Regression Model:", best_model)
        print("Reason: This model has the lowest RMSE and highest R2 Score among all models.")

        return best_model, results[best_model]

    def evaluate_classification_algorithms(self, X_train, X_test, y_train, y_test):
        algorithms = {
            'Logistic Regression': LogisticRegression(),
            'Decision Tree': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier(),
            'SVM': SVC(),
            'k-NN': KNeighborsClassifier(),
            'Naive Bayes': GaussianNB(),
            'Neural Network': MLPClassifier(),
            'Gradient Boosting': GradientBoostingClassifier(),
            'Linear Discriminant Analysis': LinearDiscriminantAnalysis(),
            'Extra Trees': ExtraTreesClassifier(),
            'Bagging': BaggingClassifier(),
            'Gaussian Process': GaussianProcessClassifier()
        }

        results = {}
        for name, model in algorithms.items():
            # Fit the model
            model.fit(X_train, y_train)

            # Predict on the test set
            predictions = model.predict(X_test)

            # Calculate evaluation metrics
            accuracy = accuracy_score(y_test, predictions)
            precision = precision_score(y_test, predictions, average='weighted')
            recall = recall_score(y_test, predictions, average='weighted')
            f1 = f1_score(y_test, predictions, average='weighted')

            # Store metrics in dictionary
            results[name] = {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1 Score': f1}

            # Print results for this model
            print("\nClassification Model:", name)
            print("Accuracy:", accuracy)
            print("Precision:", precision)
            print("Recall:", recall)
            print("F1 Score:", f1)

        # Choose the best model based on average F1 score
        best_model = max(results, key=lambda x: results[x]['F1 Score'])

        # Print the reason for selecting the best model
        print("\nBest Classification Model:", best_model)
        print("Reason: This model has the highest F1 Score among all models.")

        return best_model, results[best_model]

    def evaluate_clustering_algorithms(self, X):
        algorithms = {
            'K-Means': KMeans(),
            'Hierarchical Clustering (Agglomerative)': AgglomerativeClustering(),
            'DBSCAN': DBSCAN(),
            'Mean Shift': MeanShift(),
            'Spectral Clustering': SpectralClustering(),
            'Affinity Propagation': AffinityPropagation(),
            'Gaussian Mixture Models (GMM)': GaussianMixture(),
        }

        results = {}
        for name, model in algorithms.items():
            # Fit the model
            if name == 'Gaussian Mixture Models (GMM)':
                model = GaussianMixture(n_components=5)  # Example: You can specify the number of components
            model.fit(X)

            # Calculate cluster labels
            if name in ['DBSCAN', 'Hierarchical Clustering (Agglomerative)']:
                labels = model.labels_  # For DBSCAN and Agglomerative Clustering
            else:
                labels = model.predict(X)  # For other clustering algorithms

            # Calculate evaluation metrics
            if name != 'DBSCAN':
                silhouette = silhouette_score(X, labels)
                results[name] = {'Silhouette Score': silhouette}
                print("\nClustering Model:", name)
                print("Silhouette Score:", silhouette)
            else:
                # DBSCAN doesn't have a silhouette score, so you may want to handle this differently
                # For example, you could print the number of clusters and noise points
                unique_labels = set(labels)
                num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)  # Exclude noise points
                num_noise_points = list(labels).count(-1)
                print("\nClustering Model: DBSCAN")
                print("Number of Clusters:", num_clusters)
                print("Number of Noise Points:", num_noise_points)

        # Choose the best model based on silhouette score
        if 'DBSCAN' in results:
            del results['DBSCAN']  # Remove DBSCAN from consideration since it doesn't have a silhouette score

        best_model = max(results, key=lambda x: results[x]['Silhouette Score'])

        # Print the reason for selecting the best model
        print("\nBest Clustering Model:", best_model)
        if best_model != 'DBSCAN':
            print("Reason: This model has the highest Silhouette Score among all models.")
        else:
            print(
                "Reason: DBSCAN doesn't have a silhouette score, so the best model selection is based on other metrics.")

        return best_model, results[best_model]

    def handle_imbalanced_data(self, X, y, method='smote'):
        """
        Handle imbalanced data using techniques like oversampling or undersampling.

        Args:
        X (DataFrame): The feature matrix.
        y (Series): The target variable.
        method (str, optional): The resampling method. 'smote' for oversampling using SMOTE,
            'undersample' for undersampling using RandomUnderSampler. Defaults to 'smote'.

        Returns:
        DataFrame: Resampled feature matrix.
        Series: Resampled target variable.
        """
        if method == 'smote':
            sampler = SMOTE()
        elif method == 'undersample':
            sampler = RandomUnderSampler()
        else:
            raise ValueError("Invalid resampling method. Choose either 'smote' or 'undersample'.")

        X_resampled, y_resampled = sampler.fit_resample(X, y)
        return X_resampled, y_resampled

    def content_recommendation_system(dataset, text_data):
        """
        Build a recommendation system using CountVectorizer and cosine similarity.

        Parameters:
            dataset (DataFrame): Dataset loaded as a DataFrame.
            text_data (Series): Series containing textual data for item descriptions.

        Returns:
            function: A function that can be used to get top recommendations for a given item name.
        """
        # Step 3: Feature Extraction (CountVectorizer)
        count_vectorizer = CountVectorizer(stop_words='english')
        count_matrix = count_vectorizer.fit_transform(text_data)

        # Step 4: Build Item Profiles
        item_profiles = count_matrix

        # Step 5: Similarity Calculation
        # Calculate cosine similarity between item profiles
        cosine_sim = cosine_similarity(item_profiles, item_profiles)

        # Step 6: Ranking
        # Define a function to get top recommendations for a given item name
        def recommendation_system(item_name, item_column, n_recommendations):
            item_index = dataset[item_column][dataset[item_column] == item_name].index[0]
            sim_scores = list(enumerate(cosine_sim[item_index]))
            sim_scores.sort(key=lambda x: x[1], reverse=True)
            top_indices = [i[0] for i in sim_scores[1:n_recommendations + 1]]  # Exclude the item itself
            return dataset[item_column].iloc[top_indices].tolist(), item_column

        return recommendation_system