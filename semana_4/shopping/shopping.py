import csv
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(evidence, labels, test_size=TEST_SIZE)

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")

def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        evidence = []
        labels = []
        month_mapping = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}
        
        for row in reader:
            ev = [
                int(row[0]), float(row[1]), int(row[2]), float(row[3]),
                int(row[4]), float(row[5]), float(row[6]), float(row[7]),
                float(row[8]), float(row[9]), month_mapping[row[10]],
                int(row[11]), int(row[12]), int(row[13]), int(row[14]),
                1 if row[15] == 'Returning_Visitor' else 0,
                1 if row[16] == 'TRUE' else 0
            ]
            evidence.append(ev)
            labels.append(1 if row[17] == 'TRUE' else 0)
    return (evidence, labels)

def train_model(evidence, labels):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model

def evaluate(labels, predictions):
    true_positives = sum(1 for i in range(len(labels)) if labels[i] == 1 and predictions[i] == 1)
    true_negatives = sum(1 for i in range(len(labels)) if labels[i] == 0 and predictions[i] == 0)
    
    total_positives = sum(1 for label in labels if label == 1)
    total_negatives = sum(1 for label in labels if label == 0)
    
    sensitivity = true_positives / total_positives if total_positives else 0
    specificity = true_negatives / total_negatives if total_negatives else 0
    
    return (sensitivity, specificity)

if __name__ == "__main__":
    main()
