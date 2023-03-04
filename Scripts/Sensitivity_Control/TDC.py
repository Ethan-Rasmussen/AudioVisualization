from sklearn import svm
from sklearn.model_selection import train_test_split

class TDC:
    def __init__(self, scisound_list):
        # Extract relevant features from the SCISound instances
        self.X, self.y = self.extract_features(scisound_list)

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

        # Train the support vector machine
        self.clf = svm.SVC(kernel='rbf', C=1, gamma='scale')
        self.clf.fit(self.X_train, self.y_train)

    def extract_features(self, scisound_list):
        X = []
        y = []
        label_set = set()
        for scisound in scisound_list:
            time_diffs = scisound.sound_features.time_diffs
            for i, time_diff in enumerate(time_diffs):
                # Create a feature vector containing the time difference and its position on the array
                feature_vector = [time_diff, i]

                # Add the other time differences in the same SCISound instance to the feature vector
                for j, other_time_diff in enumerate(time_diffs):
                    if j != i:
                        feature_vector.append(other_time_diff)

                # Append the feature vector and the corresponding label to the training data
                X.append(feature_vector)
                label_set.add(scisound.label)

        # Convert the set of labels to a list, sorted in ascending order
        label_list = sorted(list(label_set))

        # If there is only one label, add a dummy second label to avoid an error in the SVM
        if len(label_list) == 1:
            label_list.append(label_list[0] + 1)

        # Map the original labels to integer values
        y = [label_list.index(label) for label in y]

        return X, y


    def predict(self, time_diffs):
        # Create a feature vector for the input time differences
        feature_vector = []
        for i, time_diff in enumerate(time_diffs):
            feature_vector.append(time_diff)
            for j, other_time_diff in enumerate(time_diffs):
                if j != i:
                    feature_vector.append(other_time_diff)

        # Use the support vector machine to predict whether the input time differences are physically possible
        return self.clf.predict([feature_vector])[0]
