import matplotlib.pyplot as plt

def train_validation_plot(history, train_metric, validation_metric):
    metric = train_metric

    history_dict = history.history
    train_values = history_dict[train_metric]
    val_values = history_dict[validation_metric]
    
    epochs = range(1, len(train_values) + 1)

    plt.plot(epochs, train_values, "bo", label=f"Training {metric}")
    plt.plot(epochs, val_values, "b", label=f"Validation {metric}")

    plt.title(f"training and validation {metric}")
    plt.xlabel("Epochs")
    plt.ylabel(train_metric)
    plt.legend()
    plt.show()